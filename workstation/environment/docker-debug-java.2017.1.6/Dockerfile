FROM openjdk:8-jre

# change directory to where the app will live
WORKDIR /usr/local/playground/

# install the jars
COPY target/*.jar ./

EXPOSE 50505


#CMD ["/bin/bash"]
#CMD ["java", \
#    "-agentlib:jdwp=transport=dt_socket,address=50505,suspend=n,server=y", \
#    "-cp", \
#    "docker-debug-java-1.0-SNAPSHOT.jar", \
#    "main.java.Main"]
###
##java -agentlib:jdwp=transport=dt_socket,address=50505,suspend=n,server=y -cp docker-debug-java-1.0-SNAPSHOT.jar main.java.Main





