from flask import Flask


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route("/")
def hello():
    """Return a friendly HTTP greeting.

    Returns:
        A string with the words 'Hello World!'.
    """
    return "a(2)+b(3)=5"


if __name__ == "__main__":
   
    app.run(host="127.0.0.1", port=8080, debug=True)
