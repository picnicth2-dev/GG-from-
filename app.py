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

style = """

<style>

*{
box-sizing:border-box;
font-family:Arial;
}


body{

min-height:100vh;

display:flex;

justify-content:center;

align-items:center;

padding:20px;

background:
linear-gradient(135deg,#74c0fc,#228be6);

}



.box{

width:100%;

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

font-size:16px;

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

color:#1976d2;

text-decoration:none;

}


.card{

background:#eee;

padding:12px;

margin:10px 0;

border-radius:10px;

}


</style>

"""



# =====================
# LOGIN PAGE
# =====================

login_page = f"""

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
# REGISTER PAGE
# =====================

register_page = f"""

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


<br>


<a href="/">
กลับหน้า Login
</a>


</div>


</body>

</html>

"""





# =====================
# LOGIN
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



        if user:


            if check_password_hash(
                user[0],
                password
            ):


                session["user"]=username


                return redirect("/home")


            else:

                return "รหัสผ่านผิด"



        else:

            return "ไม่พบผู้ใช้"



    return render_template_string(login_page)






# =====================
# REGISTER
# =====================


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





# =====================
# HOME
# =====================


@app.route("/home",methods=["GET","POST"])
def home():


    if "user" not in session:

        return redirect("/")



    conn=sqlite3.connect("users.db")

    cur=conn.cursor()



    if request.method=="POST":


        content=request.form["content"]


        cur.execute(

        "INSERT INTO data(username,content) VALUES(?,?)",

        (

        session["user"],

        content

        )

        )


        conn.commit()




    cur.execute(

    "SELECT id,content FROM data WHERE username=?",

    (session["user"],)

    )


    datas=cur.fetchall()


    conn.close()



    items=""


    for d in datas:


        items += f"""

        <div class="card">

        {d[1]}

        <br>

        <a href="/delete/{d[0]}">
        ลบ
        </a>

        </div>

        """



    return render_template_string(f"""

    <html>

    <head>

    <meta name="viewport"
    content="width=device-width,initial-scale=1">

    {style}

    </head>


    <body>


    <div class="box">


    <h2>
    สวัสดี {session["user"]}
    </h2>



    <form method="post">


    <input name="content"
    placeholder="ข้อมูลที่ต้องการบันทึก">


    <button>
    บันทึก
    </button>


    </form>


    <hr>


    <h3>
    ข้อมูลของฉัน
    </h3>


    {items}



    <a href="/logout">
    ออกจากระบบ
    </a>


    </div>


    </body>

    </html>

    """)





# =====================
# DELETE
# =====================


@app.route("/delete/<int:id>")
def delete(id):


    if "user" not in session:

        return redirect("/")



    conn=sqlite3.connect("users.db")

    cur=conn.cursor()



    cur.execute(

    "DELETE FROM data WHERE id=? AND username=?",

    (

    id,

    session["user"]

    )

    )


    conn.commit()

    conn.close()



    return redirect("/home")





# =====================
# LOGOUT
# =====================


@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")





if __name__=="__main__":

    app.run(debug=True)