from flask import Flask
from .config import Config
from .extensions import db, api, cors
from . import routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    cors.init_app(app, resources={r"/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)
    api.init_app(app)

    api.add_namespace(routes.ns_utilisateur)
    api.add_namespace(routes.ns_coiffeur)
    api.add_namespace(routes.ns_service)
    api.add_namespace(routes.ns_creneau)
    api.add_namespace(routes.ns_reservation)


    # Création des tables au démarrage de l'app
    with app.app_context():
        db.create_all()

    return app
