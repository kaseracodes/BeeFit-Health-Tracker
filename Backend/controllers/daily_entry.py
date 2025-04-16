from models.daily_entry import DailyEntry
from extensions import db

def create_entry(data):
    entry = DailyEntry(**data)
    db.session.add(entry)
    db.session.commit()
    return entry

def get_all_entries():
    return DailyEntry.query.all()

def get_entry_by_id(entry_id):
    return DailyEntry.query.get_or_404(entry_id)

def update_entry(entry_id, data):
    entry = get_entry_by_id(entry_id)
    for key, value in data.items():
        setattr(entry, key, value)
    db.session.commit()
    return entry

def delete_entry(entry_id):
    entry = get_entry_by_id(entry_id)
    db.session.delete(entry)
    db.session.commit()
    return True
