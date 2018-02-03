import psycopg2

class db_treat:
    def __init__(self, dsn_dict):
        self.connection = psycopg2.connect(
            dbname=dsn_dict['dbname'], 
            user=dsn_dict['user'], 
            password=dsn_dict['password'], 
            host=dsn_dict['host'], 
            port=dsn_dict['port'])
        self.cursor = self.connection.cursor()
    
    def close(self):
        self.cursor.close()
        self.connection.close()

    def insert(self, id, json_str):
        self.cursor.execute("INSERT INTO localtimeline VALUES (%s, %s)", [id, json_str])
        self.connection.commit() 

    def insert_all(self, status):
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
        self.cursor.execute(sql)
        self.connection.commit()


        