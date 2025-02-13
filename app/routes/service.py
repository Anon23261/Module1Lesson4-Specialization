from flask import Blueprint, jsonify, request
from app.extensions import db
from app.models.service import Service
from app.models.mechanic import Mechanic
from app.utils.validators import validate_service

bp = Blueprint('service', __name__, url_prefix='/api/v1')

@bp.route('/services', methods=['GET'])
def get_services():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    mechanic_id = request.args.get('mechanic_id', type=int)
    
    query = Service.query
    if mechanic_id:
        query = query.filter(Service.mechanic_id == mechanic_id)
        
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    services = pagination.items
    
    return jsonify({
        'services': [s.to_dict() for s in services],
        'meta': {
            'page': page,
            'per_page': per_page,
            'total_pages': pagination.pages,
            'total_items': pagination.total
        }
    })

@bp.route('/services/<int:id>', methods=['GET'])
def get_service(id):
    service = Service.query.get_or_404(id)
    return jsonify(service.to_dict())

@bp.route('/services', methods=['POST'])
def create_service():
    data = request.get_json()
    validate_service(data)
    
    # Verify mechanic exists
    mechanic = Mechanic.query.get_or_404(data['mechanic_id'])
    
    new_service = Service(
        name=data['name'],
        description=data.get('description'),
        price=data['price'],
        duration_hours=data.get('duration_hours'),
        mechanic_id=data['mechanic_id']
    )
    
    db.session.add(new_service)
    db.session.commit()
    
    return jsonify(new_service.to_dict()), 201

@bp.route('/services/<int:id>', methods=['PUT'])
def update_service(id):
    service = Service.query.get_or_404(id)
    data = request.get_json()
    validate_service(data)
    
    if 'mechanic_id' in data and data['mechanic_id'] != service.mechanic_id:
        # Verify new mechanic exists if changing mechanic
        Mechanic.query.get_or_404(data['mechanic_id'])
    
    service.name = data['name']
    service.description = data.get('description', service.description)
    service.price = data['price']
    service.duration_hours = data.get('duration_hours', service.duration_hours)
    service.mechanic_id = data.get('mechanic_id', service.mechanic_id)
    
    db.session.commit()
    return jsonify(service.to_dict())

@bp.route('/services/<int:id>', methods=['DELETE'])
def delete_service(id):
    service = Service.query.get_or_404(id)
    db.session.delete(service)
    db.session.commit()
    return '', 204

@bp.route('/services/search', methods=['GET'])
def search_services():
    name = request.args.get('name')
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)
    
    query = Service.query
    
    if name:
        query = query.filter(Service.name.ilike(f'%{name}%'))
    if min_price is not None:
        query = query.filter(Service.price >= min_price)
    if max_price is not None:
        query = query.filter(Service.price <= max_price)
        
    services = query.all()
    return jsonify([s.to_dict() for s in services])
