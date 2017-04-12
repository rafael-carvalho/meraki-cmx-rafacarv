'''
Created on Sep 13, 2016

@author: Rafael Carvalho (rafacarv@cisco.com)
'''

from flask import Flask, request
import json
from boto.s3.connection import S3Connection

app = Flask(__name__)


@app.route('/')
def hello():
    """Run your server and go browse to the root of your server and see if it is working. It shows the message Hello Meraki World!"""
    return "Hello Meraki World!"

@app.route('/meraki', methods=['GET', 'POST'])
def meraki():
    output = "No response"
    try:
        if (request.method == "GET"):
            validator = S3Connection(os.environ['validator'])
            output = validator
        
        else:
            secret = S3Connection(os.environ['validator'])
            output = "Post Received. See logs for JSON"
            print (json.dumps(request.json, indent=2))
            #print (json.dumps(request.json))

    except:
        output = "Error when dealing with {}".format(request.method)
    
    print (output)
    return (output)


if __name__ == '__main__':
    app.run()