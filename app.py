from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
<!DOCTYPE html>
<html lang="th">
<head>
    <meta charset="UTF-8">
    <title>อย่าเข้ามา</title>
    <style>
        body { background: radial-gradient(circle at center, #0a0a0a, #000); color: #ff1a1a; text-align: center; padding-top: 80px; animation: shake 0.15s infinite alternate; }
        h1 { font-size: 3em; text-shadow: 0 0 10px red; }
        @keyframes shake { from { transform: translateX(-1px); } to { transform: translateX(1px); } }
    </style>
</head>
<body>
    <h1>⚠️ ออกไปซะจีโน่เก ⚠️</h1>
    <p>ใครใช้ให้เข้ามา? จีโน่เกตัวพ่อ 😝</p>
</body>
</html>
"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
