import psycopg2

class db_treat:
    def __init__(self, dsn):
        self.dsn = dsn

    def insert(self, id, json_str):
        with psycopg2.connect(self.dsn) as conn:
            cur = conn.cursor()
            sql = "INSERT INTO localtimeline VALUES ('" + id + "', '" + json_str +"');"
            cur.execute(sql)
            conn.commit()
    def delete(self, id):
        with psycopg2.connect(self.dsn) as conn:
            cur = conn.cursor()
            sql = "DELETE FROM localtimeline WHERE id='" + id + "';"
            cur.execute(sql)
            conn.commit() 


        