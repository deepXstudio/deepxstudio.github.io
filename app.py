# app.py
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/getmsg/', methods=['GET'])
def respond():
    # Retrieve the name from url parameter
    name = request.args.get("name", None)

    # For debugging
    print(f"got name {name}")

    response = {}

    # Check if user sent a name at all
    if not name:
        response["ERROR"] = "no name found, please send a name."
    # Check if the user entered a number not a name
    elif str(name).isdigit():
        response["ERROR"] = "name can't be numeric."
    # Now the user entered a valid name
    else:
        response["MESSAGE"] = f"Welcome {name} to our awesome platform!!"

    # Return the response in json format
    return jsonify(response)

@app.route('/post/', methods=['POST'])
def post_something():
    param = request.form.get('name')
    print(param)
    # You can add the test cases you made in the previous function, but in our case here you are just testing the POST functionality
    if param:
        return jsonify({
            "Message": f"Welcome {name} to our awesome platform!!",
            # Add this option to distinct the POST request
            "METHOD" : "POST"
        })
    else:
        return jsonify({
            "ERROR": "no name found, please send a name."
        })

# A welcome message to test our server
@app.route('/')
def index():
    return "<h1>Welcome to our server !!</h1>"

@app.route('/lichvannien_privacy_policy.html')
def lichvannien_privacy_policy():
    return open('lichvannien_privacy_policy.html').read()

@app.route('/word-lock_privacy_policy.html')
def wordlock_privacy_policy():
    return open('word-lock_privacy_policy.html').read()

@app.route('/palm_test_privacy_policy.html')
def palm_test_privacy_policy():
    return open('palm_test_privacy_policy.html').read()

@app.route('/palmistry_privacy_policy.html')
def palmistry_privacy_policy():
    return open('palmistry_privacy_policy.html').read()
    
@app.route('/astro_master_privacy_policy.html')
def astro_master_privacy_policy():
    return open('astro_master_privacy_policy.html').read()

@app.route('/thuocloban_privacy_policy.html')
def thuocloban_privacy_policy():
    return open('thuocloban_privacy_policy.html').read()

@app.route('/comix_privacy_policy.html')
def comix_privacy_policy():
    return open('comix_privacy_policy.html').read()

@app.route('/sketchx_privacy_policy.html')
def sketchx_privacy_policy():
    return open('sketchx_privacy_policy.html').read()

@app.route('/timewarpscan_privacy_policy.html')
def timewarpscan_privacy_policy():
    return open('timewarpscan_privacy_policy.html').read()

from flask import Response
@app.route('/app-ads.txt')
def app_ads():
    return Response(open('app-ads.txt', 'r').read(), mimetype='text/plain')
    # return open('app-ads.txt', 'r').read()

if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

