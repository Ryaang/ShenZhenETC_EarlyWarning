package me.yzr;
import org.apache.flink.api.common.functions.FilterFunction;
import org.apache.flink.api.common.functions.MapFunction;
import org.apache.flink.api.java.tuple.Tuple2;
import org.apache.flink.api.java.tuple.Tuple3;
import org.apache.flink.streaming.api.TimeCharacteristic;
import org.apache.flink.api.common.functions.AggregateFunction;
import org.apache.flink.streaming.api.datastream.DataStreamSource;
import org.apache.flink.streaming.api.datastream.SingleOutputStreamOperator;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.api.functions.timestamps.BoundedOutOfOrdernessTimestampExtractor;
import org.apache.flink.streaming.api.windowing.time.Time;
import org.apache.flink.streaming.connectors.kafka.FlinkKafkaConsumer;
import org.apache.flink.api.common.serialization.SimpleStringSchema;
import org.apache.flink.streaming.connectors.redis.RedisSink;
import org.apache.flink.streaming.connectors.redis.common.config.FlinkJedisPoolConfig;
import org.apache.flink.streaming.connectors.redis.common.mapper.RedisCommand;
import org.apache.flink.streaming.connectors.redis.common.mapper.RedisCommandDescription;
import org.apache.flink.streaming.connectors.redis.common.mapper.RedisMapper;


import java.time.LocalDateTime;
import java.time.ZoneOffset;
import java.time.format.DateTimeFormatter;
import java.util.Properties;

public class CountWindow {
    //使用flink api 实现窗口内的收费站入口车辆数超过阈值的报警
    public static void main(String[] args) throws Exception {
        //创建redisSink
        RedisSink<Tuple2<String, Long>> redisSink = new RedisSink<>(
                new FlinkJedisPoolConfig.Builder()
                        .setHost("node4")
                        .setPort(6379)
                        .setPassword("redis_password")
                        .build(),
                new RedisMapper<Tuple2<String, Long>>() {
                    @Override
                    public RedisCommandDescription getCommandDescription() {
                        return new RedisCommandDescription(RedisCommand.HSET, "my-hash-key");
                    }

                    @Override
                    public String getKeyFromData(Tuple2<String, Long> data) {
                        return data.f0;
                    }

                    @Override
                    public String getValueFromData(Tuple2<String, Long> data) {
                        return String.valueOf(data.f1);
                    }
                    //定时过期
                    public String getExpirationFromData(Tuple2<String, Long> data) {
                        return "6";
                    }

                }
        );



        StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
        // 设置事件时间
        env.setStreamTimeCharacteristic(TimeCharacteristic.EventTime);
        // 设置并行度
//        env.setParallelism(1);

        //从socket中读取数据
//        DataStream<String> text = env.socketTextStream("node1", 25565);
        //数据格式： 225,2020/12/22 00:07,一型车(客),松山湖南,2020/12/22 00:03,深圳入,广东罗田主线站,粤A64***

        //kafka连接配置信息
        Properties prop = new Properties();
        prop.put("bootstrap.servers", "node4:9092");
        prop.put("zookeeper.connect", "node4:2181");
        prop.put("group.id", "g7");
        prop.put("key.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        prop.put("value.serializer", "org.apache.kafka.common.serialization.StringSerializer");
        prop.put("auto.offset.reset", "earliest");
        DataStreamSource<String> text = env.addSource(new FlinkKafkaConsumer<String>(
                "rawETC",
                new SimpleStringSchema(),
                prop
        )).setParallelism(1);//单线程打印，控制台不乱序，不影响结果
//        dataStreamSource.print();
        //数据格式
        //0沪','17006','2四型车(客)','3松山湖南','42022-12-21 10:50:23','5湖南雁峰站','62022-12-19 23:59:39','7深圳入

        // 在执行任何操作前需要先执行watermark设置
        SingleOutputStreamOperator<Tuple2<String, Long>> count = text.assignTimestampsAndWatermarks(new BoundedOutOfOrdernessTimestampExtractor<String>(Time.minutes(1L)) {
                    @Override
                    public long extractTimestamp(String element) {
                        int time = (int) LocalDateTime.parse(element.split("','")[6], DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")).toEpochSecond(ZoneOffset.ofHours(8));
                        return time * 1000L;
                    }
                }).map(new MapFunction<String, Tuple2<String, Long>>() {
                    @Override
                    public Tuple2<String, Long> map(String s) throws Exception {
                        String[] items = s.split("','");
                        // 返回 时间 -> 入口名称 -> 车辆数目默认为1
                        Integer time = (int) LocalDateTime.parse(items[6], DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss")).toEpochSecond(ZoneOffset.ofHours(8));
                        String entry_name = items[3];
                        Long car_num = 1L;
                        return new Tuple2<>(entry_name, car_num);
                    }});
        //设置窗口大小为5秒的、根据String对Long计数的窗口
        count.keyBy(0)
                .timeWindow(Time.seconds(5))
                .sum(1)
                .print();

        //按照入口名称分组

        //输出到控制台
//        count.print();
        count.filter((FilterFunction<Tuple2<String, Long>>) stringLongTuple2 -> stringLongTuple2.f1 > 5);
        //输出到redis
        count.addSink(redisSink);

        //将结果写入redis
//        DataStreamSink<Tuple2<String, Long>> sink = count.addsink(redisSink);
        env.execute("EntryAlert");
    }


//集群启动： flink run -c me.yzr.EntryAlert Monitor-1.0.0.jar
/*
卡夫卡生产数据:
/usr/kafka/bin/kafka-server-start.sh config/server.properties
/usr/flume/bin/flume-ng agent -c conf/ -n al -f jobs/file2kafka.conf
/usr/py python ./input_logs.py start


 */
}

/*
redis增量数据
消息队列？
 */
