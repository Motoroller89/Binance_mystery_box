import psycopg2
import psycopg2.extras

from config import host, user, password, db_name


# Избавиться от sql иньекицй
class PostgreSql:

    def __init__(self, database_file):
        self.connection = psycopg2.connect(
            dbname=db_name,
            user=user,
            host=host,
            password=password
        )

        self.cursor = self.connection.cursor()

    def add_subscriber(self, user_id, UserName):
        """ Append new user"""
        with self.connection:
            return self.cursor.execute(f"INSERT INTO subscription(username,user_id) values ('{UserName}',{user_id})")

    def subscriber_exists(self, user_id):
        """ Проверяем есть ли в базе"""
        with self.connection:
            self.cursor.execute(f"SELECT * FROM subscription where user_id = {user_id} and  status = True")
            return bool(len(self.cursor.fetchall()))

    def update_subscription(self, user_id, status):
        """ update status subscriber"""
        return self.cursor.execute(f"UPDATE subscription set status = {status} where user_id = {user_id} ")

    def add_date(self, product_id, number, csrftoken, cookie, device_info, bnc_uuid, user_id):
        with self.connection:
            return self.cursor.execute(
                f"update subscription set product_id ={product_id}, number = {number}, csrftoken = '{csrftoken}', cookie = '{cookie}', device_info = '{device_info}', bnc_vuid = '{bnc_uuid}' where user_id = {user_id}")

    def post_product_id(self, user_id):
        with self.connection:
            self.cursor.execute(f"select product_id,number from subscription where user_id = {user_id}")
            rows = self.cursor.fetchall()
            for row in rows:
                return row[0], row[1]

    def post_date_in_setting(self, user_id):
        with self.connection:
            self.cursor.execute(
                f"select csrftoken,cookie,device_info,bnc_vuid from subscription where user_id = {user_id}")
            rows = self.cursor.fetchall()
            for row in rows:
                return row[0], row[1], row[2], row[3]

    def close(self):
        """close connection with bd"""
        self.connection.close()
