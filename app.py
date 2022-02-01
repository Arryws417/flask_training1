from crypt import methods
from datetime import timedelta
from http.client import FOUND
import uuid
from flask import Flask, render_template,redirect,url_for, request,session, flash, jsonify;
from Notesmodel import Notes, db
from list import first



#membuat flask app
app.register_blueprint(first, url_prefix="/temp")
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://users.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=6)

db.app = app
db.init_app(app)

db.create_all()

@app.route('/home')
@app.route("/", methods=['GET'])
def home():
    """
    GET ALL DATA
    """
    semua = Notes.query.all()
    return render_template('index.html')

@app.route('/', methods=['POST'])
def create():
    nama = request.form["name"]
    note = Notes(nama, False)
    db.session.add(note)
    db.session.commit()
    return jsonify({
        "nama " : nama,
        "selesai" : False
    })
@app.route('/update/<user_id>',methods=['PUT'])
def change(user_id):
    uuid == user_id
    found_user = Notes.query.filter_by(id=uuid).first()
    if found_user:
        change = not found_user.done
        found_user.done = change
        db.session.commit()
        if change == True:
            act = "Selesai"
        else:
            act = "Belum Selesai"
        return found_user.nama+' adalah '+act
    else:
        return 'User tidak ditemukan'
@app.route('/delete/<user_id>', methods=['DELETE'])
def hapus(user_id):
    uuid = user_id
    Notes.query.filter_by(id=uuid).delete()
    db.session.commit()
    return 'sukses'

#nama endpoint boleh berbeda dengan nama function
#misal @app.route('/delete')
#function nya def hapus():

if __name__ == "__main__":
    app.run(debug=True)
