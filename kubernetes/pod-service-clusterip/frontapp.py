from flask import Flask
from urllib.request import urlopen 


app = Flask(__name__)

@app.route('/')
def index():
    print("About to call backend...")

    with urlopen('http://backend:5000/api/quote-of-the-day') as r:
        quote_of_the_day = r.read().decode("utf-8")
    
    return f"""<h1>Hi there!</h1>
            <h2>Quote of the day: <i>{quote_of_the_day}</i></h2>
            """


if __name__ == '__main__':
    app.run(port=8080, use_reloader=False, host='0.0.0.0', debug=True)
