FROM python:3.8-slim-buster

WORKDIR /app

ADD requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

RUN mkdir -p ./app/logs \
    && touch ./app/logs/logs.log \
    && chmod 660 ./app/logs/logs.log

EXPOSE 3000

CMD ["python3","/app/app/ec2_manager.py"]
