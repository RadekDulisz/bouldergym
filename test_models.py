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
def sample_user(test_app):
    with test_app.app_context():
        user = User(username='testuser', email='test@example.com', role='client')
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

class TestUserModel:
    def test_user_creation(self, test_app):
        with test_app.app_context():
            user = User(username='john', email='john@example.com', role='client')
            user.set_password('secret')
            db.session.add(user)
            db.session.commit()
            
            assert user.id is not None
            assert user.username == 'john'
            assert user.email == 'john@example.com'
            assert user.role == 'client'
            assert user.password_hash is not None
    
    def test_password_hashing(self, test_app):
        with test_app.app_context():
            user = User(username='alice', email='alice@example.com')
            user.set_password('mypassword')
            
            assert user.password_hash != 'mypassword'
            assert user.check_password('mypassword') is True
            assert user.check_password('wrongpassword') is False
    
    def test_user_representation(self, test_app):
        with test_app.app_context():
            user = User(username='bob', email='bob@example.com')
            assert repr(user) == '<User bob>'

class TestPassModel:
    def test_entry_pass_creation(self, test_app, sample_user):
        with test_app.app_context():
            user = User.query.get(sample_user)
            pass_obj = Pass(
                user_id=user.id,
                pass_type='10-entry',
                entries_total=10,
                entries_remaining=10,
                price=100.0
            )
            db.session.add(pass_obj)
            db.session.commit()
            
            assert pass_obj.id is not None
            assert pass_obj.pass_type == '10-entry'
            assert pass_obj.entries_remaining == 10
            assert pass_obj.is_active is True
    
    def test_time_pass_creation(self, test_app, sample_user):
        with test_app.app_context():
            user = User.query.get(sample_user)
            expiry = datetime.utcnow() + timedelta(days=30)
            pass_obj = Pass(
                user_id=user.id,
                pass_type='30-day',
                expiry_date=expiry,
                price=150.0
            )
            db.session.add(pass_obj)
            db.session.commit()
            
            assert pass_obj.pass_type == '30-day'
            assert pass_obj.entries_total is None
            assert pass_obj.expiry_date is not None
    
    def test_pass_is_valid_active(self, test_app, sample_user):
        with test_app.app_context():
            user = User.query.get(sample_user)
            pass_obj = Pass(
                user_id=user.id,
                pass_type='10-entry',
                entries_total=10,
                entries_remaining=5,
                price=100.0,
                is_active=True
            )
            db.session.add(pass_obj)
            db.session.commit()
            
            assert pass_obj.is_valid() is True
    
    def test_pass_is_valid_expired(self, test_app, sample_user):
        with test_app.app_context():
            user = User.query.get(sample_user)
            expiry = datetime.utcnow() - timedelta(days=1)
            pass_obj = Pass(
                user_id=user.id,
                pass_type='30-day',
                expiry_date=expiry,
                price=150.0
            )
            db.session.add(pass_obj)
            db.session.commit()
            
            assert pass_obj.is_valid() is False
    
    def test_pass_is_valid_no_entries(self, test_app, sample_user):
        with test_app.app_context():
            user = User.query.get(sample_user)
            pass_obj = Pass(
                user_id=user.id,
                pass_type='10-entry',
                entries_total=10,
                entries_remaining=0,
                price=100.0
            )
            db.session.add(pass_obj)
            db.session.commit()
            
            assert pass_obj.is_valid() is False
    
    def test_deduct_entry(self, test_app, sample_user):
        with test_app.app_context():
            user = User.query.get(sample_user)
            pass_obj = Pass(
                user_id=user.id,
                pass_type='10-entry',
                entries_total=10,
                entries_remaining=1,
                price=100.0
            )
            db.session.add(pass_obj)
            db.session.commit()
            
            result = pass_obj.deduct_entry()
            
            assert result is True
            assert pass_obj.entries_remaining == 0
            assert pass_obj.is_active is False
    
    def test_deduct_entry_multiple(self, test_app, sample_user):
        with test_app.app_context():
            user = User.query.get(sample_user)
            pass_obj = Pass(
                user_id=user.id,
                pass_type='10-entry',
                entries_total=10,
                entries_remaining=5,
                price=100.0
            )
            db.session.add(pass_obj)
            db.session.commit()
            
            pass_obj.deduct_entry()
            assert pass_obj.entries_remaining == 4
            assert pass_obj.is_active is True
            
            pass_obj.deduct_entry()
            assert pass_obj.entries_remaining == 3

