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
    body {
        background: radial-gradient(circle at center, #0a0a0a, #000);
        color: #ff1a1a;
        font-family: 'Segoe UI', sans-serif;
        text-align: center;
        padding-top: 80px;
        overflow: hidden;
        animation: shake 0.15s infinite alternate;
    }
    h1 {
        font-size: 3em;
        text-shadow: 0 0 10px red, 0 0 30px darkred;
        animation: glitch 1s infinite;
    }
    p {
        color: #ddd;
        font-size: 1.3em;
        margin-top: 20px;
        text-shadow: 0 0 5px black;
    }
    .warning {
        margin-top: 40px;
        color: crimson;
        font-size: 1.1em;
        animation: blink 1.2s infinite;
    }
    @keyframes glitch {
        0% { transform: translate(0); }
        20% { transform: translate(-2px, 2px); }
        40% { transform: translate(2px, -2px); }
        60% { transform: translate(-1px, 1px); }
        80% { transform: translate(1px, -1px); }
        100% { transform: translate(0); }
    }
    @keyframes blink {
        0%, 100% { opacity: 1; }
        50% { opacity: 0; }
    }
    @keyframes shake {
        from { transform: translateX(-1px); }
        to { transform: translateX(1px); }
    }
</style>
</head>
<body>
    <h1>⚠️ ออกไปซะ ⚠️</h1>
    <p>ใครใช้ให้เข้ามา?</p>
    <p>ที่นี่ไม่ใช่ที่ของแก 😑</p>
    <div class="warning">
        ระบบกำลังจับตาดูการเคลื่อนไหวของคุณ...
    </div>
</body>
</html>
"""

if __name__ == "__main__":
    # กำหนด Port ให้ตรงกับที่ Render ต้องการ
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
