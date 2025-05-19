
from datetime import datetime, date, time
from .extensions import db

class Utilisateur(db.Model):
    __tablename__ = 'utilisateur'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mot_de_passe = db.Column(db.String(128), nullable=False)
    telephone = db.Column(db.String(20))
    date_inscription = db.Column(db.DateTime, default=datetime.utcnow)

class Coiffeur(db.Model):
    __tablename__ = 'coiffeur'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    specialite = db.Column(db.String(100))
    email = db.Column(db.String(120))
    telephone = db.Column(db.String(20))

class Service(db.Model):
    __tablename__ = 'service'
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    duree = db.Column(db.Integer)  # en minutes
    prix = db.Column(db.Float)

class Creneau(db.Model):
    __tablename__ = 'creneau'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    heure_debut = db.Column(db.Time, nullable=False)
    heure_fin = db.Column(db.Time, nullable=False)
    coiffeur_id = db.Column(db.Integer, db.ForeignKey('coiffeur.id'), nullable=False)
    coiffeur = db.relationship('Coiffeur', backref=db.backref('creneaux', lazy=True))

class Reservation(db.Model):
    __tablename__ = 'reservation'
    id = db.Column(db.Integer, primary_key=True)
    date_reservation = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    utilisateur_id = db.Column(db.Integer, db.ForeignKey('utilisateur.id'), nullable=False)
    utilisateur = db.relationship('Utilisateur', backref=db.backref('reservations', lazy=True))
    coiffeur_id = db.Column(db.Integer, db.ForeignKey('coiffeur.id'), nullable=False)
    coiffeur = db.relationship('Coiffeur', backref=db.backref('reservations', lazy=True))
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    service = db.relationship('Service', backref=db.backref('reservations', lazy=True))
    creneau_id = db.Column(db.Integer, db.ForeignKey('creneau.id'), nullable=False)
    creneau = db.relationship('Creneau', backref=db.backref('reservations', lazy=True))
    statut = db.Column(db.String(20))
