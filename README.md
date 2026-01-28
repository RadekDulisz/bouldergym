# Boulder Gym - Climbing Gym Management System

A full-stack web application for managing a climbing gym, including member registration, pass management, session booking, shoe rentals, and payment processing.

## Features

### Client Features
- **User Registration & Authentication**: Secure account creation and login
- **Pass Management**: Purchase and track climbing passes
  - Entry-based passes (10 or 20 entries)
  - Time-based passes (30 or 90 days)
- **Session Booking**: Reserve climbing sessions with real-time availability
- **Dashboard**: View active passes, remaining entries, and upcoming reservations
- **Shoe Rental**: Rent climbing shoes in various sizes
- **Entry Confirmation**: Check-in for booked sessions

### Receptionist Features
- **Dashboard**: Overview of daily reservations and statistics
- **Booking Search**: Find and manage customer reservations
- **Entry Confirmation**: Check-in customers and deduct pass entries
- **Pass Management**: Verify customer pass status and issue new passes
- **Shoe Management**: Track and manage shoe rentals and returns
- **Payment Processing**: Record payments and pass sales

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/RadekDulisz/bouldergym.git
cd bouldergym
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

**For development with debug mode:**
```bash
FLASK_DEBUG=true python app.py
```

**Note**: Debug mode is disabled by default for security. Only enable it in development environments.

4. Open your browser and navigate to:
```
http://localhost:5000
```

## Default Accounts

### Receptionist Account
- **Username**: receptionist
- **Password**: admin123
- **Role**: Receptionist

You can create client accounts through the registration page.

## Database Schema

### User
- `id`: Primary key
- `username`: Unique username (required)
- `email`: Unique email address (required)
- `password_hash`: Hashed password
- `role`: Either 'client' or 'receptionist'
- `created_at`: Account creation timestamp

### Pass
- `id`: Primary key
- `user_id`: Foreign key to User
- `pass_type`: Type of pass (10-Entry, 20-Entry, 30-Day, 90-Day)
- `entries_total`: Total entries for pass
- `entries_remaining`: Remaining entries
- `expiry_date`: Pass expiration date (for time-based passes)
- `purchase_date`: Date of purchase
- `price`: Purchase price
- `is_active`: Active status

### Reservation
- `id`: Primary key
- `user_id`: Foreign key to User
- `reservation_date`: Date of reservation
- `time_slot`: Time slot (e.g., '09:00-11:00')
- `status`: 'pending' or 'confirmed'
- `created_at`: Creation timestamp
- `confirmed_by`: Receptionist ID who confirmed

### Shoes
- `id`: Primary key
- `size`: Shoe size (e.g., 9, 9.5, 10)
- `is_available`: Availability status
- `condition`: Shoe condition ('good', 'fair', 'poor')
- `current_renter_id`: Current renter (if any)
- `rental_date`: Date of current rental

### Payment
- `id`: Primary key
- `user_id`: Foreign key to User
- `amount`: Payment amount
- `payment_type`: Type of payment
- `description`: Payment description
- `payment_date`: Date of payment
- `status`: Payment status ('completed', 'pending')
- `pass_id`: Associated pass (if applicable)

## Pass Types

### Entry-Based Passes
- **10-Entry Pass**: $100.00 - Valid for 10 climbing sessions
- **20-Entry Pass**: $180.00 - Valid for 20 climbing sessions

### Time-Based Passes
- **30-Day Pass**: $150.00 - Unlimited climbing for 30 days
- **90-Day Pass**: $400.00 - Unlimited climbing for 90 days

## Available Time Slots

Daily climbing sessions from 09:00 to 21:00 (6 slots total):
- **09:00-11:00** (Morning)
- **11:00-13:00** (Late Morning)
- **13:00-15:00** (Afternoon)
- **15:00-17:00** (Late Afternoon)
- **17:00-19:00** (Evening)
- **19:00-21:00** (Night)

**Slot Details:**
- Duration: 2 hours per session
- Maximum capacity: 20 climbers per slot
- Cancellation: Up to 24 hours before start time

## Project Structure

