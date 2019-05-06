from flask import Flask
from flask import send_file

app = Flask(__name__)

@app.route("/")
def home():
    return send_file("wip.jpeg", mimetype='image/gif')

if __name__ == "__main__":
    app.run(debug=True)
