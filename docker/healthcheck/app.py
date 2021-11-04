from flask import Flask, jsonify, redirect, Response, url_for

app = Flask(__name__)

# A flag that deterrmines whether the app should start becoming unresponsive/unhealthy.
# This is very useful while playing around with the DOCKER HEALTHCHECK command.
is_healthy = True

@app.route('/')
def index():
    if is_healthy:
        return "<h1>Hello world</h1>"
    else:
        raise Exception("Intentional application crash")

# This should be an endpoint reacting for the POST HTTP request.
# But for simplicity sake, it reacts on GET HTTP.
@app.route('/start-failing')
def start_app_failing():
    global is_healthy
    is_healthy = False
    return "<h1>The app will become unhealthy, it will start crashing every time...</h1>"


@app.route('/health')
def health():
    # Choose simulation version for healthiness
    # Option 1:
    # Healthy or unhealthy state depends on a value of the variable.
    #if is_healthy:

    # Option 2:
    # Always healthy. It may cause a situation that the main application URL fails,
    # but the app is still considered healthy.
    #if True:

    # Option 3:
    # The most realistic - check the response status for the main application URL.
    # In other words - service marks itself as unhealthy, when the main application address
    # does not work.
    _ = index()  # Pretend we're accessing the main application URL
    status = {
        "success": True,
        "message": "It is working fine!"
    }
    return jsonify(status)


if __name__ == '__main__':
    app.run(port=5000, use_reloader=False, host='0.0.0.0', debug=True)
