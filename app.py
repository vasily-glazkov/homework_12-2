from flask import Flask, request, render_template, send_from_directory
from main.view import main
from loader.view import loader

app = Flask(__name__)

app.register_blueprint(main)
app.register_blueprint(loader)

if __name__ == "__main__":
    app.run(debug=True)
