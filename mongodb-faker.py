from faker import Faker
from pymongo import MongoClient

fake = Faker()


def random_docs():
    docs = []
    for _ in range(10000):
        doc = {
            'firstname': fake.first_name(),
            'lastname': fake.last_name(),
            'age': fake.random_int(min=0, max=110),
            'size': fake.pyfloat(min_value=150, max_value=200, right_digits=2),
            'alive': fake.pybool(),
            'timestamp': fake.unix_time(),
            'date_of_birth': fake.date(),
            'licence_date': fake.month() + "-" + str(fake.date_object().day) + "-" + fake.year(),
            'certificate_date': fake.iso8601(),
            'year_inserted': fake.year(),
            'month_inserted': fake.month(),
            'day_inserted': fake.random_int(min=0, max=28),
            'address_number': fake.building_number(),
            'street_name': fake.street_name(),
            'postcode': fake.postcode(),
            'city': fake.city(),
            'country': fake.country()
        }
        docs.append(doc)
    return docs


if __name__ == '__main__':
    client = MongoClient()
    collection = client.test.coll
    collection.drop()
    collection.insert_many(random_docs())
    print('Done!')
