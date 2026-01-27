from flask import Flask, render_template, redirect, url_for, flash, request, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from functools import wraps
from datetime import datetime, timedelta
import os
from models import db, User, Pass, Reservation, Shoes, Payment
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

def receptionist_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'receptionist':
            flash('You need receptionist privileges to access this page.', 'danger')
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role', 'client')
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists.', 'danger')
            return redirect(url_for('register'))
        
        if User.query.filter_by(email=email).first():
            flash('Email already exists.', 'danger')
            return redirect(url_for('register'))
        
        user = User(username=username, email=email, role=role)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            flash(f'Welcome back, {user.username}!', 'success')
            
            if user.role == 'receptionist':
                return redirect(url_for('receptionist_dashboard'))
            else:
                return redirect(url_for('client_dashboard'))
        else:
            flash('Invalid username or password.', 'danger')
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))

@app.route('/client/dashboard')
@login_required
def client_dashboard():
    if current_user.role != 'client':
        return redirect(url_for('receptionist_dashboard'))
    
    passes = Pass.query.filter_by(user_id=current_user.id).all()
    
    reservations = Reservation.query.filter_by(user_id=current_user.id).order_by(Reservation.reservation_date.desc()).all()
    
    return render_template('client_dashboard.html', passes=passes, reservations=reservations)

@app.route('/client/view-slots')
@login_required
def view_slots():
    if current_user.role != 'client':
        flash('Access denied.', 'danger')
        return redirect(url_for('index'))
    
    slots = []
    time_slots = ['09:00-11:00', '11:00-13:00', '13:00-15:00', '15:00-17:00', '17:00-19:00', '19:00-21:00']
    
    for i in range(30):
        date = datetime.now().date() + timedelta(days=i)
        for time_slot in time_slots:
            existing = Reservation.query.filter_by(
                reservation_date=datetime.combine(date, datetime.min.time()),
                time_slot=time_slot,
                status='confirmed'
            ).count()
            
            available = existing < 20
            slots.append({
                'date': date,
                'time_slot': time_slot,
                'available': available,
                'spots_left': 20 - existing
            })
    
    return render_template('view_slots.html', slots=slots)

@app.route('/client/book-entry', methods=['POST'])
@login_required
def book_entry():
    if current_user.role != 'client':
        return jsonify({'success': False, 'message': 'Access denied'}), 403
    
    date_str = request.form.get('date')
    time_slot = request.form.get('time_slot')
    
    valid_pass = Pass.query.filter_by(user_id=current_user.id, is_active=True).first()
    if not valid_pass or not valid_pass.is_valid():
        flash('You need a valid pass to book an entry.', 'danger')
        return redirect(url_for('view_slots'))
    
    reservation_date = datetime.strptime(date_str, '%Y-%m-%d')
    
    existing = Reservation.query.filter_by(
        reservation_date=reservation_date,
        time_slot=time_slot,
        status='confirmed'
    ).count()
    
    if existing >= 20:
        flash('This slot is fully booked.', 'danger')
        return redirect(url_for('view_slots'))
    
    reservation = Reservation(
        user_id=current_user.id,
        reservation_date=reservation_date,
        time_slot=time_slot,
        status='pending'
    )
    db.session.add(reservation)
    db.session.commit()
    
    flash('Reservation created successfully!', 'success')
    return redirect(url_for('client_dashboard'))

@app.route('/client/buy-pass', methods=['GET', 'POST'])
@login_required
def buy_pass():
    if current_user.role != 'client':
        flash('Access denied.', 'danger')
        return redirect(url_for('index'))
    
    if request.method == 'POST':
        pass_type = request.form.get('pass_type')
        
        pass_options = {
            '10-entry': {'entries': 10, 'price': 100.0, 'expiry_days': None},
            '20-entry': {'entries': 20, 'price': 180.0, 'expiry_days': None},
            '30-day': {'entries': None, 'price': 150.0, 'expiry_days': 30},
            '90-day': {'entries': None, 'price': 400.0, 'expiry_days': 90},
        }
        
        if pass_type not in pass_options:
            flash('Invalid pass type.', 'danger')
            return redirect(url_for('buy_pass'))
        
        option = pass_options[pass_type]
        
        new_pass = Pass(
            user_id=current_user.id,
            pass_type=pass_type,
            entries_total=option['entries'],
            entries_remaining=option['entries'],
            expiry_date=datetime.utcnow() + timedelta(days=option['expiry_days']) if option['expiry_days'] else None,
            price=option['price']
        )
        db.session.add(new_pass)
        db.session.flush()
        
        payment = Payment(
            user_id=current_user.id,
            amount=option['price'],
            payment_type='pass',
            description=f'Purchase of {pass_type} pass',
            pass_id=new_pass.id
        )
        db.session.add(payment)
        
        db.session.commit()
        
        flash(f'Successfully purchased {pass_type} pass!', 'success')
        return redirect(url_for('client_dashboard'))
    
    return render_template('buy_pass.html')

@app.route('/receptionist/dashboard')
@login_required
@receptionist_required
def receptionist_dashboard():
    today = datetime.now().date()
    today_reservations = Reservation.query.filter(
        db.func.date(Reservation.reservation_date) == today
    ).all()
    
    total_shoes = Shoes.query.count()
    rented_shoes = Shoes.query.filter_by(is_available=False).count()
    
    return render_template('receptionist_dashboard.html', 
                         reservations=today_reservations,
                         total_shoes=total_shoes,
                         rented_shoes=rented_shoes)

