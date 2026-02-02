
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
            margin: 0;
            /* จัดกึ่งกลางหน้าจอแบบสมบูรณ์ */
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            overflow: hidden;
            animation: shake 0.15s infinite alternate;
        }

        h1 {
            font-size: 8em; /* ขนาดใหญ่ยักษ์ */
            margin: 0;
            text-shadow: 0 0 20px red, 0 0 50px darkred;
            animation: glitch 1s infinite;
        }

        p {
            color: #ddd;
            font-size: 2em;
            margin-top: 20px;
        }

        .warning {
            margin-top: 40px;
            color: crimson;
            font-size: 1.2em;
            animation: blink 1.2s infinite;
        }

        @keyframes glitch {
            0% { transform: translate(0); }
            20% { transform: translate(-3px, 3px); }
            40% { transform: translate(3px, -3px); }
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
    <h1>จีโน่เป็นเกย์</h1>
    <p>อ่านทำไมอ่านไปเขาก็ไม่กลับมารักหรอก😝</p>
    <div class="warning">ระบบกำลังจับตาดูคุณอยู่...</div>
</body>
</html>
"""

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host='0.0.0.0', port=port)
