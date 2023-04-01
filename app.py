from flask import Flask, render_template, request, url_for
import mysql.connector as sqltor
import pickle

model = pickle.load(open('model.pkl', 'rb'))

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    mycon = sqltor.connect(host="localhost", user="root",
                           password="Akash20032006", database="cia")
    cursor = mycon.cursor()
    cursor.execute("select * from users")
    db_user = ""
    db_pwd = ""
    for i in cursor:
        db_user = i[1]
        db_pwd = i[2]
    username = request.form["username"]
    password = request.form["password"]
    if username == db_user and password == db_pwd:
        return render_template("success.html")
    else:
        return render_template("failure.html")


@app.route("/classify", methods=["POST"])
def classify():
    features = [float(i) for i in (request.form.values())]
    pred = model.predict([features])
    pred_val = ""
    if pred == [0]:
        pred_val = "Iris setosa"
    elif pred == [1]:
        pred_val = "Iris virginica"
    elif pred == [2]:
        pred_val = "Iris versicolor"

    return render_template("predict.html", data=pred_val)


if __name__ == "__main__":
    app.run(debug=True)
