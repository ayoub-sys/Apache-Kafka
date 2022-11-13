from kafka import KafkaConsumer
import json 

if __name__=='__main__':
    consumer=KafkaConsumer(
        'registred_user',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        group_id="consumer-group-a"
    )
    print('start the consumer')
    for msg in consumer:
        print("Registred User={}".format(json.loads(msg.value)))
