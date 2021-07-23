from flask_mongoengine import MongoEngine

from werkzeug.security import generate_password_hash


db = MongoEngine()

class Table(db.Document):
    check = db.StringField(required=True)


    monday = db.StringField()
    tuesday = db.StringField()
    wednesday = db.StringField()
    thursday = db.StringField()
    friday = db.StringField()
    saturday = db.StringField()


    m_1_u = db.StringField()
    m_2_u = db.StringField()
    m_3_u = db.StringField()
    m_4_u = db.StringField()
    m_5_u = db.StringField()
    m_6_u = db.StringField()
    m_7_u = db.StringField()

    m_1_d = db.StringField()
    m_2_d = db.StringField()
    m_3_d = db.StringField()
    m_4_d = db.StringField()
    m_5_d = db.StringField()
    m_6_d = db.StringField()
    m_7_d = db.StringField()
    

    t_1_u = db.StringField()
    t_2_u = db.StringField()
    t_3_u = db.StringField()
    t_4_u = db.StringField()
    t_5_u = db.StringField()
    t_6_u = db.StringField()
    t_7_u = db.StringField()
    
    t_1_d = db.StringField()
    t_2_d = db.StringField()
    t_3_d = db.StringField()
    t_4_d = db.StringField()
    t_5_d = db.StringField()
    t_6_d = db.StringField()
    t_7_d = db.StringField()


    w_1_u = db.StringField()
    w_2_u = db.StringField()
    w_3_u = db.StringField()
    w_4_u = db.StringField()
    w_5_u = db.StringField()
    w_6_u = db.StringField()
    w_7_u = db.StringField()
    
    w_1_d = db.StringField()
    w_2_d = db.StringField()
    w_3_d = db.StringField()
    w_4_d = db.StringField()
    w_5_d = db.StringField()
    w_6_d = db.StringField()
    w_7_d = db.StringField()


    th_1_u = db.StringField()
    th_2_u = db.StringField()
    th_3_u = db.StringField()
    th_4_u = db.StringField()
    th_5_u = db.StringField()
    th_6_u = db.StringField()
    th_7_u = db.StringField()

    th_1_d = db.StringField()
    th_2_d = db.StringField()
    th_3_d = db.StringField()
    th_4_d = db.StringField()
    th_5_d = db.StringField()
    th_6_d = db.StringField()
    th_7_d = db.StringField()


    f_1_u = db.StringField()
    f_2_u = db.StringField()
    f_3_u = db.StringField()
    f_4_u = db.StringField()
    f_5_u = db.StringField()
    f_6_u = db.StringField()
    f_7_u = db.StringField()

    f_1_d = db.StringField()
    f_2_d = db.StringField()
    f_3_d = db.StringField()
    f_4_d = db.StringField()
    f_5_d = db.StringField()
    f_6_d = db.StringField()
    f_7_d = db.StringField()


    s_1_u = db.StringField()
    s_2_u = db.StringField()
    s_3_u = db.StringField()
    s_4_u = db.StringField()
    s_5_u = db.StringField()
    s_6_u = db.StringField()
    s_7_u = db.StringField()

    s_1_d = db.StringField()
    s_2_d = db.StringField()
    s_3_d = db.StringField()
    s_4_d = db.StringField()
    s_5_d = db.StringField()
    s_6_d = db.StringField()
    s_7_d = db.StringField()

    @staticmethod
    def create_mock_tables():
        tables = (
            Table(
    check=f"ИБ12020",
        monday = "Понедельник",
    m_5_u = "Философия",
    m_6_d = "Философия",    
        tuesday = "Вторник",
    t_2_u = "Основы информационной безопасности",
    t_3_u = "Основы информационной безопасности",
    t_4_u = "Физическая культура",
    t_2_d = "Основы информационной безопасности",
    t_3_d = "Основы информационной безопасности",
    t_4_d = "Физическая культура",    
        wednesday = "Среда",
    w_2_u = "Математический анализ",
    w_3_u = "Иностранный язык",
    w_4_u = "Информатика",
    w_3_d = "Иностранный язык",
    w_4_d = "Информатика",
        thursday = "Четверг",
    th_1_u = "Физическая культура",
    th_2_u = "Основы геодезии",
    th_3_u = "Математический анализ",
    th_4_u = "Основы геодезии",
    th_1_d = "Физическая культура",
    th_2_d = "Основы геодезии",
    th_3_d = "Математический анализ",
    th_4_d = "Основы геодезии",
        friday = "Пятница",
    f_1_u = "Основы управленческой деятельности",
    f_2_u = "Истоия и современная система защиты информации в России",
    f_1_d = "Основы управленческой деятельности",
    f_2_d = "Истоия и современная система защиты информации в России",
    f_3_d = "Основы управленческой деятельности",
            ).save()
        )

class User(db.Document):
    username = db.StringField(required=True)
    password = db.StringField(required=True)
    first_name = db.StringField()
    last_name = db.StringField()
    patronymic = db.StringField()
    addmission_year = db.StringField()
    direction = db.StringField()
    group_num = db.StringField()


    role = db.StringField(required=True)

    @staticmethod
    def create_mock_users():
        users = [
            User(
                username=f"student{i}",
                password=generate_password_hash(f"student{i}password"),
                first_name = f"student{i}first_name",
                last_name = f"student{i}last_name",
                patronymic = f"student{i}patronymic",
                addmission_year =f"student{i}addmission_year",
                direction = f"student{i}direction",
                group_num = f"student{i}group_num",
                role="student",
            )
            for i in range(5)
        ]

        users.append(
            User(
                username=f"teacher",
                password=generate_password_hash(f"teacherpassword"),
                first_name = f"teacherfirst_name",
                last_name = f"teacherlast_name",
                patronymic = f"teacherpatronymic",
                addmission_year =f"teacheraddmission_year",
                direction = f"teacherdirection",
                group_num = f"teachergroup_num",
                role="teacher",
            )
        )

        users.append(
            User(
                username=f"secretary",
                password=generate_password_hash(f"secretarypassword"),
                first_name = f"secretatyfirst_name",
                last_name = f"secretatylast_name",
                patronymic = f"secretatypatronymic",
                addmission_year =f"secretatyaddmission_year",
                direction = f"secretatydirection",
                group_num = f"secretatygroup_num",
                role="secretary",
            )
        )

        users.append(
            User(
                username=f"test",
                password=generate_password_hash(f"testpassword"),
                first_name = f"testfirst_name",
                last_name = f"testlast_name",
                patronymic = f"testpatronymic",
                addmission_year =f"2020",
                direction = f"ИБ",
                group_num = f"1",
                role="student",
            )
        )

       
        for user in users:
            user.save()
