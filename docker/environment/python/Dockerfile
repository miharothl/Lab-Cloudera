FROM ubuntu:latest  

##############################################################################
# Pycharm pyspark debug requiremntes
##############################################################################

RUN apt-get update

# Install tools
RUN apt-get install --no-install-recommends --no-install-suggests -y \
    vim \
    #python3-pip \
    python-pip \
    wget \
    software-properties-common

# Install java
RUN add-apt-repository ppa:webupd8team/java
RUN apt-get install --no-install-recommends --no-install-suggests -y  \
    default-jre

# Install python packages
RUN pip install --upgrade pip
RUN pip install pandas

# Support for pycharm
RUN pip install setuptools

# Support for pyspark
#RUN pip install py4j==0.10.4
#RUN pip install py4j
RUN pip install findspark

##############################################################################
# Jupiter
##############################################################################

RUN apt-get install --no-install-recommends --no-install-suggests -y \
    ipython \
    ipython-notebook

#VOLUME /data

##############################################################################
# Install spark
##############################################################################

# Scala related variables.
ARG SCALA_VERSION=2.12.2
ARG SCALA_BINARY_ARCHIVE_NAME=scala-${SCALA_VERSION}
ARG SCALA_BINARY_DOWNLOAD_URL=http://downloads.lightbend.com/scala/${SCALA_VERSION}/${SCALA_BINARY_ARCHIVE_NAME}.tgz

# SBT related variables.
ARG SBT_VERSION=0.13.15
ARG SBT_BINARY_ARCHIVE_NAME=sbt-$SBT_VERSION
ARG SBT_BINARY_DOWNLOAD_URL=https://dl.bintray.com/sbt/native-packages/sbt/${SBT_VERSION}/${SBT_BINARY_ARCHIVE_NAME}.tgz

# Spark related variables.
ARG SPARK_VERSION=2.2.0
ARG SPARK_BINARY_ARCHIVE_NAME=spark-${SPARK_VERSION}-bin-hadoop2.7
ARG SPARK_BINARY_DOWNLOAD_URL=http://d3kbcqa49mib13.cloudfront.net/${SPARK_BINARY_ARCHIVE_NAME}.tgz

# Configure env variables for Scala, SBT and Spark.
# Also configure PATH env variable to include binary folders of Java, Scala, SBT and Spark.
ENV SCALA_HOME  /usr/local/scala
ENV JAVA_HOME   /usr/lib/jvm/java-1.8.0-openjdk-amd64
ENV SBT_HOME    /usr/local/sbt
ENV SPARK_HOME  /usr/local/spark
ENV PATH        $JAVA_HOME/bin:$SCALA_HOME/bin:$SBT_HOME/bin:$SPARK_HOME/bin:$SPARK_HOME/sbin:$PATH
ENV PYTHONPATH  $SPARK_HOME/python

# Download, uncompress and move all the required packages and libraries to their corresponding directories in /usr/local/ folder.
RUN apt-get -yqq update && \
    apt-get install -yqq vim screen tmux && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* && \
    rm -rf /tmp/* && \
    wget -qO - ${SCALA_BINARY_DOWNLOAD_URL} | tar -xz -C /usr/local/ && \
    wget -qO - ${SBT_BINARY_DOWNLOAD_URL} | tar -xz -C /usr/local/  && \
    wget -qO - ${SPARK_BINARY_DOWNLOAD_URL} | tar -xz -C /usr/local/ && \
    cd /usr/local/ && \
    ln -s ${SCALA_BINARY_ARCHIVE_NAME} scala && \
    ln -s ${SPARK_BINARY_ARCHIVE_NAME} spark && \
    cp spark/conf/log4j.properties.template spark/conf/log4j.properties && \
    sed -i -e s/WARN/ERROR/g spark/conf/log4j.properties && \
    sed -i -e s/INFO/ERROR/g spark/conf/log4j.properties

# We will be running our Spark jobs as `root` user.
USER root

# Working directory is set to the home folder of `root` user.
WORKDIR /root

# Expose ports for monitoring.
# SparkContext web UI on 4040 -- only available for the duration of the application.
# Spark master’s web UI on 8080.
# Spark worker web UI on 8081.
EXPOSE 4040 8080 8081

# Expose jupyter notebook
EXPOSE 55555

CMD ["/bin/bash"]
