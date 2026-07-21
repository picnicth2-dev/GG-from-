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
    background:linear-gradient(135deg,#74c0fc,#4dabf7,#228be6);
}

.box{
    width:360px;
    padding:40px;
    text-align:center;
    border-radius:20px;
    background:rgba(255,255,255,.18);
    backdrop-filter:blur(15px);
    box-shadow:0 10px 30px rgba(0,0,0,.25);
}

h1{
    color:white;
    margin-bottom:25px;
}

button{
    width:100%;
    padding:15px;
    border:none;
    border-radius:12px;
    cursor:pointer;
    font-size:18px;
    color:white;
    background:#1976d2;
}

.credit{
    margin-top:20px;
    color:white;
    opacity:.85;
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
background:linear-gradient(135deg,#74c0fc,#4dabf7,#228be6);
}

.box{
width:400px;
padding:35px;
border-radius:20px;
background:rgba(255,255,255,.18);
backdrop-filter:blur(15px);
box-shadow:0 10px 30px rgba(0,0,0,.25);
text-align:center;
}

h2{
color:white;
margin-bottom:20px;
}

input{
width:100%;
padding:14px;
border:none;
border-radius:10px;
margin-bottom:20px;
font-size:16px;
}

button{
width:100%;
padding:14px;
border:none;
border-radius:10px;
font-size:17px;
cursor:pointer;
background:#1976d2;
color:white;
margin-top:10px;
}

.credit{
margin-top:20px;
color:white;
opacity:.85;
}

</style>

</head>

<body>

<div class="box">

<h2>ใส่ลิงก์เพื่อเปิดเว็บไซต์</h