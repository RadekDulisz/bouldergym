import pytest
from datetime import datetime, timedelta
from models import db, User, Pass, Reservation, Shoes, Payment
from app import app

@pytest.fixture
def test_app():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(test_app):
    return test_app.test_client()

@pytest.fixture
def sample_client_user(test_app):
    with test_app.app_context():
        user = User(username='client1', email='client1@example.com', role='client')
        user.set_password('password123')
        db.session.add(user)
        db.session.commit()
        return user.id

@pytest.fixture
def sample_receptionist(test_app):
    with test_app.app_context():
        receptionist = User(username='receptionist', email='receptionist@example.com', role='receptionist')
        receptionist.set_password('admin123')
        db.session.add(receptionist)
        db.session.commit()
        return receptionist.id

class TestIndexRoute:
    def test_index_page(self, client):
        response = client.get('/')
        assert response.status_code == 200
        assert b'Boulder Gym' in response.data or b'Gym' in response.data

class TestRegistrationRoute:
    def test_get_register_page(self, client):
        response = client.get('/register')
        assert response.status_code == 200
    
    def test_register_new_user(self, client):
        response = client.post('/register', data={
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password': 'password123',
            'role': 'client'
        }, follow_redirects=True)
        
        assert response.status_code == 200
        assert b'Registration successful' in response.data
    
    def test_register_duplicate_username(self, client, sample_client_user):
        response = client.post('/register', data={
            'username': 'client1',
            'email': 'different@example.com',
            'password': 'password123',
            'role': 'client'
        }, follow_redirects=True)
        
        assert b'Username already exists' in response.data
    
    def test_register_duplicate_email(self, client, sample_client_user):
        response = client.post('/register', data={
            'username': 'differentuser',
            'email': 'client1@example.com',
            'password': 'password123',
            'role': 'client'
        }, follow_redirects=True)
        
        assert b'Email already exists' in response.data

class TestLoginRoute:
    def test_get_login_page(self, client):
        response = client.get('/login')
        assert response.status_code == 200
    
    def test_login_valid_client(self, client, sample_client_user):
        response = client.post('/login', data={
            'username': 'client1',
            'password': 'password123'
        }, follow_redirects=True)
        
        assert response.status_code == 200
        assert b'Welcome back' in response.data
    
    def test_login_valid_receptionist(self, client, sample_receptionist):
        response = client.post('/login', data={
            'username': 'receptionist',
            'password': 'admin123'
        }, follow_redirects=True)
        
        assert response.status_code == 200
    
    def test_login_invalid_password(self, client, sample_client_user):
        response = client.post('/login', data={
            'username': 'client1',
            'password': 'wrongpassword'
        }, follow_redirects=True)
        
        assert b'Invalid username or password' in response.data
    
    def test_login_nonexistent_user(self, client):
        response = client.post('/login', data={
            'username': 'nonexistent',
            'password': 'password123'
        }, follow_redirects=True)
        
        assert b'Invalid username or password' in response.data

class TestLogoutRoute:
    def test_logout(self, client, sample_client_user):
        client.post('/login', data={
            'username': 'client1',
            'password': 'password123'
        })
        
        response = client.get('/logout', follow_redirects=True)
        assert response.status_code == 200
        assert b'logged out' in response.data

class TestClientDashboard:
    def test_client_dashboard_requires_login(self, client):
        response = client.get('/client/dashboard', follow_redirects=True)
        assert response.status_code == 200
        assert b'login' in response.data.lower() or response.request.path == '/login'
    
    def test_client_dashboard_access(self, client, sample_client_user):
        client.post('/login', data={
            'username': 'client1',
            'password': 'password123'
        })
        
        response = client.get('/client/dashboard')
        assert response.status_code == 200

