from flask import jsonify
from werkzeug.exceptions import HTTPException

def register_error_handlers(app):
    @app.errorhandler(HTTPException)
    def handle_http_error(error):
        response = {
            'error': {
                'code': error.code,
                'name': error.name,
                'description': error.description,
            }
        }
        return jsonify(response), error.code

    @app.errorhandler(422)
    def handle_validation_error(error):
        response = {
            'error': {
                'code': 422,
                'name': 'Unprocessable Entity',
                'description': 'The request data failed validation.',
                'errors': error.description
            }
        }
        return jsonify(response), 422

    @app.errorhandler(Exception)
    def handle_generic_error(error):
        response = {
            'error': {
                'code': 500,
                'name': 'Internal Server Error',
                'description': 'An unexpected error occurred.'
            }
        }
        return jsonify(response), 500
