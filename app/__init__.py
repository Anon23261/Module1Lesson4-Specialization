from flask import Flask, jsonify
from app.config import Config
from app.extensions import db, migrate
from app.utils.error_handlers import register_error_handlers

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    
    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register error handlers
    register_error_handlers(app)
    
    # Register blueprints
    from app.routes.mechanic import bp as mechanic_bp
    from app.routes.service import bp as service_bp
    
    app.register_blueprint(mechanic_bp)
    app.register_blueprint(service_bp)
    
    @app.route('/api/v1/health')
    def health_check():
        return jsonify({
            'status': 'healthy',
            'version': '1.0.0',
            'database': 'connected' if db.engine.pool.checkedout() == 0 else 'busy'
        })
        
    return app