class TestReceptionistDashboard:
    def test_receptionist_dashboard_requires_login(self, client):
        response = client.get('/receptionist/dashboard', follow_redirects=True)
        assert response.status_code == 200
    
    def test_receptionist_dashboard_requires_role(self, client, sample_client_user):
        client.post('/login', data={
            'username': 'client1',
            'password': 'password123'
        })
        
        response = client.get('/receptionist/dashboard', follow_redirects=True)
        assert b'receptionist privileges' in response.data or b'Access denied' in response.data
    
    def test_receptionist_dashboard_access(self, client, sample_receptionist):
        client.post('/login', data={
            'username': 'receptionist',
            'password': 'admin123'
        })
        
        response = client.get('/receptionist/dashboard')
        assert response.status_code == 200

class TestBuyPass:
    def test_buy_pass_page_access(self, client, sample_client_user):
        client.post('/login', data={
            'username': 'client1',
            'password': 'password123'
        })
        
        response = client.get('/client/buy-pass')
        assert response.status_code == 200
    
    def test_buy_entry_pass(self, client, test_app, sample_client_user):
        client.post('/login', data={
            'username': 'client1',
            'password': 'password123'
        })
        
        response = client.post('/client/buy-pass', data={
            'pass_type': '10-entry'
        }, follow_redirects=True)
        
        assert response.status_code == 200
        assert b'Successfully purchased' in response.data
        
        with test_app.app_context():
            pass_obj = Pass.query.filter_by(user_id=sample_client_user).first()
            assert pass_obj is not None
            assert pass_obj.pass_type == '10-entry'
            assert pass_obj.entries_remaining == 10
    
    def test_buy_time_pass(self, client, test_app, sample_client_user):
        client.post('/login', data={
            'username': 'client1',
            'password': 'password123'
        })
        
        response = client.post('/client/buy-pass', data={
            'pass_type': '30-day'
        }, follow_redirects=True)
        
        assert response.status_code == 200
        
        with test_app.app_context():
            pass_obj = Pass.query.filter_by(user_id=sample_client_user).first()
            assert pass_obj is not None
            assert pass_obj.pass_type == '30-day'
    
    def test_prevent_multiple_active_passes(self, client, test_app, sample_client_user):
        with test_app.app_context():
            user = User.query.get(sample_client_user)
            existing_pass = Pass(
                user_id=user.id,
                pass_type='10-entry',
                entries_total=10,
                entries_remaining=5,
                price=100.0,
                is_active=True
            )
            db.session.add(existing_pass)
            db.session.commit()
        
        client.post('/login', data={
            'username': 'client1',
            'password': 'password123'
        })
        
        response = client.post('/client/buy-pass', data={
            'pass_type': '20-entry'
        }, follow_redirects=True)
        
        assert b'already have an active pass' in response.data

class TestBooking:
    def test_view_slots_page(self, client, sample_client_user):
        client.post('/login', data={
            'username': 'client1',
            'password': 'password123'
        })
        
        response = client.get('/client/view-slots')
        assert response.status_code == 200
    
    def test_book_entry_without_pass(self, client, sample_client_user):
        client.post('/login', data={
            'username': 'client1',
            'password': 'password123'
        })
        
        tomorrow = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        response = client.post('/client/book-entry', data={
            'date': tomorrow,
            'time_slot': '09:00-11:00'
        }, follow_redirects=True)
        
        assert b'need a valid pass' in response.data
    
    def test_book_entry_with_pass(self, client, test_app, sample_client_user):
        with test_app.app_context():
            user = User.query.get(sample_client_user)
            pass_obj = Pass(
                user_id=user.id,
                pass_type='10-entry',
                entries_total=10,
                entries_remaining=10,
                price=100.0,
                is_active=True
            )
            db.session.add(pass_obj)
            db.session.commit()
        
        client.post('/login', data={
            'username': 'client1',
            'password': 'password123'
        })
        
        tomorrow = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        response = client.post('/client/book-entry', data={
            'date': tomorrow,
            'time_slot': '09:00-11:00'
        }, follow_redirects=True)
        
        assert b'Reservation created successfully' in response.data
        
        with test_app.app_context():
            reservation = Reservation.query.filter_by(user_id=sample_client_user).first()
            assert reservation is not None
            assert reservation.status == 'pending'
    
    def test_prevent_duplicate_booking(self, client, test_app, sample_client_user):
        with test_app.app_context():
            user = User.query.get(sample_client_user)
            pass_obj = Pass(
                user_id=user.id,
                pass_type='10-entry',
                entries_total=10,
                entries_remaining=10,
                price=100.0,
                is_active=True
            )
            db.session.add(pass_obj)
            
            tomorrow = datetime.now() + timedelta(days=1)
            existing_reservation = Reservation(
                user_id=user.id,
                reservation_date=tomorrow,
                time_slot='09:00-11:00',
                status='pending'
            )
            db.session.add(existing_reservation)
            db.session.commit()
        
        client.post('/login', data={
            'username': 'client1',
            'password': 'password123'
        })
        
        tomorrow_str = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
        response = client.post('/client/book-entry', data={
            'date': tomorrow_str,
            'time_slot': '09:00-11:00'
        }, follow_redirects=True)
        
        assert b'already have a reservation' in response.data

