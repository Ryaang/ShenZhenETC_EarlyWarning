"""
造数器：向kafka发送json格式数据

数据格式如下所示：
{
    "namespace":"000001",
    "region"："Beijing",
    "id":"9d58f83e-fb3b-45d8-b7e4-13d33b0dd832",
    "valueType":"Float",
    "value":"48.5",
    "time":"2018-11-05 15:04:47"
}
"""
import uuid
import time
import random
from pykafka import KafkaClient
import json

sample_type = ['Float', 'String', 'Int']
sample_namespace = ['000000', '000001', '000002']
sample_region = ['Beijing', 'Shanghai', 'Jinan', 'Qingdao', 'Yantai', 'Hangzhou']
sample_id_info = [
    {'3f7e7feb-fce6-4421-8321-3ac7c712f57a': {'valueType': 'Float', 'region': 'Shanghai', 'namespace': '000001'}},
    {'42f3937e-301c-489e-976b-d18f47df626f': {'valueType': 'Float', 'region': 'Beijing', 'namespace': '000000'}},
    {'d61e5ac7-4357-4d48-a6d9-3e070927f087': {'valueType': 'Int', 'region': 'Beijing', 'namespace': '000000'}},
    {'ddfca6fe-baf5-4853-8463-465ddf8234b4': {'valueType': 'String', 'region': 'Hangzhou', 'namespace': '000001'}},
    {'15f7ef13-2100-464c-84d7-ce99d494f702': {'valueType': 'Int', 'region': 'Qingdao', 'namespace': '000001'}},
    {'abb43869-dd0b-4f43-ab9d-e4682cb9c844': {'valueType': 'Int', 'region': 'Beijing', 'namespace': '000000'}},
    {'b63c1a92-c76c-4db3-a8ac-66d67c9dc6e6': {'valueType': 'Int', 'region': 'Yantai', 'namespace': '000001'}},
    {'0cf781ae-8202-4986-8df5-7ca0b21c094e': {'valueType': 'String', 'region': 'Yantai', 'namespace': '000002'}},
    {'42073ecd-0f23-49d6-a8ba-a8cbee6446e3': {'valueType': 'Float', 'region': 'Beijing', 'namespace': '000000'}},
    {'bd1fc887-d980-4488-8b03-2254165da582': {'valueType': 'String', 'region': 'Shanghai', 'namespace': '000000'}},
    {'eec90363-48bc-44b7-90dd-f79288d34f39': {'valueType': 'String', 'region': 'Shanghai', 'namespace': '000002'}},
    {'fb15d27f-d2e3-4048-85b8-64f4faa526d1': {'valueType': 'Float', 'region': 'Jinan', 'namespace': '000001'}},
    {'c5a623fd-d67b-4d83-8b42-3345352b8db9': {'valueType': 'String', 'region': 'Qingdao', 'namespace': '000001'}},
    {'fee3ecb2-dd1a-4421-a8bd-cf8bc6648320': {'valueType': 'Float', 'region': 'Yantai', 'namespace': '000001'}},
    {'e62818ab-a42a-4342-be31-ba46e0ae7720': {'valueType': 'Float', 'region': 'Qingdao', 'namespace': '000001'}},
    {'83be5bdc-737c-4616-a576-a15a2c1a1684': {'valueType': 'String', 'region': 'Hangzhou', 'namespace': '000001'}},
    {'14dcd861-14eb-40f3-a556-e52013646e6d': {'valueType': 'String', 'region': 'Beijing', 'namespace': '000002'}},
    {'8117826d-4842-4907-b6eb-446fead74244': {'valueType': 'String', 'region': 'Beijing', 'namespace': '000001'}},
    {'fb23b254-a873-4fba-a17d-73fdccbfe768': {'valueType': 'Int', 'region': 'Yantai', 'namespace': '000000'}},
    {'0685c868-2f74-4f91-a531-772796b1c8a4': {'valueType': 'String', 'region': 'Shanghai', 'namespace': '000001'}}]


def generate_id_info(amount=20):
    """
    生成id 信息，只执行一次
    :return:
    [{
    "id":{
        "type":"Int",
        "region":"Hangzhou"
    }
    }]
    """
    return [{str(uuid.uuid4()): {"valueType": random.sample(sample_type, 1)[0],
                                 "region": random.sample(sample_region, 1)[0],
                                 "namespace": random.sample(sample_namespace, 1)[0]
                                 }} for i in range(amount)]


def random_value(value_type):
    value = 0
    if value_type == "Float":
        value = random.uniform(1, 100)
    if value_type == "Int":
        value = random.randint(1, 100)
    return value


def generate_data(id_info):
    data = dict()
    for _id, info in id_info.items():
        data = {"id": _id,
                "value": random_value(info['valueType']),
                "time": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
                }
        data.update(info)
    return data


def random_data():
    return generate_data(random.sample(sample_id_info, 1)[0])


if __name__ == '__main__':
    client = KafkaClient(hosts="192.168.130.28:9092", zookeeper_hosts="192.168.130.28:2181")
    topic = client.topics[b"spark_streaming_kafka_json"]
    with topic.get_sync_producer() as producer:
        for i in range(1000):
            _random_data = json.dumps(random_data())
            print(_random_data)
            producer.produce(bytes(_random_data, encoding="utf-8"))
            time.sleep(1)
