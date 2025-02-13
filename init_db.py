import os
from app import create_app
from app.extensions import db

app = create_app()

with app.app_context():
    # Drop all tables
    db.drop_all()
    print("Dropped all existing tables")
    
    # Create all tables
    db.create_all()
    print("Created new tables with updated schema")
    
    # Verify the schema
    from app.models.mechanic import Mechanic
    from app.models.service import Service
    
    inspector = db.inspect(db.engine)
    
    print("\nMechanic table columns:")
    for column in inspector.get_columns('mechanic'):
        print(f"- {column['name']}: {column['type']}")
        
    print("\nService table columns:")
    for column in inspector.get_columns('service'):
        print(f"- {column['name']}: {column['type']}")

