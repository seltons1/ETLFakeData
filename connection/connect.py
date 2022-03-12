import psycopg2

class Connect():
    USER = None
    PASS = None
    HOST = None
    DB = None
    connected = None

    def __init__(self, USER, PASS, HOST, DB):
        self.USER = USER
        self.PASS = PASS
        self.HOST = HOST
        self.DB = DB

        try:
            conn = psycopg2.connect(host=self.HOST, database=self.DB, user=self.USER, password=self.PASS)

            self.connected = conn
            print("You are Connected!")
            return self.connected
        except psycopg2.errorcodes as e:
            print(e)
            return None

    def commit(self):
        self.connected.commit()

    def execute_query(self, query):
        cursor = self.connected.cursor()
        cursor.execute(query)
        self.commit()

    def execute_query(self, query, params):
        cursor = self.connected.cursor()
        cursor.execute(query,params)
        rs = cursor.fetchall()
        return rs