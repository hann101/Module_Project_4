FROM ubuntu:latest
  
RUN apt-get update
RUN apt-get install python3 -y 
RUN apt-get install git -y
RUN apt-get install pip -y
RUN git clone https://github.com/hann101/team4_output.git
RUN pip install flask
RUN pip install flask_migrate
RUN pip install flask_wtf
RUN pip install email_validator
RUN pip install pymongo
RUN boto3
RUN pyspark
RUN findspark

WORKDIR /team4_output/mybide_output



CMD ["python3", "start_app.py"]

EXPOSE 5000
