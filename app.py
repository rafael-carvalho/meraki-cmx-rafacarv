from flask import Flask, request

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
            output = "cdc34455d960baa0981d7d19f31b3a3923dfbda6"
        
        else:
            secret = "thisshouldbechanged"
            output = "{}".format(request.json)
    except:
        output = "Error when dealing with {}".format(request.method)
    
    
    print (output)
    return (output)


if __name__ == '__main__':
    app.run()