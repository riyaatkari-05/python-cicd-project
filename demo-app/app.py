from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Jenkins CI/CD deployment successful!",
        "application": "Positive Number Checker"
    })


@app.route("/check/<int:number>")
def check_number(number):
    return jsonify({
        "number": number,
        "result": "Positive" if number > 0 else (
            "Negative" if number < 0 else "Zero"
        )
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)