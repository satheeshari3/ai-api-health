from extensions import db
from datetime import datetime

class HealthLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    endpoint_id = db.Column(db.Integer)
    status = db.Column(db.Integer)
    response_time = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)