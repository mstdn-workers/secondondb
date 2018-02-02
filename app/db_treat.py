import psycopg2

class db_treat:
    def __init__(self, dsn_dict):
        self.connection = psycopg2.connect(
            dbname=dsn_dict['dbname'], 
            user=dsn_dict['user'], 
            password=dsn_dict['password'], 
            host=dsn_dict['host'], 
            port=dsn_dict['port'])
        self.cursor = connection.cursor()
    
    def close(self):
        self.cursor.close()
        self.connection.close()

    def insert(self, table, value):
        self.cursor.execute("INSERT INTO %s VALUES (%s)", (table, value))
        