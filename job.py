from flask import Flask, render_template_string

app = Flask(__name__)

jobs = [
    {"title": "Python Developer", "company": "ABC Tech"},
    {"title": "Web Designer", "company": "XYZ Solutions"},
    {"title": "Data Analyst", "company": "Data Corp"}
]

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Job Portal</title>
</head>
<body>
    <h1>Job Portal</h1>

    <h2>Available Jobs</h2>

    <ul>
    {% for job in jobs %}
        <li>
            <b>{{ job.title }}</b> - {{ job.company }}
        </li>
    {% endfor %}
    </ul>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, jobs=jobs)

if __name__ == "__main__":
    app.run(debug=True)