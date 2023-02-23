# encoding = utf-8
"""
读取 kafka 的用户操作数据并打印
设定编码
"""
from kafka import KafkaConsumer

topic = 'rawETC'
bootstrap_servers = ['node4:9092']
group_id = 'group77'

consumer = KafkaConsumer(
    topic,  # topic的名称
    group_id=group_id,  # 指定此消费者实例属于的组名，可以不指定
    bootstrap_servers=bootstrap_servers,  # 指定kafka服务器
    auto_offset_reset='earliest',  # 'smallest': 'earliest', 'largest': 'latest'
)

for msg in consumer:
    print(msg.value.decode('utf-8'))
    # print(msg)
