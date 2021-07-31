from flask_mongoengine import MongoEngine

from werkzeug.security import generate_password_hash

db = MongoEngine()


class User(db.Document):
    username = db.StringField(required=True)
    password = db.StringField(required=True)
    first_name = db.StringField()
    last_name = db.StringField()
    patronymic = db.StringField()
    admission_year = db.StringField()
    direction = db.StringField()
    group_num = db.StringField()

    role = db.StringField(required=True)

    @staticmethod
    def create_mock_users():
        users = [
            User(
                username=f"student{i}",
                password=generate_password_hash(f"student{i}password"),
                first_name=f"student{i}first_name",
                last_name=f"student{i}last_name",
                patronymic=f"student{i}patronymic",
                addmission_year=f"student{i}addmission_year",
                direction=f"student{i}direction",
                group_num=f"student{i}group_num",
                role="student",
            )
            for i in range(5)
        ]

        users.append(
            User(
                username=f"teacher",
                password=generate_password_hash(f"teacherpassword"),
                first_name=f"teacherfirst_name",
                last_name=f"teacherlast_name",
                patronymic=f"teacherpatronymic",
                addmission_year=f"teacheraddmission_year",
                direction=f"teacherdirection",
                group_num=f"teachergroup_num",
                role="teacher",
            )
        )

        users.append(
            User(
                username=f"secretary",
                password=generate_password_hash(f"secretarypassword"),
                first_name=f"secretatyfirst_name",
                last_name=f"secretatylast_name",
                patronymic=f"secretatypatronymic",
                addmission_year=f"secretatyaddmission_year",
                direction=f"secretatydirection",
                group_num=f"secretatygroup_num",
                role="secretary",
            )
        )

        for user in users:
            user.save()