@app.route('/receptionist/search-bookings', methods=['GET', 'POST'])
@login_required
@receptionist_required
def search_bookings():
    reservations = []
    
    if request.method == 'POST':
        search_term = request.form.get('search_term')
        date_str = request.form.get('date')
        
        query = Reservation.query.join(User)
        
        if search_term:
            query = query.filter(
                (User.username.contains(search_term)) | 
                (User.email.contains(search_term))
            )
        
        if date_str:
            search_date = datetime.strptime(date_str, '%Y-%m-%d')
            query = query.filter(db.func.date(Reservation.reservation_date) == search_date.date())
        
        reservations = query.all()
    
    return render_template('search_bookings.html', reservations=reservations)

@app.route('/receptionist/confirm-entry/<int:reservation_id>', methods=['POST'])
@login_required
@receptionist_required
def confirm_entry(reservation_id):
    reservation = Reservation.query.get_or_404(reservation_id)
    
    valid_pass = Pass.query.filter_by(user_id=reservation.user_id, is_active=True).first()
    
    if not valid_pass or not valid_pass.is_valid():
        flash('User does not have a valid pass.', 'danger')
        return redirect(url_for('search_bookings'))
    
    if valid_pass.entries_remaining is not None:
        valid_pass.deduct_entry()
    
    reservation.status = 'confirmed'
    reservation.confirmed_by = current_user.id
    
    db.session.commit()
    
    flash('Entry confirmed successfully!', 'success')
    return redirect(url_for('search_bookings'))

@app.route('/receptionist/check-pass/<int:user_id>')
@login_required
@receptionist_required
def check_pass(user_id):
    user = User.query.get_or_404(user_id)
    passes = Pass.query.filter_by(user_id=user_id).all()
    
    return render_template('check_pass.html', user=user, passes=passes)

@app.route('/receptionist/sell-pass', methods=['GET', 'POST'])
@login_required
@receptionist_required
def sell_pass():
    if request.method == 'POST':
        username = request.form.get('username')
        pass_type = request.form.get('pass_type')
        
        user = User.query.filter_by(username=username).first()
        if not user:
            flash('User not found.', 'danger')
            return redirect(url_for('sell_pass'))
        
        pass_options = {
            '10-entry': {'entries': 10, 'price': 100.0, 'expiry_days': None},
            '20-entry': {'entries': 20, 'price': 180.0, 'expiry_days': None},
            '30-day': {'entries': None, 'price': 150.0, 'expiry_days': 30},
            '90-day': {'entries': None, 'price': 400.0, 'expiry_days': 90},
        }
        
        if pass_type not in pass_options:
            flash('Invalid pass type.', 'danger')
            return redirect(url_for('sell_pass'))
        
        option = pass_options[pass_type]
        
        new_pass = Pass(
            user_id=user.id,
            pass_type=pass_type,
            entries_total=option['entries'],
            entries_remaining=option['entries'],
            expiry_date=datetime.utcnow() + timedelta(days=option['expiry_days']) if option['expiry_days'] else None,
            price=option['price']
        )
        db.session.add(new_pass)
        db.session.flush()
        
        payment = Payment(
            user_id=user.id,
            amount=option['price'],
            payment_type='pass',
            description=f'Purchase of {pass_type} pass (sold by receptionist)',
            pass_id=new_pass.id
        )
        db.session.add(payment)
        
        db.session.commit()
        
        flash(f'Successfully sold {pass_type} pass to {username}!', 'success')
        return redirect(url_for('receptionist_dashboard'))
    
    return render_template('sell_pass.html')

@app.route('/receptionist/shoes', methods=['GET', 'POST'])
@login_required
@receptionist_required
def manage_shoes():
    if request.method == 'POST':
        action = request.form.get('action')
        
        if action == 'add':
            size = float(request.form.get('size'))
            shoe = Shoes(size=size)
            db.session.add(shoe)
            db.session.commit()
            flash(f'Added shoes size {size}', 'success')
        
        elif action == 'rent':
            shoe_id = int(request.form.get('shoe_id'))
            username = request.form.get('username')
            
            shoe = Shoes.query.get_or_404(shoe_id)
            user = User.query.filter_by(username=username).first()
            
            if not user:
                flash('User not found.', 'danger')
            elif not shoe.is_available:
                flash('Shoes are already rented.', 'danger')
            else:
                shoe.is_available = False
                shoe.current_renter_id = user.id
                shoe.rental_date = datetime.utcnow()
                
                payment = Payment(
                    user_id=user.id,
                    amount=5.0,
                    payment_type='shoe_rental',
                    description=f'Shoe rental - size {shoe.size}'
                )
                db.session.add(payment)
                db.session.commit()
                
                flash(f'Rented shoes size {shoe.size} to {username}', 'success')
        
        elif action == 'return':
            shoe_id = int(request.form.get('shoe_id'))
            shoe = Shoes.query.get_or_404(shoe_id)
            
            if shoe.is_available:
                flash('Shoes are not currently rented.', 'danger')
            else:
                shoe.is_available = True
                shoe.current_renter_id = None
                shoe.rental_date = None
                db.session.commit()
                
                flash(f'Returned shoes size {shoe.size}', 'success')
    
    shoes = Shoes.query.all()
    return render_template('manage_shoes.html', shoes=shoes)

def init_db():
    with app.app_context():
        db.create_all()
        
        if not User.query.filter_by(username='receptionist').first():
            receptionist = User(
                username='receptionist',
                email='receptionist@bouldergym.com',
                role='receptionist'
            )
            receptionist.set_password('admin123')
            db.session.add(receptionist)
            db.session.commit()
            print('Created default receptionist account (username: receptionist, password: admin123)')
        
        if Shoes.query.count() == 0:
            for size in [7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0]:
                shoe = Shoes(size=size)
                db.session.add(shoe)
            db.session.commit()
            print('Added sample shoes')

if __name__ == '__main__':
    init_db()
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)

