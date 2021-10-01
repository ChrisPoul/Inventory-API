from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Model:

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self, data=None):
        if data is not None:
            for attr in data:
                setattr(self, attr, data[attr])
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
