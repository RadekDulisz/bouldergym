# 🧗 Boulder Gym Reservation System

A comprehensive web-based climbing gym reservation system with role-based access control for clients and receptionists.

## Features

### For Clients
- **User Registration & Login**: Secure authentication system
- **View Available Slots**: Browse climbing slots for the next 7 days
- **Book Entry**: Reserve climbing sessions (requires valid pass)
- **Buy Pass**: Purchase entry-based or time-based passes
- **View Bookings**: Track all your reservations
- **View Pass Details**: Monitor pass validity and remaining entries

### For Receptionists
- **Search Bookings**: Find reservations by username, email, or date
- **Confirm Entry**: Validate and confirm client check-ins
- **Check Pass**: Verify pass validity and remaining entries
- **Deduct Pass**: Automatically deduct entries on confirmation
- **Sell Pass**: Issue passes to clients at the desk
- **Rent Shoes**: Manage shoe rentals with tracking
- **Return Shoes**: Process shoe returns

### System Features
- **Availability Checking**: Maximum 20 people per time slot
- **Pass Validation**: Ensures valid pass before booking
- **Multi-user Support**: Concurrent access for multiple users
- **Secure Authentication**: Password hashing with Werkzeug
- **SQLite Database**: Persistent data storage
- **Responsive UI**: Bootstrap-based interface
- **Role-based Access Control**: Client and Receptionist roles

## Technology Stack

- **Backend**: Python Flask 3.0.0
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-Login
- **Frontend**: HTML, CSS, Bootstrap 5.1.3
- **Security**: Werkzeug password hashing

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
- id, username, email, password_hash, role, created_at

### Pass
- id, user_id, pass_type, entries_total, entries_remaining, expiry_date, purchase_date, price, is_active

### Reservation
- id, user_id, reservation_date, time_slot, status, created_at, confirmed_by

### Shoes
- id, size, is_available, condition, current_renter_id, rental_date

### Payment
- id, user_id, amount, payment_type, description, payment_date, status, pass_id

## Pass Types

### Entry-Based Passes
- **10-Entry Pass**: $100.00 - 10 climbing sessions
- **20-Entry Pass**: $180.00 - 20 climbing sessions

### Time-Based Passes
- **30-Day Pass**: $150.00 - Unlimited climbing for 30 days
- **90-Day Pass**: $400.00 - Unlimited climbing for 90 days

## Available Time Slots

Daily slots from 09:00 to 21:00:
- 09:00-11:00
- 11:00-13:00
- 13:00-15:00
- 15:00-17:00
- 17:00-19:00
- 19:00-21:00

Maximum capacity: 20 people per slot

## Project Structure

```
bouldergym/
├── app.py                 # Main Flask application
├── models.py              # Database models
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
├── templates/             # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── client_dashboard.html
│   ├── view_slots.html
│   ├── buy_pass.html
│   ├── receptionist_dashboard.html
│   ├── search_bookings.html
│   ├── check_pass.html
│   ├── sell_pass.html
│   └── manage_shoes.html
└── bouldergym.db          # SQLite database (created on first run)
```

## Usage Guide

### As a Client

1. **Register**: Create a new account with username, email, and password
2. **Buy a Pass**: Purchase an entry-based or time-based pass
3. **View Slots**: Browse available time slots
4. **Book Entry**: Reserve a slot (requires valid pass)
5. **View Dashboard**: Check your passes and reservations

### As a Receptionist

1. **Login**: Use receptionist credentials
2. **Dashboard**: View today's reservations and statistics
3. **Search Bookings**: Find customer reservations
4. **Confirm Entry**: Check-in customers and deduct pass entries
5. **Check Pass**: Verify customer pass status
6. **Sell Pass**: Issue passes to customers
7. **Manage Shoes**: Rent and return climbing shoes

## Security Features

- Password hashing using Werkzeug's `generate_password_hash`
- Session management with Flask-Login
- Role-based access control (decorator-based)
- CSRF protection (Flask built-in)
- SQL injection prevention (SQLAlchemy ORM)

## Development

To run in development mode with debug enabled:
```bash
python app.py
```

The application will automatically create the database and initialize with sample data on first run.

## License

This project is open source and available for educational purposes.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

For issues or questions, please open an issue on the GitHub repository.