class TestConfirmEntry:
    def test_confirm_entry(self, client, test_app, sample_client_user, sample_receptionist):
        with test_app.app_context():
            user = User.query.get(sample_client_user)
            pass_obj = Pass(
                user_id=user.id,
                pass_type='10-entry',
                entries_total=10,
                entries_remaining=10,
                price=100.0,
                is_active=True
            )
            db.session.add(pass_obj)
            
            reservation = Reservation(
                user_id=user.id,
                reservation_date=datetime.now(),
                time_slot='09:00-11:00',
                status='pending'
            )
            db.session.add(reservation)
            db.session.commit()
            reservation_id = reservation.id
        
        client.post('/login', data={
            'username': 'receptionist',
            'password': 'admin123'
        })
        
        response = client.post(f'/receptionist/confirm-entry/{reservation_id}', 
                              follow_redirects=True)
        
        assert response.status_code == 200
        
        with test_app.app_context():
            reservation = Reservation.query.get(reservation_id)
            assert reservation.status == 'confirmed'
            
            pass_obj = Pass.query.filter_by(user_id=sample_client_user).first()
            assert pass_obj.entries_remaining == 9

class TestShoesManagement:
    def test_add_shoes(self, client, test_app, sample_receptionist):
        client.post('/login', data={
            'username': 'receptionist',
            'password': 'admin123'
        })
        
        response = client.post('/receptionist/shoes', data={
            'action': 'add',
            'size': 9.5
        }, follow_redirects=True)
        
        assert response.status_code == 200
        assert b'Added shoes' in response.data
        
        with test_app.app_context():
            shoe = Shoes.query.filter_by(size=9.5).first()
            assert shoe is not None
    
    def test_rent_shoes(self, client, test_app, sample_client_user, sample_receptionist):
        with test_app.app_context():
            shoe = Shoes(size=10.0, is_available=True)
            db.session.add(shoe)
            db.session.commit()
            shoe_id = shoe.id
        
        client.post('/login', data={
            'username': 'receptionist',
            'password': 'admin123'
        })
        
        response = client.post('/receptionist/shoes', data={
            'action': 'rent',
            'shoe_id': shoe_id,
            'username': 'client1'
        }, follow_redirects=True)
        
        assert response.status_code == 200
        assert b'Rented shoes' in response.data
        
        with test_app.app_context():
            shoe = Shoes.query.get(shoe_id)
            assert shoe.is_available is False
            assert shoe.current_renter_id == sample_client_user
    
    def test_return_shoes(self, client, test_app, sample_client_user, sample_receptionist):
        with test_app.app_context():
            user = User.query.get(sample_client_user)
            shoe = Shoes(size=10.0, is_available=False, current_renter_id=user.id)
            db.session.add(shoe)
            db.session.commit()
            shoe_id = shoe.id
        
        client.post('/login', data={
            'username': 'receptionist',
            'password': 'admin123'
        })
        
        response = client.post('/receptionist/shoes', data={
            'action': 'return',
            'shoe_id': shoe_id
        }, follow_redirects=True)
        
        assert response.status_code == 200
        assert b'Returned shoes' in response.data
        
        with test_app.app_context():
            shoe = Shoes.query.get(shoe_id)
            assert shoe.is_available is True
            assert shoe.current_renter_id is None
