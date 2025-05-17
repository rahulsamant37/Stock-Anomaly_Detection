import json
import time

from faker import Faker
from kafka import KafkaProducer
import random

faker = Faker(['en_US'])


def generate_data():
    data = {'user_id': random.getrandbits(32),
            'event_type': random.choice(['click', 'view', 'purchase']),
            'country': faker.country_code(),
            'city': faker.city(),
            'device': random.choice(['mobile', 'desktop', 'tablet']),
            'product_id': random.getrandbits(32),
            'price': round(random.uniform(5.0, 500.0), 2),
            'quantity': random.randint(1, 100),
            'timestamp': round(time.time())}

    return data

if __name__ == '__main__':
    fake = Faker()
    topic_name = 'ecommerce_data'
    producer = KafkaProducer(
        bootstrap_servers=['localhost:29092', 'localhost:39092'],
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    count = 0
    while count < 50:
        rec = generate_data()
        producer.send(topic_name, value=rec)
        count +=1
        print(f'Record[{count}]: {rec}')
        producer.flush()