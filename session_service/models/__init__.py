from flask_mongoengine import MongoEngine

from werkzeug.security import generate_password_hash


db = MongoEngine()


class User(db.Document):
    username = db.StringField(required=True)
    password = db.StringField(required=True)

    role = db.StringField(required=True)

    @staticmethod
    def create_mock_users():
        users = [
            User(
                username=f"student{i}",
                password=generate_password_hash(f"student{i}password")
                role="student",
            )
            for i in range(5)
        ]

        users.append(
            User(
                username=f"teacher",
                password=generate_password_hash(f"teacherpassword"),
                role="teacher",
            )
        )

        users.append(
            User(
                username=f"secretary",
                password=generate_password_hash(f"secretarypassword"),
                role="secretary",
            )
        )

        for user in users:
            user.save()
