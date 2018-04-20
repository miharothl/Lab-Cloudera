print("Hi, put breakpoint here!")

import findspark
findspark.init()

from pyspark import SparkContext
from pyspark import SparkConf

APP_NAME = 'my python script'
conf = SparkConf().setAppName(APP_NAME)
conf = conf.setMaster('local[*]')
sc = SparkContext(conf=conf)
lines = sc.textFile("/etc/hosts")

somelist = [1, 2, 3, 4, 5]

lines_p = sc.parallelize(somelist)
print(lines_p)

print(lines.count())
lineLength = lines.map(lambda s: len(s))
lineLength.persist()
totalLength = lineLength.reduce(lambda a,b:a+b)
print(totalLength)