class TestReservationModel:
    def test_reservation_creation(self, test_app, sample_user):
        with test_app.app_context():
            user = User.query.get(sample_user)
            reservation = Reservation(
                user_id=user.id,
                reservation_date=datetime.now() + timedelta(days=1),
                time_slot='09:00-11:00',
                status='pending'
            )
            db.session.add(reservation)
            db.session.commit()
            
            assert reservation.id is not None
            assert reservation.time_slot == '09:00-11:00'
            assert reservation.status == 'pending'
    
    def test_reservation_representation(self, test_app, sample_user):
        with test_app.app_context():
            user = User.query.get(sample_user)
            date = datetime(2026, 2, 1, 10, 0)
            reservation = Reservation(
                user_id=user.id,
                reservation_date=date,
                time_slot='09:00-11:00'
            )
            db.session.add(reservation)
            db.session.commit()
            
            expected = f'<Reservation {reservation.id} for {date} 09:00-11:00>'
            assert repr(reservation) == expected

class TestShoesModel:
    def test_shoes_creation(self, test_app):
        with test_app.app_context():
            shoe = Shoes(size=9.0)
            db.session.add(shoe)
            db.session.commit()
            
            assert shoe.id is not None
            assert shoe.size == 9.0
            assert shoe.is_available is True
            assert shoe.condition == 'good'
    
    def test_shoes_rental(self, test_app, sample_user):
        with test_app.app_context():
            user = User.query.get(sample_user)
            shoe = Shoes(size=10.0)
            db.session.add(shoe)
            db.session.commit()
            
            shoe.is_available = False
            shoe.current_renter_id = user.id
            shoe.rental_date = datetime.utcnow()
            db.session.commit()
            
            assert shoe.is_available is False
            assert shoe.current_renter_id == user.id
            assert shoe.rental_date is not None
    
    def test_shoes_representation(self, test_app):
        with test_app.app_context():
            shoe = Shoes(size=8.5)
            assert repr(shoe) == '<Shoes size 8.5>'

class TestPaymentModel:
    def test_payment_creation(self, test_app, sample_user):
        with test_app.app_context():
            user = User.query.get(sample_user)
            payment = Payment(
                user_id=user.id,
                amount=100.0,
                payment_type='pass',
                description='10-entry pass purchase'
            )
            db.session.add(payment)
            db.session.commit()
            
            assert payment.id is not None
            assert payment.amount == 100.0
            assert payment.payment_type == 'pass'
            assert payment.status == 'completed'
    
    def test_payment_representation(self, test_app, sample_user):
        with test_app.app_context():
            user = User.query.get(sample_user)
            payment = Payment(
                user_id=user.id,
                amount=5.0,
                payment_type='shoe_rental',
                description='Shoe rental'
            )
            db.session.add(payment)
            db.session.commit()
            
            expected = f'<Payment {payment.id} - $5.0>'
            assert repr(payment) == expected

class TestRelationships:
    def test_user_pass_relationship(self, test_app, sample_user):
        with test_app.app_context():
            user = User.query.get(sample_user)
            pass_obj = Pass(
                user_id=user.id,
                pass_type='10-entry',
                entries_total=10,
                entries_remaining=10,
                price=100.0
            )
            db.session.add(pass_obj)
            db.session.commit()
            
            assert len(user.passes) == 1
            assert user.passes[0].pass_type == '10-entry'
    
    def test_user_reservation_relationship(self, test_app, sample_user):
        with test_app.app_context():
            user = User.query.get(sample_user)
            reservation = Reservation(
                user_id=user.id,
                reservation_date=datetime.now() + timedelta(days=1),
                time_slot='09:00-11:00'
            )
            db.session.add(reservation)
            db.session.commit()
            
            assert len(user.reservations) == 1
            assert user.reservations[0].time_slot == '09:00-11:00'
    
    def test_shoes_renter_relationship(self, test_app, sample_user):
        with test_app.app_context():
            user = User.query.get(sample_user)
            shoe = Shoes(size=9.0, current_renter_id=user.id)
            db.session.add(shoe)
            db.session.commit()
            
            assert shoe.current_renter is not None
            assert shoe.current_renter.username == 'testuser'
