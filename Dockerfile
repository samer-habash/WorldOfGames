FROM python:alpine3.9
#Copied all the directory
COPY / ./worldofgames-docker
WORKDIR /worldofgames-docker
RUN pip3 install -r /worldofgames-docker/requirements.txt
#Run Flask
CMD ["python" , "/worldofgames-docker/MainScores.py"]
