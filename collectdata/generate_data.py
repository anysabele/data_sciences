import pandas as pd
import random 
from faker import Faker

faker = Faker()

person_data = []

for _ in range(10):
    name = faker.name()
    ssn = faker.ssn()
    age = random.randint(21, 60)
    date = faker.date_of_birth(minimum_age=age, maximum_age=age).strftime('%m/%d/%Y')
    address = faker.address()
    state = faker.state()
    country = 'USA'

    person = {
        'name': name,
        'ssn': ssn,
        'age': age,
        'date': date,
        'state': state,
        'address': address,
        'country': country
    }

    person_data.append(person)
df_person = pd.DataFrame(person_data)
print(df_person)

#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)
#pd.set_option('display.max_colwidth', None)
#pd.set_option('display.width', None)

print(df_person.to_string())

#df_person.to.to_csv('customers.csv')

