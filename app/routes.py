from flask import request
from flask_restx import Resource, Namespace
from .extensions import api, db
from .models import Utilisateur, Coiffeur, Service, Creneau, Reservation
from .schemas import utilisateur_model, coiffeur_model, service_model, creneau_model, reservation_model

# Définition des namespaces
ns_utilisateur = Namespace('utilisateurs', description='Gestion des utilisateurs')
ns_coiffeur = Namespace('coiffeurs', description='Gestion des coiffeurs')
ns_service = Namespace('services', description='Gestion des services')
ns_creneau = Namespace('creneaux', description='Gestion des créneaux')
ns_reservation = Namespace('reservations', description='Gestion des réservations')

# UTILISATEURS

@ns_utilisateur.route('/')
class UtilisateurList(Resource):
    @ns_utilisateur.marshal_list_with(utilisateur_model)
    def get(self):
        return Utilisateur.query.all()

    @ns_utilisateur.expect(utilisateur_model)
    @ns_utilisateur.marshal_with(utilisateur_model, code=201)
    def post(self):
        data = request.json
        data.pop('id', None)
        try:
            utilisateur = Utilisateur(**data)
            db.session.add(utilisateur)
            db.session.commit()
            return utilisateur, 201
        except Exception as e:
            db.session.rollback()
            ns_utilisateur.abort(400, f"Erreur lors de la création de l'utilisateur: {str(e)}")

@ns_utilisateur.route('/<int:id>')
class UtilisateurDetail(Resource):
    @ns_utilisateur.marshal_with(utilisateur_model)
    def get(self, id):
        return Utilisateur.query.get_or_404(id)

    def delete(self, id):
        utilisateur = Utilisateur.query.get_or_404(id)
        db.session.delete(utilisateur)
        db.session.commit()
        return '', 204

    @ns_utilisateur.expect(utilisateur_model)
    @ns_utilisateur.marshal_with(utilisateur_model)
    def put(self, id):
        utilisateur = Utilisateur.query.get_or_404(id)
        data = request.json
        for key, value in data.items():
            setattr(utilisateur, key, value)
        db.session.commit()
        return utilisateur
    
@ns_utilisateur.route('/login')
class UtilisateurLogin(Resource):
    def post(self):
        data = request.json
        email = data.get('email')
        password = data.get('password')

        utilisateur = Utilisateur.query.filter_by(email=email, mot_de_passe=password).first()

        if utilisateur:
            return {"message": "Connexion réussie", "id": utilisateur.id, "nom": utilisateur.nom}, 200
        else:
            return {"message": "Identifiants invalides"}, 401


# COIFFEURS

@ns_coiffeur.route('/')
class CoiffeurList(Resource):
    @ns_coiffeur.marshal_list_with(coiffeur_model)
    def get(self):
        return Coiffeur.query.all()

    @ns_coiffeur.expect(coiffeur_model)
    @ns_coiffeur.marshal_with(coiffeur_model, code=201)
    def post(self):
        data = request.json
        data.pop('id', None)
        try:
            coiffeur = Coiffeur(**data)
            db.session.add(coiffeur)
            db.session.commit()
            return coiffeur, 201
        except Exception as e:
            db.session.rollback()
            ns_coiffeur.abort(400, f"Erreur lors de la création du coiffeur: {str(e)}")

@ns_coiffeur.route('/<int:id>')
class CoiffeurDetail(Resource):
    @ns_coiffeur.marshal_with(coiffeur_model)
    def get(self, id):
        return Coiffeur.query.get_or_404(id)

    def delete(self, id):
        coiffeur = Coiffeur.query.get_or_404(id)
        db.session.delete(coiffeur)
        db.session.commit()
        return '', 204

    @ns_coiffeur.expect(coiffeur_model)
    @ns_coiffeur.marshal_with(coiffeur_model)
    def put(self, id):
        coiffeur = Coiffeur.query.get_or_404(id)
        data = request.json
        for key, value in data.items():
            setattr(coiffeur, key, value)
        db.session.commit()
        return coiffeur

