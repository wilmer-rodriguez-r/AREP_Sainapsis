from flask import Flask, render_template
import model
app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/openai/<query>")
def search(query):
    return model.execute(query)

if __name__ == "__main__":
    app.run(debug=True)
