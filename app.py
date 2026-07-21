from flask import Flask, render_template_string, request

app = Flask(__name__)


# =========================
# หน้า Login
# =========================

login_page = """

<!DOCTYPE html>
<html lang="th">

<head>

<meta charset="UTF-8">

<title>Ayano Login</title>

<style>

body{
    height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    background:linear-gradient(135deg,#74c0fc,#228be6);
    font-family:Arial;
}

.box{
    background:white;
    padding:40px;
    border-radius:20px;
    text-align:center;
    width:300px;
    box-shadow:0 10px 30px #555;
}

button{

    width:100%;
    padding:15px;
    border:none;
    border-radius:10px;
    background:#1976d2;
    color:white;
    font-size:18px;
    cursor:pointer;

}

</style>

</head>


<body>


<div class="box">

<h1>
ยินดีต้อนรับ
</h1>


<form action="/home">

<button>
เข้าสู่ระบบ
</button>

</form>


<p>
Created by Ayano
</p>


</div>


</body>

</html>

"""


# =========================
# หน้าหลัก
# =========================

home_page = """

<!DOCTYPE html>
<html lang="th">


<head>

<meta charset="UTF-8">

<title>Ayano Home</title>


<style>

body{

height:100vh;
display:flex;
justify-content:center;
align-items:center;
background:#74c0fc;
font-family:Arial;

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
border-radius:10px;
border:1px solid #ccc;

}


button{

padding:12px 30px;
margin-top:15px;
background:#1976d2;
color:white;
border:none;
border-radius:10px;
cursor:pointer;

}


</style>


</head>


<body>


<div class="box">


<h2>
กรอกชื่อ
</h2>


<form method="post">


<input
name="text"
placeholder="ใส่ชื่อของคุณ">


<br>


<button>
บันทึก
</button>


</form>


<p>
{{result}}
</p>


</div>


</body>


</html>

"""


# =========================
# หน้าตัวเลือก
# =========================


menu_page = """

<!DOCTYPE html>

<html lang="th">


<head>

<meta charset="UTF-8">

<title>Menu</title>


<style>


body{

height:100vh;
display:flex;
justify-content:center;
align-items:center;
background:linear-gradient(135deg,#74c0fc,#228be6);
font-family:Arial;

}


.box{

background:white;
padding:40px;
border-radius:20px;
text-align:center;

}


button{

width:250px;
padding:15px;
margin:10px;
border:none;
border-radius:10px;
background:#1976d2;
color:white;
font-size:18px;
cursor:pointer;

}


</style>


</head>


<body>


<div class="box">


<h2>
เลือกเมนู
</h2>



<form action="/open">

<button>
เปิดเว็บไซต์
</button>

</form>




<form action="/home">

<button>
กลับหน้าหลัก
</button>

</form>



</div>


</body>


</html>

"""



# =========================
# ระบบทำงาน
# =========================


@app.route("/")
def login():

    return render_template_string(login_page)



@app.route("/home", methods=["GET","POST"])
def home():

    result = ""


    if request.method == "POST":

        name = request.form["text"]

        return render_template_string(menu_page)


    return render_template_string(
        home_page,
        result=result
    )



@app.route("/open")
def open_web():

    return """
    <script>
    window.location.href="https://zefoy.com/";
    </script>
    """



if __name__ == "__main__":

    app.run(debug=True)