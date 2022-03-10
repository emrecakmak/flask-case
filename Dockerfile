FROM python:3.8-slim-buster

WORKDIR /app

ADD requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

RUN mkdir -p ./app/app/logs \
    && touch ./app/app/logs/logs.log \
    && chmod 660 ./app/app/logs/logs.log
EXPOSE 8080

CMD ["python3","/app/app/ec2_manager.py"]