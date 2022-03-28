from flask import Flask, request, render_template, send_from_directory
from main.view import main
from loader.view import loader
import logging

logging.basicConfig(filename="log.txt", encoding='utf-8', level=logging.INFO)

app = Flask(__name__)

app.register_blueprint(main)
app.register_blueprint(loader)


@app.route("/uploads/images/<path:path>")
def static_dir(path):
    return send_from_directory("uploads/images", path)


if __name__ == "__main__":
    app.run(debug=True)
