import os
from flask import Flask


app = Flask(__name__)

@app.route('/')
def index():
    dish_name = os.environ.get("DISH_NAME", "-")

    extra_dish_password = os.environ.get("EXTRA_DISH_PASSWORD", "")

    # Sometimes, the password is not the password itself, but the name of the file containing password
    if ".txt" in extra_dish_password:
        with open(extra_dish_password, 'r') as f:
            extra_dish_password = f.read()

    return f"""<h1>Welcome to the restaurant!</h1>
               <h2>Today, a dish of the day is: {dish_name}</h2>
               <h2>Show that password: <i>{extra_dish_password}</i> to the waiter to get something extra</h2>"""


if __name__ == '__main__':
    app.run(port=5000, use_reloader=False, host='0.0.0.0', debug=True)
