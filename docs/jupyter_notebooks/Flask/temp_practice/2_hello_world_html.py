from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("2_hello_world.html")

app.run(port="8080")