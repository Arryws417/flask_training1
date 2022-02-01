from crypt import methods
from unicodedata import name
from flask import Blueprint, render_template, redirect, url_for, render_template, request, session, flash

from db import new_item, all_item, update_item, delete_item

first = Blueprint("first", __name__)
@first.route("/home")
@first.route('/')
def home():
    return render_template('index.html', todo=all_item())

@first.route('/new',methods=['POST'])
def new():
    name = request.form.get('name')
    return new_item(name)


@first.route('/update',methods=['POST'])
def update():
    kode = request.form.get('id')
    update_item(id)
    return 'Sukses update!!'

@first.route('/delete', methods=['POST'])
def hapus():
    id = request.form.get('id')
    delete_item(id)
    return 'Sudah di Hapus!'