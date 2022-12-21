import model
import config
import mysql.connector


class Managment_user:



    def AddUser(self, user: model.Data_user):    # Добавление данных пользователя в БД

        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                add_user = f"""
                    INSERT INTO users
                    (telegID, username, name)
                    VALUES
                    ({user.telegchatID}, '{user.username}', '{user.name}')

                """
                with connection.cursor() as cursor:
                    cursor.execute(add_user)
                    connection.commit()
        except Exception as e:
            return e

    def GetMedical(self, typeID):    # Добавление данных пользователя в БД

        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                get_medical = f"""
                    SELECT name, address, number_phone, website from medical where typeID = {typeID}

                """
                with connection.cursor() as cursor:
                    cursor.execute(get_medical)
                    send = []
                    for row in cursor.fetchall():
                        send.append(model.Data_medical(row[0], row[1], row[2], row[3]))
                    return send
        except Exception as e:
            return e

    def GetEntertainments(self, typeID):    # Добавление данных пользователя в БД

        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                get_entertainments = f"""
                    SELECT name, address, number_phone, website from entertainments where typeID = {typeID}

                """
                with connection.cursor() as cursor:
                    cursor.execute(get_entertainments)
                    send = []
                    for row in cursor.fetchall():
                        send.append(model.Data_entertainments(row[0], row[1], row[2], row[3]))
                    return send
        except Exception as e:
            return e
    def GetEat(self, typeID):    # Добавление данных пользователя в БД

        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                get_eat = f"""
                    SELECT name, address, number_phone, website from eat where typeID = {typeID}

                """
                with connection.cursor() as cursor:
                    cursor.execute(get_eat)
                    send = []
                    for row in cursor.fetchall():
                        send.append(model.Data_eat(row[0], row[1], row[2], row[3]))
                    return send
        except Exception as e:
            return e


    def GetSchool(self, typeID):    # Добавление данных пользователя в БД

        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                get_school = f"""
                    SELECT name, website from school where typeID = {typeID}

                """
                with connection.cursor() as cursor:
                    cursor.execute(get_school)
                    send = []
                    for row in cursor.fetchall():
                        send.append(model.Data_school(row[0], row[1]))
                    return send
        except Exception as e:
            return e

    def GetStudu(self, typeID):    # Добавление данных пользователя в БД

        try:
            with mysql.connector.connect(host=config.host,
                                         user=config.user,
                                         password=config.password,
                                         database=config.database,
                                         ) as connection:
                get_school = f"""
                    SELECT name, description, website from eat where typeID = {typeID}

                """
                with connection.cursor() as cursor:
                    cursor.execute(get_school)
                    send = []
                    for row in cursor.fetchall():
                        send.append(model.Data_school(row[0], row[1]))
                    return send
        except Exception as e:
            return e