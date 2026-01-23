from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    """User model for both Clients and Receptionists"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), nullable=False, default='client')  # 'client' or 'receptionist'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    reservations = db.relationship('Reservation', backref='user', lazy=True, cascade='all, delete-orphan')
    passes = db.relationship('Pass', backref='user', lazy=True, cascade='all, delete-orphan')
    payments = db.relationship('Payment', backref='user', lazy=True, cascade='all, delete-orphan')
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f'<User {self.username}>'

class Pass(db.Model):
    """Pass model for gym entries"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    pass_type = db.Column(db.String(50), nullable=False)  # e.g., '10-entry', '30-day'
    entries_total = db.Column(db.Integer, nullable=True)  # Total entries for entry-based passes
    entries_remaining = db.Column(db.Integer, nullable=True)  # Remaining entries
    expiry_date = db.Column(db.DateTime, nullable=True)  # Expiry date for time-based passes
    purchase_date = db.Column(db.DateTime, default=datetime.utcnow)
    price = db.Column(db.Float, nullable=False)
    is_active = db.Column(db.Boolean, default=True)
    
    def is_valid(self):
        """Check if pass is valid (not expired and has entries)"""
        if not self.is_active:
            return False
        if self.expiry_date and self.expiry_date < datetime.utcnow():
            return False
        if self.entries_remaining is not None and self.entries_remaining <= 0:
            return False
        return True
    
    def deduct_entry(self):
        """Deduct one entry from the pass"""
        if self.entries_remaining is not None and self.entries_remaining > 0:
            self.entries_remaining -= 1
            if self.entries_remaining == 0:
                self.is_active = False
            return True
        return False
    
    def __repr__(self):
        return f'<Pass {self.pass_type} for User {self.user_id}>'

class Reservation(db.Model):
    """Reservation model for booking gym slots"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    reservation_date = db.Column(db.DateTime, nullable=False)
    time_slot = db.Column(db.String(20), nullable=False)  # e.g., '09:00-11:00'
    status = db.Column(db.String(20), default='pending')  # 'pending', 'confirmed', 'cancelled'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    confirmed_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    
    def __repr__(self):
        return f'<Reservation {self.id} for {self.reservation_date} {self.time_slot}>'

class Shoes(db.Model):
    """Shoes model for rental tracking"""
    id = db.Column(db.Integer, primary_key=True)
    size = db.Column(db.Float, nullable=False)
    is_available = db.Column(db.Boolean, default=True)
    condition = db.Column(db.String(20), default='good')  # 'good', 'fair', 'poor'
    
    # Rental tracking
    current_renter_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    rental_date = db.Column(db.DateTime, nullable=True)
    
    def __repr__(self):
        return f'<Shoes size {self.size}>'

class Payment(db.Model):
    """Payment model for tracking transactions"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    payment_type = db.Column(db.String(50), nullable=False)  # 'pass', 'shoe_rental'
    description = db.Column(db.String(200))
    payment_date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='completed')  # 'completed', 'pending', 'refunded'
    
    # Reference to what was purchased
    pass_id = db.Column(db.Integer, db.ForeignKey('pass.id'), nullable=True)
    
    def __repr__(self):
        return f'<Payment {self.id} - ${self.amount}>'
