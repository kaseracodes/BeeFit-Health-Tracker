from app import db

class DailyEntry(db.model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    weight_kg = db.Column(db.Float)
    steps_walked = db.Column(db.Integer)
    sleep_hours = db.Column(db.Float)
    calories_consumed = db.Column(db.Integer)
    water_intake_liters = db.Column(db.Float)
    heart_rate_bpm =  db.Column(db.Integer)
    mood = db.Column(db.String(50))
    stress_level = db.Column(db.Integer)
    workout_type = db.Column(db.String(50))
    workout_duration_minutes = db.Column(db.Integer)