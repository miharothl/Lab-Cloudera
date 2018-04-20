import findspark
findspark.init()
from pyspark import SparkContext
from pyspark import SparkConf

print("Hi, put breakpoint here!")

APP_NAME = 'Debug pyspark via docker!'
conf = SparkConf().setAppName(APP_NAME)
conf = conf.setMaster('local[*]')
sc = SparkContext(conf=conf)
lines = sc.textFile("/etc/hosts")
print(lines.count())

lineLength = lines.map(lambda s: len(s))
lineLength.persist()
totalLength = lineLength.reduce(lambda a, b: a + b)
print(totalLength)
