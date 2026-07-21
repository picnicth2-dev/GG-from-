from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def login():
    return render_template("login.html")


@app.route("/home", methods=["GET", "POST"])
def home():

    message = ""

    if request.method == "POST":
        data = request.form["data"]
        message = "บันทึกข้อมูลแล้ว: " + data

    return render_template(
        "home.html",
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)
<!DOCTYPE html>
<html lang="th">

<head>
<meta charset="UTF-8">

<title>Login</title>

<style>

body{
background:#4dabf7;
height:100vh;
display:flex;
justify-content:center;
align-items:center;
font-family:Arial;
}


.box{

background:white;
padding:40px;
border-radius:20px;
text-align:center;

}


button{

background:#1976d2;
color:white;
border:none;
padding:15px 40px;
border-radius:10px;
font-size:18px;

}

</style>

</head>


<body>


<div class="box">

<h1>Ayano</h1>

<form action="/home">

<button>
เข้าสู่ระบบ
</button>

</form>

</div>


</body>

</html>
<!DOCTYPE html>
<html lang="th">

<head>

<meta charset="UTF-8">

<title>Home</title>


<style>

body{

background:#74c0fc;
font-family:Arial;
height:100vh;
display:flex;
justify-content:center;
align-items:center;

}


.box{

background:white;
padding:40px;
border-radius:20px;
text-align:center;

}


input{

padding:12px;
width:250px;

}


button{

padding:12px 30px;
background:#1976d2;
color:white;
border:none;
border-radius:10px;

}

</style>


</head>


<body>


<div class="box">


<h2>
หน้าหลัก
</h2>


<form method="post">


<input 
name="data"
placeholder="กรอกข้อมูล">


<br><br>


<button>
บันทึก
</button>


</form>


<p>

{{ message }}

</p>


</div>


</body>

</html>