# models.py
from app import db

class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(80), nullable=False, unique=True)
    files = db.relationship('LogFile', backref='project', lazy=True)

class LogFile(db.Model):
    __tablename__ = 'log_files'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    file_name = db.Column(db.String, nullable=False)
    file_path = db.Column(db.String, nullable=False)
    checksum = db.Column(db.String(64), nullable=True)
    processed_time = db.Column(db.DateTime, nullable=True)
    filtered_files = db.relationship('FilteredFile', backref='log_file', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'project_id': self.project_id,
            'file_name': self.file_name,
            'file_path': self.file_path
        }

class FilteredFile(db.Model):
    __tablename__ = 'filtered_files'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    log_file_id = db.Column(db.Integer, db.ForeignKey('log_files.id'), nullable=False)
    filtered_file_name = db.Column(db.String, nullable=False)
    filtered_file_path = db.Column(db.String, nullable=False)
    checksum = db.Column(db.String(64), nullable=True)
    processed_time = db.Column(db.DateTime, nullable=True)
