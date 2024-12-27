import mysql.connector

class Database:
    def __init__(self):
        self.conn = None

    def connect(self):
        try:
            self.conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Qaz_123',
                database='medical_faq_chatbot'
            )
            print("Connected to database")
        except mysql.connector.Error as e:
            print("Error connecting to database: {}".format(e))

    def create_tables(self):
        with open('../db/schema.sql', 'r') as f:
            schema_sql = f.read()
        try:
            c = self.conn.cursor()
            c.executescript(schema_sql)
        except mysql.connector.Error as e:
            print("Error creating tables: {}".format(e))

    def seed_data(self):
        with open('../db/seed_data.sql', 'r') as f:
            seed_sql = f.read()
        try:
            c = self.conn.cursor()
            c.executescript(seed_sql)
        except mysql.connector.Error as e:
            print("Error seeding data: {}".format(e))

    def retrieve_data(self, table_name):
        sql = f"""SELECT * FROM {table_name};"""
        try:
            c = self.conn.cursor()
            c.execute(sql)
            rows = c.fetchall()
            return rows
        except mysql.connector.Error as e:
            print("Error retrieving data: {}".format(e))

    def close_connection(self):
        if self.conn:
            self.conn.close()
