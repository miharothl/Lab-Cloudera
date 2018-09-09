FROM centos:7

# Install R
RUN yum install -y epel-release
RUN yum install -y R

# Install Rstudio
RUN yum install -y \
  wget -y \
  initscripts

RUN wget https://download2.rstudio.org/rstudio-server-rhel-1.1.453-x86_64.rpm
RUN yum install -y \
  rstudio-server-rhel-1.1.453-x86_64.rpm

RUN useradd rstudio
RUN echo 'rstudio' | passwd rstudio --stdin

# Cleanup
RUN rm rstudio-server-rhel-1.1.453-x86_64.rpm

# Entrypoint
USER root
WORKDIR /root
ENTRYPOINT rstudio-server start && bash
