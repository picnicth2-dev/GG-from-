from flask import Flask, render_template_string, request

app = Flask(__name__)


style = """
<style>

*{
    margin:0;
    padding:0;
    box-sizing:border-box;
    font-family:'Arial',sans-serif;
}


body{

    min-height:100vh;
    display:flex;
    justify-content:center;
    align-items:center;
    padding:20px;

    background:
    linear-gradient(135deg,
    #74c0fc,
    #228be6);

}


/* กล่องหลัก */

.box{

    width:100%;
    max-width:360px;

    padding:30px 25px;

    background:
    rgba(255,255,255,0.20);

    backdrop-filter:blur(15px);

    border-radius:25px;

    text-align:center;

    box-shadow:
    0 15px 40px rgba(0,0,0,.25);

    animation:
    show .5s ease;

}


@keyframes show{

from{

opacity:0;
transform:translateY(30px);

}

to{

opacity:1;
transform:translateY(0);

}

}



h1,h2{

color:white;

margin-bottom:25px;

font-size:28px;

}



/* ช่องกรอก */

input{

width:100%;

padding:15px;

border:none;

outline:none;

border-radius:15px;

font-size:16px;

margin-bottom:15px;

}



/* ปุ่ม */

button{

width:100%;

padding:15px;

border:none;

border-radius:15px;

background:#1976d2;

color:white;

font-size:18px;

font-weight:bold;

cursor:pointer;

margin-top:10px;

transition:.2s;

}



button:active{

transform:scale(.95);

}



.credit{

color:white;

margin-top:20px;

font-size:14px;

opacity:.8;

}



</style>
"""



# =====================
# LOGIN
# =====================


login_page = f"""

<!DOCTYPE html>

<html>

<head>

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>Ayano</title>

{style}

</head>


<body>


<div class="box">


<h1>
Ayano
</h1>


<h2>
ยินดีต้อนรับ
</h2>


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



# =====================
# HOME
# =====================


home_page = f"""

<!DOCTYPE html>

<html>

<head>

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>Home</title>

{style}

</head>


<body>


<div class="box">


<h2>
กรอกชื่อ
</h2>


<form method="post">


<input
name="name"
placeholder="ชื่อของคุณ">


<button>
บันทึก
</button>


</form>



</div>


</body>


</html>

"""



# =====================
# MENU
# =====================


menu_page = f"""

<!DOCTYPE html>

<html>

<head>

<meta name="viewport"
content="width=device-width, initial-scale=1.0">

<title>Menu</title>

{style}

</head>


<body>


<div class="box">


<h2>
เลือกเมนู
</h2>


<form action="/open">

<button>

🌐 เปิดเว็บไซต์

</button>

</form>



<form action="/home">

<button>

🏠 กลับหน้าหลัก

</button>

</form>



</div>


</body>


</html>

"""



@app.route("/")
def login():

    return render_template_string(login_page)



@app.route("/home", methods=["GET","POST"])
def home():

    if request.method=="POST":

        return render_template_string(menu_page)


    return render_template_string(home_page)



@app.route("/open")
def open_web():

    return """
    <script>
    window.location.href="https://zefoy.com/";
    </script>
    """



if __name__=="__main__":

    app.run(debug=True)