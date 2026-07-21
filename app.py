from flask import Flask, render_template_string, request

app = Flask(__name__)


# หน้า Login
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
}

button{
    width:100%;
    padding:15px;
    border:none;
    border-radius:10px;
    background:#1976d2;
    color:white;
    font-size:18px;
}

</style>

</head>

<body>

<div class="box">

<h1>ยินดีต้อนรับ</h1>

<form action="/home">

<button>
เข้าสู่ระบบ
</button>

</form>

</div>

</body>
</html>
"""


# หน้า Home
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
name="text"
placeholder="พิมพ์ข้อมูล">


<br><br>


<button>
บันทึก
</button>


</form>


<p>

{{ result }}

</p>


</div>


</body>

</html>

"""


@app.route("/")
def login():

    return render_template_string(login_page)



@app.route("/home", methods=["GET","POST"])
def home():

    result = ""

    if request.method == "POST":

        data = request.form["text"]

        result = "คุณบันทึก: " + data


    return render_template_string(
        home_page,
        result=result
    )



if __name__ == "__main__":

    app.run(debug=True)