from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from extensions import db, migrate
from models import Korisnik, Vozilo, Lokacija, Najam
from flask_migrate import Migrate
from flask import Flask, jsonify
from flask_cors import CORS


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/nikolaprojekt"

db.init_app(app)
migrate.init_app(app, db)
CORS(app)

#KORISNIK
@app.route("/korisnici", methods=["POST"])
def add_korisnik():
    data = request.get_json()

    korisnik = Korisnik(
        ime=data.get('ime'),
        prezime=data.get('prezime'),
        email=data.get('email'),
        broj_mobitela=data.get('broj_mobitela'),
        broj_vozacke=data.get('broj_vozacke')
    )

    db.session.add(korisnik)
    db.session.commit()

    return jsonify(korisnik.to_dict())

@app.route("/korisnici", methods=["GET"])
def get_korisnici():
    korisnici = Korisnik.query.all()
    return jsonify([k.to_dict() for k in korisnici])

@app.route("/korisnici/<int:id>", methods=["PUT"])
def update_korisnik(id):
    korisnik = Korisnik.query.filter_by(id=id).first()
    data = request.json

    korisnik.ime = data["ime"]
    korisnik.prezime = data["prezime"]
    korisnik.email = data["email"]
    korisnik.broj_mobitela = data["broj_mobitela"]
    korisnik.broj_vozacke = data["broj_vozacke"]

    db.session.commit()

    return jsonify(korisnik.to_dict())

@app.route("/korisnici/<int:id>", methods=["DELETE"])
def delete_korisnik(id):
    korisnik = Korisnik.query.filter_by(id=id).first()
    db.session.delete(korisnik)
    db.session.commit()

    return jsonify({"message": "Obrisan korisnik"})


#VOZILO
@app.route("/vozila", methods=["POST"])
def add_vozilo():
    data = request.get_json()

    vozilo = Vozilo(
        marka=data.get('marka'),
        model=data.get('model'),
        godina_proizvodnje=data.get('godina_proizvodnje'),
        snaga_kw=data.get('snaga_kw'),
        registracija=data.get('registracija'),
        cijena_po_danu=data.get('cijena_po_danu'),
        dostupno=data.get('dostupno')
    )

    db.session.add(vozilo)
    db.session.commit()

    return jsonify(vozilo.to_dict())

@app.route("/vozila", methods=["GET"])
def get_vozila():
    vozila = Vozilo.query.all()
    return jsonify([v.to_dict() for v in vozila])

@app.route("/vozila/<int:id>", methods=["PUT"])
def update_vozilo(id):
    vozilo = Vozilo.query.filter_by(id=id).first()
    data = request.json

    vozilo.marka = data["marka"]
    vozilo.model = data["model"]
    vozilo.godina_proizvodnje = data["godina_proizvodnje"]
    vozilo.snaga_kw = data["snaga_kw"]
    vozilo.registracija = data["registracija"]
    vozilo.cijena_po_danu = data["cijena_po_danu"]
    vozilo.dostupno = data["dostupno"]

    db.session.commit()

    return jsonify(vozilo.to_dict())

@app.route("/vozila/<int:id>", methods=["DELETE"])
def delete_vozilo(id):
    vozilo = Vozilo.query.filter_by(id=id).first()
    db.session.delete(vozilo)
    db.session.commit()

    return jsonify({"message": "Obrisano vozilo"})


#LOKACIJA
@app.route("/lokacije", methods=["POST"])
def add_lokacija():
    data = request.get_json()

    lokacija = Lokacija(
        naziv_lokacije=data.get('naziv_lokacije'),
        adresa=data.get('adresa'),
        grad=data.get('grad')
    )

    db.session.add(lokacija)
    db.session.commit()

    return jsonify(lokacija.to_dict())

@app.route("/lokacije", methods=["GET"])
def get_lokacije():
    lokacije = Lokacija.query.all()
    return jsonify([l.to_dict() for l in lokacije])

@app.route("/lokacije/<int:id>", methods=["PUT"])
def update_lokacija(id):
    lokacija = Lokacija.query.filter_by(id=id).first()
    data = request.json

    lokacija.naziv_lokacije = data["naziv_lokacije"]
    lokacija.adresa = data["adresa"]
    lokacija.grad = data["grad"]

    db.session.commit()

    return jsonify(lokacija.to_dict())

@app.route("/lokacije/<int:id>", methods=["DELETE"])
def delete_lokacija(id):
    lokacija = Lokacija.query.filter_by(id=id).first()
    db.session.delete(lokacija)
    db.session.commit()

    return jsonify({"message": "Obrisana lokacija"})
#NAJAM
@app.route("/najmovi", methods=["POST"])
def add_najam():
    data = request.get_json()

    najam = Najam(
        korisnik_id=data.get('korisnik_id'),
        vozilo_id=data.get('vozilo_id'),
        lokacija_id=data.get('lokacija_id'),
        datum_preuzimanja=data.get('datum_preuzimanja'),
        datum_povrata=data.get('datum_povrata'),
        ukupna_cijena=data.get('ukupna_cijena')
    )

    db.session.add(najam)
    db.session.commit()

    return jsonify(najam.to_dict())

@app.route("/najmovi", methods=["GET"])
def get_najmovi():
    najmovi = Najam.query.all()
    return jsonify([n.to_dict() for n in najmovi])

@app.route("/najmovi/<int:id>", methods=["PUT"])
def update_najam(id):
    najam = Najam.query.filter_by(id=id).first()
    data = request.json


    najam.korisnik_id = data["korisnik_id"]
    najam.vozilo_id = data["vozilo_id"]
    najam.lokacija_id = data["lokacija_id"]

    db.session.commit()

    return jsonify(najam.to_dict())

@app.route("/najmovi/<int:id>", methods=["DELETE"])
def delete_najam(id):
    najam = Najam.query.filter_by(id=id).first()
    db.session.delete(najam)
    db.session.commit()

    return jsonify({"message": "Obrisan najam"})


if __name__ == "__main__":
    app.run(debug=True, port=5000)