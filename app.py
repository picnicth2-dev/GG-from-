from flask import Flask, request, render_template_string, redirect, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

app.secret_key = "ayano_secret_key"



# =====================
# DATABASE
# =====================

def database():

    conn = sqlite3.connect("users.db")

    cur = conn.cursor()


    cur.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
    """)


    cur.execute("""
    CREATE TABLE IF NOT EXISTS data(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        content TEXT
    )
    """)


    conn.commit()

    conn.close()



database()



# =====================
# STYLE
# =====================

style="""

<style>

body{

height:100vh;
display:flex;
justify-content:center;
align-items:center;

background:
linear-gradient(135deg,#74c0fc,#228be6);

font-family:Arial;

}


.box{

width:90%;
max-width:360px;

background:white;

padding:30px;

border-radius:20px;

text-align:center;

box-shadow:0 10px 30px #555;

}



input{

width:100%;

padding:14px;

margin:8px 0;

border-radius:10px;

border:1px solid #ccc;

}


button{

width:100%;

padding:14px;

margin-top:10px;

border:none;

border-radius:10px;

background:#1976d2;

color:white;

font-size:17px;

}


a{

text-decoration:none;

color:#1976d2;

}

</style>

"""



# =====================
# LOGIN
# =====================


login_page=f"""

<html>

<head>

<meta name="viewport"
content="width=device-width,initial-scale=1">

{style}

</head>


<body>


<div class="box">


<h2>
Login
</h2>


<form method="post">


<input name="username"
placeholder="ชื่อผู้ใช้">


<input name="password"
type="password"
placeholder="รหัสผ่าน">


<button>
เข้าสู่ระบบ
</button>


</form>


<br>

<a href="/register">
สมัครสมาชิก
</a>


</div>


</body>

</html>

"""




# =====================
# REGISTER
# =====================


register_page=f"""

<html>

<head>

<meta name="viewport"
content="width=device-width,initial-scale=1">

{style}

</head>


<body>


<div class="box">


<h2>
สมัครสมาชิก
</h2>


<form method="post">


<input name="username"
placeholder="ชื่อผู้ใช้">


<input name="password"
type="password"
placeholder="รหัสผ่าน">


<button>
สมัคร
</button>


</form>


<a href="/">
กลับหน้า Login
</a>


</div>


</body>

</html>

"""




# =====================
# HOME
# =====================


home_page=f"""

<html>

<head>

<meta name="viewport"
content="width=device-width,initial-scale=1">

{style}

</head>


<body>


<div class="box">


<h2>
สวัสดี {{user}}
</h2>


<form method="post">


<input name="content"
placeholder="บันทึกข้อมูล">


<button>
บันทึก
</button>


</form>


<a href="/logout">
ออกจากระบบ
</a>


</div>


</body>

</html>

"""



# =====================
# ROUTES
# =====================



@app.route("/",methods=["GET","POST"])
def login():

    if request.method=="POST":


        username=request.form["username"]

        password=request.form["password"]



        conn=sqlite3.connect("users.db")

        cur=conn.cursor()


        cur.execute(
        "SELECT password FROM users WHERE username=?",
        (username,)
        )


        user=cur.fetchone()


        conn.close()



        if user and check_password_hash(
            user[0],
            password
        ):


            session["user"]=username


            return redirect("/home")



    return render_template_string(login_page)





@app.route("/register",methods=["GET","POST"])
def register():

    if request.method=="POST":


        username=request.form["username"]

        password=generate_password_hash(
            request.form["password"]
        )


        try:

            conn=sqlite3.connect("users.db")

            cur=conn.cursor()


            cur.execute(
            "INSERT INTO users(username,password) VALUES(?,?)",
            (username,password)
            )


            conn.commit()

            conn.close()


            return redirect("/")

        except:


            return "ชื่อผู้ใช้นี้มีแล้ว"



    return render_template_string(register_page)





@app.route("/home",methods=["GET","POST"])
def home():


    if "user" not in session:

        return redirect("/")



   