import psycopg2
import psycopg2.extras
import os



# Избавиться от sql иньекицй
class PostgreSql:

    def __init__(self):
        self.connection = psycopg2.connect(
            host = 'ec2-52-208-185-143.eu-west-1.compute.amazonaws.com',
            database  = 'd5b9a4s137v9j0',
            user = 'cnhwbwwxgxegnn',
            port= '5432',
            password = '79cf742acc0d215e07466c4871726d193914c4037eb5208c665e3d30db9d8b87',

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

    def subscriber_exists_super_sub(self, user_id):
        """ Проверяем есть ли в базе"""
        with self.connection:
            self.cursor.execute(f"SELECT * FROM subscription where user_id = {user_id} and  super_sub = True")
            return bool(len(self.cursor.fetchall()))

    def have_users(self, user_id):
        """ Проверяем есть ли в базе"""
        with self.connection:
            self.cursor.execute(f"SELECT * FROM subscription where user_id = {user_id}")
            return bool(len(self.cursor.fetchall()))



    def update_subscription(self, user_id, status):
        """ update status subscriber"""
        return self.cursor.execute(f"UPDATE subscription set status = {status} where user_id = {user_id} ")

    def add_date(self, product_id, number, csrftoken, cookie, device_info, bnc_uuid, user_id,nomer):
        with self.connection:
            return self.cursor.execute(
                f"update subscription set product_id{nomer} ={product_id}, number{nomer} = {number}, csrftoken{nomer} = '{csrftoken}', cookie{nomer} = '{cookie}', device_info{nomer} = '{device_info}', bnc_vuid{nomer} = '{bnc_uuid}' where user_id = {user_id}")



    def post_product_id(self, user_id,account):
        with self.connection:
            self.cursor.execute(f"select product_id{account},number{account} from subscription where user_id = {user_id}")
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

    def add_referal(self, user_id, UserName):
        with self.connection:
            return self.cursor.execute(f"Insert into referal(user_name,id_user)  values('{UserName}',{user_id})")

    def add_code(self, user_id, code):
        with self.connection:
            return self.cursor.execute(f"UPDATE referal set code = '{code}' where id_user = {user_id} ")

    def code_cheak(self, user_id):
        with self.connection:
            self.cursor.execute(f"select * from  referal where  id_user= {user_id} and code IS NULL")
            return bool(len(self.cursor.fetchall()))

    def return_code(self,user_id):
            with self.connection:
                self.cursor.execute(
                    f"select code from referal where id_user = {user_id}")
            rows = self.cursor.fetchall()
            for row in rows:
                return row[0]

    def add_invite(self, word):
        with self.connection:
            return self.cursor.execute(f"update referal set users_invite = users_invite +{1} where code = '{word}'")

    def return_users(self,user_id):
            with self.connection:
                self.cursor.execute(
                    f"select users_invite from referal where id_user = {user_id}")
            rows = self.cursor.fetchall()
            for row in rows:
                return row[0]
    def close(self):
        """close connection with bd"""
        self.connection.close()
