from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    number = request.args.get("number", "")
    if number:
        double = doubling(number)
    else:
        double = ""

    return (
        """<form action="" method="get">
                <input type="text" name="number">
                <input type="submit" value="Apply">
            </form>"""
        + "Double: The new version"
        + double
    )

def doubling(number):
    try:
        double = int(number) * 2
        return str(double)

    except ValueError:
        return "invalid input"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
