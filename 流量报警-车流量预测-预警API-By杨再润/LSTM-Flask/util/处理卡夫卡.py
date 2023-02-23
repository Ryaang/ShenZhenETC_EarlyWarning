import sys, os, re
import json
from pyspark import SparkContext, SparkConf
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils, OffsetRange, TopicAndPartition

# 每2 秒钟处理一次数据


def start():
    sconf = SparkConf()
    sconf.set('spark.cores.max', 3)
    sc = SparkContext(appName='spark_streaming_kafka_json', conf=sconf)
    sc.setLogLevel('WARN')
    ssc = StreamingContext(sc,2)
    brokers = "192.168.130.29:9092"
    topic = 'spark_streaming_kafka_json'
    user_data = KafkaUtils.createDirectStream(ssc, [topic], kafkaParams={"metadata.broker.list": brokers})

    # lines = KafkaUtils.createDirectStream(ssc, [topic], kafkaParams={"metadata.broker.list": broker_list})
    # lines.map(parse).cache().foreachRDD(handleResult)
    # lines.transform(store_offset_ranges).foreachRDD(save_offset_ranges)


    # object_stream = user_data.map(lambda x: json.loads(x[1]))
    object_stream = user_data.map(lambda x: (json.loads(x[1]))['value']).reduce(lambda x, y: x + y)


    #object_stream.pprint()
    tpprint(object_stream)

    # object_stream = user_data.map(lambda x: x[1])
    # object_stream.pprint()

    ssc.start()
    ssc.awaitTermination()

def tpprint(val, num=10000):
    """
    Print the first num elements of each RDD generated in this DStream.
    @param num: the number of elements from the first will be printed.
    """
    def takeAndPrint(time, rdd):
        taken = rdd.take(num + 1)
        print("########################")
        print("Time: %s" % time)
        print("########################")
        DATEFORMAT = '%Y%m%d'
        today = datetime.datetime.now().strftime(DATEFORMAT)
        myfile = open("./speech." + today, "a")
        for record in taken[:num]:
            print(record)
            myfile.write(str(record)+"\n")
        myfile.close()
        if len(taken) > num:
            print("...")
        print("")

    val.foreachRDD(takeAndPrint)

if __name__ == '__main__':
    start()

