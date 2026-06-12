from flask import Flask, render_template_string

app = Flask(__name__)

news = [
    {
        "title": "Technology News",
        "content": "New AI technology is changing the world."
    },
    {
        "title": "Sports News",
        "content": "Local team wins the championship."
    },
    {
        "title": "Business News",
        "content": "Stock market shows positive growth."
    }
]

html = """
<!DOCTYPE html>
<html>
<head>
    <title>News Portal</title>
</head>
<body>
    <h1>📰 News Portal</h1>

    {% for item in news %}
    <div style="border:1px solid #ccc;padding:10px;margin:10px;">
        <h2>{{ item.title }}</h2>
        <p>{{ item.content }}</p>
    </div>
    {% endfor %}

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html, news=news)

if __name__ == "__main__":
    app.run(debug=True)