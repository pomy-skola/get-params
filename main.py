from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello, World!"


@app.route("/vzhled")
def vzhled():
    color_theme = request.args.get("theme", "light")
    if color_theme not in ["light", "dark"]:
        color_theme = "light"
    
    return render_template("vzhled.html", color_theme=color_theme)


if __name__ == '__main__':
    app.run(debug=True)
