from flask import Flask, render_template, request, redirect
import csv


def database_insert(data):
    with open("database.csv", mode="a") as database:
        email = data.get("email")
        subject = data.get("subject")
        message = data.get("message")
        csv_writer = csv.writer(database, lineterminator="\n", delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


class Server:
    def __init__(self):
        self._app = Flask(__name__)
        self._init__routes()

    def _init__routes(self):
        
        @self._app.route("/")
        def home():
            return render_template('index.html')
        @self._app.route("/<string:page_name>")
        def index(page_name):
            return render_template(page_name)

        @self._app.route("/contact", methods=["POST"])
        def contact():
            data = request.form.to_dict()
            database_insert(data)
            return redirect("/thankyou.html")

    def get_app(self):
        return self._app


app = Server().get_app()
