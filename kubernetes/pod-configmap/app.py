import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    dish_name = os.environ.get("DISH_NAME", "-")

    return f"""<h1>Welcome to the restaurant!</h1>
               <h2>Today, a dish of the day is: {dish_name}"""


if __name__ == '__main__':
    app.run(port=5000, use_reloader=False, host='0.0.0.0', debug=True)
