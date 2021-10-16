FROM python

##create directory "app" and then "cd app"
WORKDIR /app

##copy requirements to image
COPY requirements.txt .

##install requirements to image
RUN pip install -r requirements.txt

##copy python code to docker image
COPY main.py .

##run python code in the docker image
CMD ["python","/app/main.py"]
