from faker import Faker

class GenerateFake():
    
    conn = None
    '''
    def __init__(self, connection):
        self.conn = connection
    '''
    
    def generate():
        
        faker = Faker(["pt_BR"])
        qtd = 0
        while qtd < 10:
            data = []
            data.append(faker.name())
            data.append(faker.job())
            print(data)
            ins = "INSERT INTO person(name, job, address, phone_number, email, record_date, id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s,)"
            qtd = qtd + 1

if __name__ == "__main__":
    
    gen = GenerateFake.generate()
    