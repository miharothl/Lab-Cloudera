docker run \
       -v ~/scm:/scm -v ~/data:/data \
       --hostname=quickstart.cloudera \
       --privileged=true -t -i \
       -p:8888:8888 -p:7180:7180 -p:80:80 \
       cloudera/quickstart /usr/bin/docker-quickstart
