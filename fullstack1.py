from flask import Flask, request

app = Flask(__name__)

# Sample internships
internships = [
    "Python Developer",
    "Web Developer",
    "Data Analyst"
]

applications = []

@app.route("/")
def home():
    html = "<h1>Internship Portal</h1>"

    for i, internship in enumerate(internships):
        html += f"""
        <p>{internship}
        <a href='/apply/{i}'>Apply</a></p>
        """

    html += "<br><a href='/applications'>View Applications</a>"
    return html


@app.route("/apply/<int:id>", methods=["GET", "POST"])
def apply(id):
    if request.method == "POST":
        name = request.form["name"]

        applications.append({
            "student": name,
            "internship": internships[id]
        })

        return "Application Submitted!"

    return """
    <h2>Apply for Internship</h2>

    <form method="post">
        Name:
        <input type="text" name="name" required>
        <button type="submit">Apply</button>
    </form>
    """


@app.route("/applications")
def view_applications():
    html = "<h2>Applications</h2>"

    for app_data in applications:
        html += f"""
        <p>
        {app_data['student']}
        applied for
        {app_data['internship']}
        </p>
        """

    return html


if __name__ == "__main__":
    app.run(debug=True)