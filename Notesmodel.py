from argparse import Namespace
import uuid
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

item = []
db = SQLAlchemy()

class note(db.Notesmodel):
    id = db.Colum('id', db.string(200), primary_key = True)
    nama = db.Column(db.string(200))
    made = db.Column(db.datetime)

    def __init__(self, nama, done):
        self.id = str(uuid.uuid4())
        self.nama = nama
        self.done = done
        self.made = datetime.now()
    
    def serialize(self):
        return {"id": self.id,
                "Nama": self.nama,
                "done": self.done}
                