from flask_restful import Resource, reqparse
from models.rate_to_owner import RateToOwnerModel
from models.user import UserModel
from models.owner import OwnerModel

class RateToOwner(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('user_id',
            type=int,
            required=True,
            help='fill that part'
    )

    parser.add_argument('owner_id',
            type=int,
            required=True,
            help='fill that part'
    )

    parser.add_argument('rate',
            type=float,
            required=True,
            help='fill that part'
    )

    def post(self):
        data = self.parser.parse_args()

        if not UserModel.find_by_id(data['user_id']):
            return {"message": "no user with that id"}

        if not OwnerModel.find_by_id(data['owner_id']):
            return {"message": "no owner with that id"}

        if RateToOwnerModel.already_rated(**data):
                return {"message": "you already rated this owner"}

        rate = RateToOwnerModel(**data)
        try:
            rate.save_to_database()
        except:
            return {"message": "error while adding to database"}

        return rate.json(), 201