from flask import Flask, render_template_string

app = Flask(__name__)

freelancers = [
    {"name": "Kavin", "skill": "Python Developer"},
    {"name": "Arun", "skill": "Web Designer"},
    {"name": "Priya", "skill": "Graphic Designer"}
]

html = """
<!DOCTYPE html>
<html>
<head>
    <title>Freelancer Marketplace</title>
</head>
<body>
    <h1>Freelancer Marketplace</h1>

    <h2>Available Freelancers</h2>

    <ul>
    {% for freelancer in freelancers %}
        <li>
            <b>{{ freelancer.name }}</b> - {{ freelancer.skill }}
        </li>
    {% endfor %}
    </ul>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html, freelancers=freelancers)

if __name__ == "__main__":
    app.run(debug=True)