from flask_restx import fields
from .extensions import api

utilisateur_model = api.model('Utilisateur', {
    'id': fields.Integer(readOnly=True),
    'nom': fields.String(required=True),
    'prenom': fields.String(required=True),
    'email': fields.String(required=True),
    'mot_de_passe': fields.String(required=True),
    'telephone': fields.String,
    'date_inscription': fields.DateTime
})

coiffeur_model = api.model('Coiffeur', {
    'id': fields.Integer(readOnly=True),
    'nom': fields.String(required=True),
    'prenom': fields.String(required=True),
    'specialite': fields.String,
    'email': fields.String,
    'telephone': fields.String
})

service_model = api.model('Service', {
    'id': fields.Integer(readOnly=True),
    'nom': fields.String(required=True),
    'description': fields.String,
    'duree': fields.Integer,
    'prix': fields.Float
})

creneau_model = api.model('Creneau', {
'id': fields.Integer(readOnly=True),
'date': fields.String(required=True),  # Stocké en string isoformat YYYY-MM-DD
'heure_debut': fields.String(required=True),  # HH:MM:SS
'heure_fin': fields.String(required=True),  # HH:MM:SS
'coiffeur_id': fields.Integer(required=True)
})
reservation_model = api.model('Reservation', {
'id': fields.Integer(readOnly=True),
'date_reservation': fields.String(required=True), # Date et heure ISO8601
'utilisateur_id': fields.Integer(required=True),
'coiffeur_id': fields.Integer(required=True),
'service_id': fields.Integer(required=True),
'creneau_id': fields.Integer(required=True),
'statut': fields.String
})