源代码主要是.java文件
其中./src/main/java/me/yzrEntryAlert.java文件
实现了从Kafka读取数据，
通过重写watermark、设定时间窗口、计算车流量后，
存入Redis
