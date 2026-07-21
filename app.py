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
font-family:Arial,sans-serif;
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

box-shadow:0 10px 30px rgba(0,0,0,.3);

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

cursor:pointer;

}



.message{

padding:12px;

border-radius:10px;

margin-bottom:15px;

}



.error{

background:#ffd6d6;

color:#c00000;

border:1px solid #ff8080;

}



.success{

background:#d6ffd9;

color:#008000;

border:1px solid #70d670;

}



.card{

background:#eeeeee;

padding:12px;

margin:10px 0;

border-radius:10px;

}



a{

color:#1976d2;

text-decoration:none;

}


</style>

"""