from werkzeug.exceptions import UnprocessableEntity
import re

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        raise UnprocessableEntity({'email': 'Invalid email format'})

def validate_mechanic(data):
    errors = {}
    required_fields = ['name', 'email']
    
    for field in required_fields:
        if field not in data or not data[field]:
            errors[field] = f'{field} is required'
    
    if 'email' in data and data['email']:
        validate_email(data['email'])
        
    if 'years_experience' in data:
        try:
            years = int(data['years_experience'])
            if years < 0:
                errors['years_experience'] = 'Years of experience cannot be negative'
        except (ValueError, TypeError):
            errors['years_experience'] = 'Years of experience must be a valid number'
            
    if errors:
        raise UnprocessableEntity(errors)

def validate_service(data):
    errors = {}
    required_fields = ['name', 'price', 'mechanic_id']
    
    for field in required_fields:
        if field not in data or not data[field]:
            errors[field] = f'{field} is required'
    
    if 'price' in data:
        try:
            price = float(data['price'])
            if price <= 0:
                errors['price'] = 'Price must be greater than 0'
        except (ValueError, TypeError):
            errors['price'] = 'Price must be a valid number'
            
    if 'duration_hours' in data and data['duration_hours']:
        try:
            duration = float(data['duration_hours'])
            if duration <= 0:
                errors['duration_hours'] = 'Duration must be greater than 0'
        except (ValueError, TypeError):
            errors['duration_hours'] = 'Duration must be a valid number'
            
    if errors:
        raise UnprocessableEntity(errors)
