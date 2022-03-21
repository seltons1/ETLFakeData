from faker import Faker
import sys
sys.path.append("..")
from connection.con import Connect

class GenerateFake():
    
    conn = None
    '''
    def __init__(self, connection):
        self.conn = connection
    '''
    
    def generate():
        
        conn = Connect('postgres','123456','localhost','data_fake')
        cnx = conn.cnx()
        cnx.autocommit = False
        
        faker = Faker(["pt_BR"])
        qtd = 0
        data = []
        while qtd < 10:
            
            data.append(faker.name())
            data.append(faker.job())
            data.append(faker.address())
            data.append(faker.phone_number())
            data.append(faker.email())
            data.append(faker.date_time_this_century())
            data.append(faker.random_int())
            
            #print(data)
            qtd = qtd + 1
        cursor = cnx.cursor()
        ins = "INSERT INTO person(name, job, address, phone_number, email, record_date, id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        
        try:
            cursor.executemany(ins, data)
            cnx.commit()
            #print(str(cursor.rowcount)+" registros inseridos...")
        except Exception as e:
            print(e)
        finally:
            cursor.close()
            cnx.close()
            print("Removendo instancia da Database... OK")
        
        

if __name__ == "__main__":
    
    gen = GenerateFake.generate()
    