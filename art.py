# The art class. Talks to the database.

from Models import Art
from peewee import IntegrityError

def add_art(art):
    try:
        art.save()
    except IntegrityError:
        raise ArtError(f'{art.name} already in system')

def get_all_art():
    query = Art.select()
    return list(query)

def change_available(art_id):
    art = get_art_by_id(art_id)
    if art == None:
        raise ArtError
    if art.available == True:
        art.available = False
    else:
        art.available = True
    art.save()

def delete_art(art_id):
    rows_deleted = Art.delete().where(Art.id == art_id).execute()
    if rows_deleted == 0:
        raise ArtError('Error deleting art piece.')

def get_art_by_id(art_id):
    return Art.get_or_none(Art.id == art_id)

def get_art_by_availability():
    query = Art.select().where(Art.available == True)
    return list(query)

class ArtError(Exception):
    pass