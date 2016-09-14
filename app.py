'''
Created on Sep 13, 2016

@author: Rafael Carvalho (rafacarv@cisco.com)
'''

from flask import Flask, request
import json

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
            output = "a70d7d804074be01c63b2dc3385e6c3f0adc7fb1"
        
        else:
            secret = "thisshouldbechanged"
            output = "Post Received. See logs for JSON"
            #print (json.dumps(request.json, indent=4))
            print (json.dumps(request.json))

    except:
        output = "Error when dealing with {}".format(request.method)
    
    print (output)
    return (output)


if __name__ == '__main__':
    app.run()