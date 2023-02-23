SERVER = 'node4'
USERNAME = 'kingname'
PASSWORD = 'kingnameisgod'
TOPIC = 'rawETC'
from kafka import KafkaConsumer


consumer = KafkaConsumer(TOPIC,
                         bootstrap_servers=SERVER,
                         group_id='test',
                         auto_offset_reset='earliest')
for msg in consumer:
    print(msg.value)
