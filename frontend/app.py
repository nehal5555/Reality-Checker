from flask import Flask, render_template, request

app = Flask(__name__)

# Dummy function to simulate news verification
def verify_news(text):
    # Replace this with a real news verification API or logic
    if "real" in text.lower():
        return "Real News"
    elif "false" in text.lower():
        return "False News"
    else:
        return "Unable to Verify"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        user_input = request.form.get("user_input")
        result = verify_news(user_input)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)