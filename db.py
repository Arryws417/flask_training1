import imp
from pkgutil import iter_modules
from typing import ItemsView
from unicodedata import name
import uuid
from datetime import datetime

items = []

def semua_items():
    return items

def tambah_items():
    items = {
        'id': str(uuid.uuid4()),
        'name': name,
        'status': False,
        'created': datetime.now()
    }
    items.append(items)

def update_item(id):
