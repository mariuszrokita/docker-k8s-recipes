import os
from flask import Flask


app = Flask(__name__)

@app.route('/api/quote-of-the-day')
def index():
    return os.environ.get("QUOTE_OF_THE_DAY", "Have fun!")


if __name__ == '__main__':
    app.run(port=5000, use_reloader=False, host='0.0.0.0', debug=True)