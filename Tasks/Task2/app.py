from flask import Flask, render_template, request
import config

app = Flask(__name__)

@app.route("/add", methods=["GET", "POST"])
def add_feedback():
    """
    This route handles feedback submission.
    GET  -> Displays the feedback form
    POST -> Processes the submitted feedback
    """
    if request.method == "POST":
        name = request.form.get("name")
        message = request.form.get("message")

        # For now, just print (later you can store in DB)
        print(f"Name: {name}")
        print(f"Message: {message}")

        return "Feedback submitted"

    return render_template("add_feedback.html")


if __name__ == "__main__":
    app.run(port=5000, debug=config.DEBUG)