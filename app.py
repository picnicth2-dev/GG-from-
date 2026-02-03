from flask import Flask, render_template_string, redirect, url_for

app = Flask(__name__)

login_page = """
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
    <style>
        body {
            height: 100vh;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(135deg, #6a11cb, #2575fc, #00c9ff);
            font-family: Arial, sans-serif;
        }
        .box {
            background: rgba(255,255,255,0.15);
            padding: 40px;
            border-radius: 20px;
            text-align: center;
            color: white;
            box-shadow: 0 0 20px rgba(0,0,0,0.3);
        }
        button {
            margin-top: 20px;
            padding: 12px 30px;
            border: none;
            border-radius: 30px;
            font-size: 16px;
            cursor: pointer;
            background: linear-gradient(135deg, #ff758c, #ff7eb3);
            color: white;
        }
        button:hover {
            opacity: 0.85;
        }
    </style>
</head>
<body>
    <div class="box">
        <h2>ยินดีต้อนรับ</h2>
        <form action="/inside">
            <button type="submit">เข้าสู่ระบบเพื่อดูสิ่งที่ดีกว่า</button>
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
            height: 100vh;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            background: linear-gradient(135deg, #11998e, #38ef7d);
            font-family: Arial, sans-serif;
        }
        .box {
            background: rgba(0,0,0,0.25);
            padding: 40px;
            border-radius: 20px;
            text-align: center;
            color: white;
        }
        button {
            margin-top: 20px;
            padding: 10px 25px;
            border: none;
            border-radius: 25px;
            cursor: pointer;
            background: #ffffff;
            color: #11998e;
            font-size: 15px;
        }
    </style>
</head>
<body>
    <div class="box">
        <h1>นี่คือหน้าลับ 😎</h1>
        <button onclick="location.reload()">รีเฟรตหน้า</button>
    </div>
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
    app.run(debug=True)