```
bouldergym/
├── app.py                      # Main Flask application and routes
├── models.py                   # SQLAlchemy database models
├── config.py                   # Configuration settings
├── run_tests.py               # Test runner
├── requirements.txt           # Python dependencies
├── requirements-test.txt      # Testing dependencies
├── requirements-acceptance.txt # Acceptance testing dependencies
├── pytest.ini                 # Pytest configuration
├── behave.ini                 # Behave (BDD) configuration
│
├── templates/                 # Jinja2 HTML templates
│   ├── base.html             # Base template with navigation
│   ├── index.html            # Home page
│   ├── login.html            # Login page
│   ├── register.html         # Registration page
│   ├── client_dashboard.html # Client main dashboard
│   ├── view_slots.html       # Session booking interface
│   ├── buy_pass.html         # Pass purchase page
│   ├── check_pass.html       # Pass verification
│   ├── receptionist_dashboard.html # Receptionist main dashboard
│   ├── search_bookings.html  # Booking search interface
│   ├── sell_pass.html        # Receptionist pass selling
│   └── manage_shoes.html     # Shoe rental management
│
├── features/                 # BDD test scenarios
│   ├── environment.py        # Behave environment setup
│   ├── login.feature         # Login feature tests
│   ├── registration.feature  # Registration feature tests
│   ├── pass_purchase.feature # Pass purchase feature tests
│   ├── reservation.feature   # Reservation feature tests
│   ├── shoes_rental.feature  # Shoe rental feature tests
│   ├── receptionist.feature  # Receptionist features
│   └── steps/                # Step definitions for BDD tests
│       ├── common_steps.py
│       ├── user_steps.py
│       ├── pass_steps.py
│       ├── reservation_steps.py
│       ├── receptionist_steps.py
│       └── shoes_steps.py
│
├── test_models.py            # Unit tests for models
├── test_routes.py            # Unit tests for routes
├── bouldergym.db             # SQLite database (created on first run)
└── instance/                 # Instance folder for local config
```

## Usage Guide

### As a Client

1. **Register**: Navigate to the registration page and create a new account
2. **Buy a Pass**: After login, go to "Buy Pass" and select your desired pass type
3. **View Slots**: Browse available climbing sessions by date and time
4. **Book Session**: Click on an available slot to reserve (requires valid pass)
5. **Dashboard**: View your active passes, remaining entries, and upcoming reservations
6. **Rent Shoes**: Rent climbing shoes through the dashboard
7. **Check-in**: Receptionists will confirm your entry when you arrive

### As a Receptionist

1. **Login**: Use receptionist credentials (username: receptionist, password: admin123)
2. **Dashboard**: View today's scheduled reservations and gym statistics
3. **Search Bookings**: Use the search interface to find specific customer reservations
4. **Confirm Entry**: Check-in customers, deduct pass entries, and update reservation status
5. **Check Pass**: Verify customer pass validity and remaining entries
6. **Sell Pass**: Issue new passes to customers and process payments
7. **Manage Shoes**: Track shoe rentals, record returns, and update inventory

## Testing

### Unit Tests
```bash
pytest test_models.py
pytest test_routes.py
```

### Acceptance Tests (BDD)
```bash
behave
```

### Run All Tests
```bash
python run_tests.py
```

## Security Features

- **Password Security**: Passwords hashed using Werkzeug's `generate_password_hash`
- **Session Management**: Secure session handling with Flask-Login
- **Role-Based Access Control**: Decorator-based authorization checks
- **CSRF Protection**: Built-in Flask CSRF protection
- **SQL Injection Prevention**: SQLAlchemy ORM protects against SQL injection
- **Input Validation**: All user inputs validated before processing

## Technology Stack

- **Backend**: Flask (Python web framework)
- **Database**: SQLite with SQLAlchemy ORM
- **Frontend**: HTML5, Tailwind CSS, JavaScript
- **Authentication**: Flask-Login
- **Testing**: pytest, Behave (BDD)

## Development

To run in development mode:
```bash
python app.py
```

The application will automatically create the database and initialize with default data on first run.

### Environment Variables

Key settings can be configured in `config.py`:
- `SQLALCHEMY_DATABASE_URI`: Database connection string
- `SECRET_KEY`: Flask secret key for sessions
- `DEBUG`: Debug mode flag

## License

This project is open source and available for educational purposes.