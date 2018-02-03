import psycopg2

class db_treat:
    def __init__(self, dsn_dict):
        self.dsn_dict = dsn_dict

    def insert(self, id, json_str):
        with psycopg2.connect(
            dbname=self.dsn_dict['dbname'], 
            user=self.dsn_dict['user'], 
            password=self.dsn_dict['password'], 
            host=self.dsn_dict['host'], 
            port=self.dsn_dict['port']) as conn:
            cursor = conn.cursor()
            sql = "INSERT INTO localtimeline VALUES ('" + id + "', '" + json_str +"');"
            print(sql)
            cursor.execute(sql)
            conn.commit()

    def insert_all(self, status):
        with psycopg2.connect(
            dbname=self.dsn_dict['dbname'], 
            user=self.dsn_dict['user'], 
            password=self.dsn_dict['password'], 
            host=self.dsn_dict['host'], 
            port=self.dsn_dict['port']) as conn:
            cursor = conn.cursor()
            # self.cursor.execute("INSERT INTO localtimeline VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", [
            print( status.keys() )
            keys = ""
            values = ""
            kc = 0
            vc = 0
            for k in status.keys():
                if keys == "":
                    keys = k
                    values = str(status[k])
                    kc = kc + 1
                    vc = vc + 1
                else:
                    keys = keys + ", " + k
                    values = values + ", '" + str(status[k]) + "'" 
                    kc = kc + 1
                    vc = vc + 1
            print(str(kc)+"keys: "+keys)
            print(str(vc)+"values: "+values)
            sql = "INSERT INTO localtimeline (" + keys + ") VALUES (" + values + ");"
            cursor.execute(sql)
            conn.commit()


        