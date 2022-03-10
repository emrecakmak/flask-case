from crypt import methods
from re import I
from aiohttp import request
from flask import Flask, request,jsonify,make_response
import logging,cfg,boto3


app = Flask(__name__)
logging.basicConfig(filename="./app/app/logs/logs.log", filemode="w", format="%(name)s -> %(levelname)s: %(message)s")

@app.route("/",methods=["GET"])
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
   
    try:
        if (action=="list"):
            aws_response=aws_client.describe_instances()
            ec2_Instances=aws_response["Reservations"]
            instanceId="InstanceIDs"
            ec2list=[]
            for i in ec2_Instances:
                ec2list.append(i["Instances"][0]["InstanceId"])
            response = make_response(
                jsonify(instanceId=ec2list),
                200,)
            logging.critical("List Returned.")     
            return response             

        elif (action=="start"):
            insID=aws_data["InstanceId"]
            aws_response=aws_client.start_instances(InstanceIds=[insID])
            status="status"
            response = make_response(
                jsonify(status=aws_response["StartingInstances"][0]["CurrentState"]["Name"]),
                200,)
            logging.critical("Instances Started.")     
            return response

        elif (action=="stop"):
            insID=aws_data["InstanceId"]
            aws_response=aws_client.stop_instances(InstanceIds=[insID])
            status="status"
            response = make_response(
                jsonify(status=aws_response["StoppingInstances"][0]["CurrentState"]["Name"]),
                200,)
            logging.critical("Instances Stopped.")
            return response        
        
        else:
            logging.critical("Undefined action detected")
            return make_response("Undefined action.",400)
    except Exception as e:
        return make_response(str(e),412)

if __name__ == "__main__":
    app.run(host=cfg.config["hostname"], port=cfg.config["port"],debug=True)