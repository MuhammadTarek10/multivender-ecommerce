from database import database


class OwnerModel(database.Model):
    __tablename__ = 'owners'

    id = database.Column(database.Integer, primary_key=True)
    first_name = database.Column(database.String(80))
    last_name = database.Column(database.String(80))
    username = database.Column(database.String(80))
    password = database.Column(database.String(80))
    email = database.Column(database.String(120))

    stores = database.relationship('StoreModel')

    def __init__(self, first_name, last_name, username, password, email):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.email = email

    def save_to_database(self):
        database.session.add(self)
        database.session.commit()

    def json(self):
        return {"name": self.first_name, "stores": self.get_stores(), "email": self.email}

    def get_stores(self):
        values = []
        for i in range(len(self.stores)):
            values.append(self.stores[i].name)
        return values

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
