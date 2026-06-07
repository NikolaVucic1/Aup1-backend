from sqlalchemy.orm import backref
from extensions import db

class Korisnik(db.Model):
    __tablename__ = "korisnici"

    id = db.Column(db.Integer, primary_key=True)
    ime = db.Column(db.String(30), nullable=False)
    prezime = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    broj_mobitela = db.Column(db.String(30), nullable=False)
    broj_vozacke = db.Column(db.String(30), nullable=False, unique=True)

    najmovi = db.relationship("Najam", backref="korisnik", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "ime": self.ime,
            "prezime": self.prezime,
            "email": self.email,
            "broj_mobitela": self.broj_mobitela,
            "broj_vozacke": self.broj_vozacke
        }


class Vozilo(db.Model):
    __tablename__ = "vozila"

    id = db.Column(db.Integer, primary_key=True)
    marka = db.Column(db.String(30), nullable=False)
    model = db.Column(db.String(30), nullable=False)
    godina_proizvodnje = db.Column(db.Integer, nullable=False)
    snaga_kw = db.Column(db.Integer, nullable=False)
    registracija = db.Column(db.String(20), nullable=False)
    cijena_po_danu = db.Column(db.Float, nullable=False)
    dostupno = db.Column(db.Boolean, default=True, nullable=False)

    najmovi = db.relationship("Najam", backref="vozilo", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "marka": self.marka,
            "model": self.model,
            "godina_proizvodnje": self.godina_proizvodnje,
            "snaga_kw": self.snaga_kw,
            "registracija": self.registracija,
            "cijena_po_danu": self.cijena_po_danu,
            "dostupno": self.dostupno,

        }


class Lokacija(db.Model):
    __tablename__ = "lokacije"

    id = db.Column(db.Integer, primary_key=True)
    naziv_lokacije = db.Column(db.String(80), nullable=False)
    adresa = db.Column(db.String(100), nullable=False)
    grad = db.Column(db.String(50), nullable=False)


    najmovi = db.relationship("Najam", backref="lokacija", lazy=True)

    def to_dict(self):
        return {
            "id": self.id,
            "naziv_lokacije": self.naziv_lokacije,
            "adresa": self.adresa,
            "grad": self.grad
        }

class Najam(db.Model):
    __tablename__ = "najmovi"

    id = db.Column(db.Integer, primary_key=True)
    datum_preuzimanja = db.Column(db.Date, nullable=False)
    datum_povrata = db.Column(db.Date, nullable=False)
    ukupna_cijena = db.Column(db.Float, nullable=False)


    korisnik_id = db.Column(db.Integer, db.ForeignKey("korisnici.id"), nullable=True)
    vozilo_id = db.Column(db.Integer, db.ForeignKey("vozila.id"), nullable=True)
    lokacija_id = db.Column(db.Integer, db.ForeignKey("lokacije.id"), nullable=True)

    def to_dict(self):
        return {
            "id": self.id,
            "datum_preuzimanja": self.datum_preuzimanja,
            "datum_povrata": self.datum_povrata,
            "ukupna_cijena": self.ukupna_cijena,
            "korisnik_id": self.korisnik_id,
            "vozilo_id": self.vozilo_id,
            "lokacija_id": self.lokacija_id,

            "korisnik_ime_prezime": (self.korisnik.ime + " " + self.korisnik.prezime) if self.korisnik else "",
            "vozilo_info": (self.vozilo.marka + " " + self.vozilo.model) if self.vozilo else "",
            "lokacija_naziv": self.lokacija.naziv_lokacije if self.lokacija else ""
        }


