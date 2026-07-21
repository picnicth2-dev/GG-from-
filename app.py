from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Ayano</title>

<style>
*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:Arial,sans-serif;
}

body{
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    background:linear-gradient(135deg,#7dd3fc,#60a5fa,#3b82f6);
}

.card{
    width:350px;
    padding:40px;
    text-align:center;

    background:rgba(255,255,255,.18);
    backdrop-filter:blur(18px);
    border-radius:20px;
    box-shadow:0 10px 30px rgba(0,0,0,.25);
}

h1{
    color:white;
    margin-bottom:30px;
    font-size:32px;
}

button{
    width:100%;
    padding:15px;
    border:none;
    border-radius:12px;
    font-size:18px;
    cursor:pointer;
    color:white;
    background:linear-gradient(90deg,#38bdf8,#2563eb);
    transition:.3s;
}

button:hover{
    transform:scale(1.03);
}

.credit{
    margin-top:25px;
    color:white;
    opacity:.85;
    font-size:14px;
}
</style>

</head>

<body>

<div class="card">

<h1>ยินดีต้อนรับ</h1>

<form action="/home">
<button>
เข้าสู่ระบบ
</button>
</form>

<div class="credit">
Created by Ayano
</div>

</div>

</body>
</html>
"""

HOME = """
<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Home</title>

<style>

body{
    margin:0;
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    background:linear-gradient(135deg,#7dd3fc,#60a5fa,#3b82f6);
    font-family:Arial,sans-serif;
}

.box{
    width:400px;
    text-align:center;
    padding:40px;
    border-radius:20px;
    background:rgba(255,255,255,.18);
    backdrop-filter:blur(18px);
    box-shadow:0 10px 30px rgba(0,0,0,.25);
}

h1{
    color:white;
    margin-bottom:25px;
}

button{

padding:14px 28px;
font-size:17px;
border:none;
border-radius:12px;
cursor:pointer;

background:#ffffff;
color:#2563eb;

}

.credit{

margin-top:30px;
color:white;
opacity:.85;

}

</style>

</head>

<body>

<div class="box">

<h1>เข้าสู่เว็บไซต์สำเร็จ 🎉</h1>

<button onclick="location.href='/'">
กลับหน้าแรก
</button>

<div class="credit">
Created by Ayano
</div>

</div>

</body>

</html>
"""

@app.route("/")
def login():
    return render_template_string(HTML)

@app.route("/home")
def home():
    return render_template_string(HOME)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)