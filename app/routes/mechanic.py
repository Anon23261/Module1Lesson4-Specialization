from flask import Blueprint, jsonify, request, abort
from app.extensions import db
from app.models.mechanic import Mechanic
from app.utils.validators import validate_mechanic

bp = Blueprint('mechanic', __name__, url_prefix='/api/v1')

@bp.route('/mechanics', methods=['GET'])
def get_mechanics():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    specialty = request.args.get('specialty')
    
    query = Mechanic.query
    if specialty:
        query = query.filter(Mechanic.specialty == specialty)
        
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    mechanics = pagination.items
    
    return jsonify({
        'mechanics': [m.to_dict() for m in mechanics],
        'meta': {
            'page': page,
            'per_page': per_page,
            'total_pages': pagination.pages,
            'total_items': pagination.total
        }
    })

@bp.route('/mechanics/<int:id>', methods=['GET'])
def get_mechanic(id):
    mechanic = Mechanic.query.get_or_404(id)
    return jsonify(mechanic.to_dict())

@bp.route('/mechanics', methods=['POST'])
def create_mechanic():
    try:
        print('Received request to create mechanic')
        data = request.get_json()
        print(f'Request data: {data}')
        
        validate_mechanic(data)
        print('Data validation passed')
        
        new_mechanic = Mechanic(
            name=data['name'],
            email=data['email'],
            specialty=data.get('specialty'),
            certification=data.get('certification'),
            years_experience=data.get('years_experience')
        )
        print('Created mechanic object')
        
        db.session.add(new_mechanic)
        print('Added to session')
        db.session.commit()
        print('Committed to database')
        
        result = new_mechanic.to_dict()
        print(f'Returning result: {result}')
        return jsonify(result), 201
    except Exception as e:
        print(f'Error creating mechanic: {str(e)}')
        db.session.rollback()
        raise

@bp.route('/mechanics/<int:id>', methods=['PUT'])
def update_mechanic(id):
    mechanic = Mechanic.query.get_or_404(id)
    data = request.get_json()
    validate_mechanic(data)
    
    mechanic.name = data['name']
    mechanic.email = data['email']
    mechanic.specialty = data.get('specialty', mechanic.specialty)
    mechanic.certification = data.get('certification', mechanic.certification)
    mechanic.years_experience = data.get('years_experience', mechanic.years_experience)
    
    db.session.commit()
    return jsonify(mechanic.to_dict())

@bp.route('/mechanics/<int:id>', methods=['DELETE'])
def delete_mechanic(id):
    mechanic = Mechanic.query.get_or_404(id)
    db.session.delete(mechanic)
    db.session.commit()
    return '', 204

@bp.route('/mechanics/search', methods=['GET'])
def search_mechanics():
    name = request.args.get('name')
    min_experience = request.args.get('min_experience', type=int)
    certification = request.args.get('certification')
    
    query = Mechanic.query
    
    if name:
        query = query.filter(Mechanic.name.ilike(f'%{name}%'))
    if min_experience is not None:
        query = query.filter(Mechanic.years_experience >= min_experience)
    if certification:
        query = query.filter(Mechanic.certification == certification)
        
    mechanics = query.all()
    return jsonify([m.to_dict() for m in mechanics])
