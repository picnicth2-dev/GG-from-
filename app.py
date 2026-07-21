from flask import Flask, render_template_string
import os

app = Flask(__name__)

login_page = """
<!DOCTYPE html>
<html lang="th">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Ayano</title>

<style>

body{
    margin:0;
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    font-family:Arial,sans-serif;
    background:linear-gradient(135deg,#6dd5fa,#2980b9);
}

.box{
    width:350px;
    padding:40px;
    text-align:center;
    border-radius:20px;
    background:rgba(255,255,255,.18);
    backdrop-filter:blur(15px);
    box-shadow:0 10px 30px rgba(0,0,0,.25);
}

h1{
    color:white;
}

button{
    width:100%;
    padding:15px;
    margin-top:20px;
    border:none;
    border-radius:12px;
    cursor:pointer;
    font-size:18px;
    color:white;
    background:#1e88e5;
}

.credit{
    margin-top:20px;
    color:white;
    opacity:.8;
}

</style>

</head>

<body>

<div class="box">

<h1>ยินดีต้อนรับ</h1>

<form action="/home">
<button type="submit">
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

home_page = """
<!DOCTYPE html>
<html lang="th">
<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>หน้าหลัก</title>

<style>

body{

margin:0;
height:100vh;

display:flex;
justify-content:center;
align-items:center;

font-family:Arial,sans-serif;

background:linear-gradient(135deg,#6dd5fa,#2980b9);

}

.box{

width:350px;
padding:40px;

text-align:center;

border-radius:20px;

background:rgba(255,255,255,.18);

backdrop-filter:blur(15px);

box-shadow:0 10px 30px rgba(0,0,0,.25);

}

h2{

color:white;

}

a{

text-decoration:none;

}

button{

width:100%;
padding:15px;

margin-top:20px;

border:none;
border-radius:12px;

cursor:pointer;

font-size:18px;

color:white;

background:#43a047;

}

.credit{

margin-top:20px;
color:white;
opacity:.8;

}

</style>

</head>

<body>

<div class="box">

<h2>เลือกสิ่งที่ต้องการ</h2>

<a href="https://example.com" target="_blank">

<button>
เปิดเว็บไซต์
</button>

</a>

<br>

<a href="/">

<button style="background:#f57c00;">
กลับหน้าแรก
</button>

</a>

<div class="credit">

Created by Ayano

</div>

</div>

</body>
</html>
"""

@app.route("/")
def login():
    return render_template_string(login_page)

@app.route("/home")
def home():
    return render_template_string(home_page)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)