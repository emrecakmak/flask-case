from crypt import methods
from aiohttp import request
from flask import Flask, request
import logging,cfg,boto3


app = Flask(__name__)
logging.basicConfig(filename="./logs/logs.log", filemode="w", format="%(name)s -> %(levelname)s: %(message)s")

@app.route("/")
def index():
    return "Welcome to EC2 Manager!"

@app.route("/ec2/<action>",methods=["POST"])
def ec2action(action):

    aws_data=request.get_json()
    aws_client=boto3.client('ec2',
        region_name=aws_data["region_name"],
        aws_access_key_id=aws_data["aws_access_key_id"],
        aws_secret_access_key=aws_data["aws_secret_access_key"] 
    ) 
    aws_response=aws_client.describe_instances()
    ec2_Instances=aws_response["Reservations"][0]["Instances"]
    logging.critical("AWS Client Created")

    if (action=="list"):
        ic_id=ec2_Instances[0]["InstanceId"]
        logging.critical("InstanceId returned")
        return ic_id
    elif (action=="start"):
        return ""
    elif (action=="stop"):
        return ""
    else:
        return "Undefined action."

if __name__ == "__main__":
    app.run(host=cfg.config["hostname"], port=cfg.config["port"],debug=True)