from flask import Flask, request, render_template_string, redirect

app = Flask(__name__)

projects = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Project Management SaaS</title>
</head>
<body>
    <h1>Project Management SaaS</h1>

    <form method="POST" action="/add">
        <input type="text" name="project" placeholder="Project Name" required>
        <button type="submit">Add Project</button>
    </form>

    <h2>Projects</h2>
    <ul>
    {% for project in projects %}
        <li>{{ project }}</li>
    {% endfor %}
    </ul>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, projects=projects)

@app.route("/add", methods=["POST"])
def add_project():
    project_name = request.form["project"]
    projects.append(project_name)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)