# SERVICES

@ns_service.route('/')
class ServiceList(Resource):
    @ns_service.marshal_list_with(service_model)
    def get(self):
        return Service.query.all()

    @ns_service.expect(service_model)
    @ns_service.marshal_with(service_model, code=201)
    def post(self):
        data = request.json
        data.pop('id', None)
        try:
            service = Service(**data)
            db.session.add(service)
            db.session.commit()
            return service, 201
        except Exception as e:
            db.session.rollback()
            ns_service.abort(400, f"Erreur lors de la création du service: {str(e)}")

@ns_service.route('/<int:id>')
class ServiceDetail(Resource):
    @ns_service.marshal_with(service_model)
    def get(self, id):
        return Service.query.get_or_404(id)

    def delete(self, id):
        service = Service.query.get_or_404(id)
        db.session.delete(service)
        db.session.commit()
        return '', 204

    @ns_service.expect(service_model)
    @ns_service.marshal_with(service_model)
    def put(self, id):
        service = Service.query.get_or_404(id)
        data = request.json
        for key, value in data.items():
            setattr(service, key, value)
        db.session.commit()
        return service

# CRENEAUX

@ns_creneau.route('/')
class CreneauList(Resource):
    @ns_creneau.marshal_list_with(creneau_model)
    def get(self):
        return Creneau.query.all()

    @ns_creneau.expect(creneau_model)
    @ns_creneau.marshal_with(creneau_model, code=201)
    def post(self):
        data = request.json
        data.pop('id', None)
        try:
            creneau = Creneau(**data)
            db.session.add(creneau)
            db.session.commit()
            return creneau, 201
        except Exception as e:
            db.session.rollback()
            ns_creneau.abort(400, f"Erreur lors de la création du créneau: {str(e)}")

@ns_creneau.route('/<int:id>')
class CreneauDetail(Resource):
    @ns_creneau.marshal_with(creneau_model)
    def get(self, id):
        return Creneau.query.get_or_404(id)

    def delete(self, id):
        creneau = Creneau.query.get_or_404(id)
        db.session.delete(creneau)
        db.session.commit()
        return '', 204

    @ns_creneau.expect(creneau_model)
    @ns_creneau.marshal_with(creneau_model)
    def put(self, id):
        creneau = Creneau.query.get_or_404(id)
        data = request.json
        for key, value in data.items():
            setattr(creneau, key, value)
        db.session.commit()
        return creneau

# RESERVATIONS

@ns_reservation.route('/')
class ReservationList(Resource):
    @ns_reservation.marshal_list_with(reservation_model)
    def get(self):
        return Reservation.query.all()

    @ns_reservation.expect(reservation_model)
    @ns_reservation.marshal_with(reservation_model, code=201)
    def post(self):
        data = request.json
        data.pop('id', None)
        try:
            reservation = Reservation(**data)
            db.session.add(reservation)
            db.session.commit()
            return reservation, 201
        except Exception as e:
            db.session.rollback()
            ns_reservation.abort(400, f"Erreur lors de la création de la réservation: {str(e)}")

@ns_reservation.route('/<int:id>')
class ReservationDetail(Resource):
    @ns_reservation.marshal_with(reservation_model)
    def get(self, id):
        return Reservation.query.get_or_404(id)

    def delete(self, id):
        reservation = Reservation.query.get_or_404(id)
        db.session.delete(reservation)
        db.session.commit()
        return '', 204

    @ns_reservation.expect(reservation_model)
    @ns_reservation.marshal_with(reservation_model)
    def put(self, id):
        reservation = Reservation.query.get_or_404(id)
        data = request.json
        for key, value in data.items():
            setattr(reservation, key, value)
        db.session.commit()
        return reservation

# Enregistrement des namespaces à l'API
api.add_namespace(ns_utilisateur)
api.add_namespace(ns_coiffeur)
api.add_namespace(ns_service)
api.add_namespace(ns_creneau)
api.add_namespace(ns_reservation)
