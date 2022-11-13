from kafka import KafkaProducer
import json 
from data import get_registred_user
import time 

def json_serializer(data):
    return json.dumps(data).encode("utf-8")

producer=KafkaProducer(bootstrap_servers='localhost:9092', value_serializer=json_serializer)

if __name__=="__main__":
    while 1==1:
        registred_user=get_registred_user()
        print(registred_user)
        producer.send('registred_user',registred_user)
        time.sleep(4)
