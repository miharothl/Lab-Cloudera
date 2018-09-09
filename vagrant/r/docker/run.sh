docker run -it \
  -p 8787:8787 \
  -v ~/scm:/home/rstudio/scm \
  -v ~/data:/home/rstudio/data \
  rserver
