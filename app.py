from flask import Flask, render_template_string
import os

app = Flask(__name__)

login_page = """
<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Login</title>

<style>
body {
    margin: 0;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #ff9a9e, #fad0c4, #fad0c4);
}

.box {
    background: rgba(255, 255, 255, 0.25);
    backdrop-filter: blur(10px);
    padding: 50px;
    border-radius: 25px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.2);
}

button {
    width: 80px;
    height: 80px;
    border-radius: 50%;
    border: none;
    font-size: 2rem;
    cursor: pointer;
    background: linear-gradient(135deg, #ff4d94, #ff8fb1);
    color: white;
    transition: transform 0.3s;
}

button:hover {
    transform: scale(1.1);
}
</style>
</head>

<body>
    <div class="box">
        <form action="/inside">
            <button type="submit">➡️</button>
        </form>
    </div>
</body>
</html>
"""

inside_page = """
<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<title>Inside</title>
<style>
body {
    margin: 0;
    height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #667eea, #764ba2);
}

h1 {
    color: white;
    font-size: 5rem;
}
</style>
</head>
<body>
    <h1>ควย</h1>
</body>
</html>
"""

@app.route("/")
def login():
    return render_template_string(login_page)

@app.route("/inside")
def inside():
    return render_template_string(inside_page)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)