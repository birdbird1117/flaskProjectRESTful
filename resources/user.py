import sqlite3
from flask_restful import Resource, reqparse

from models.usermodel import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be blank."
                        )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "User created already."}, 400

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        # query = "SELECT * from users"
        # for row in cursor.execute(query):
        #     if row[0] == data['username']:
        #         return {"message" : "User created already."}, 201

        query = "INSERT INTO users VALUES (NULL, ?, ?)"
        cursor.execute(query, (data['username'], data['password']))

        connection.commit()
        connection.close()

        return {"message": "User created successfully."}, 201