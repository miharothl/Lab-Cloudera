# Goal

Run pyspark in docker container using IDE pycharm with code completion and debug support.

## Prerequisites

* [Install Pycharm 2017.3.4 Professional Edition](https://www.jetbrains.com/)
* [Install Docker](https://www.docker.com/)
* Go to docker advanced settings and adjust computing resources available to docker
  * CPUs: 4
  * Memory 8GB
* Assuming the your source code repositories are in `~/scm` and your data is in `~/data`
 

Verified on Mac, it should work on Windows.

## Instructions
 
* Build and run the docker container
  * `./build.sh`
  * (optional) `./run.sh`
  * (optional) In the container start pyspark
  
* Start pycharm and open `debug-pyspark.py`
* Add remote docker python interpreter
* Add data volume by editing Run configuration settings
* Start debugging

## Jupyter Notebook (optional)

  * `./run.sh`
  * In the container start ipython notebook `ipython notebook --port=55555 --no-browser --ip=0.0.0.0`
  * On the host navigate to [notebook] (http://localhost:55555)
  