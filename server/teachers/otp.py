from flask import Flask, request, jsonify
from flask_cors import CORS
import pyotp

app = Flask(__name__)
app.static_folder = './Static'
CORS(app)
# Random secret key (store per user in real apps)
SECRET = pyotp.random_base32()
print(f"Secret key: {SECRET}")

@app.route('/generate_otp', methods=['GET'])
def generate_otp():
    totp = pyotp.TOTP(SECRET, interval=300, digits=4)  # 4-digit OTP, 30 sec expiry
    otp = totp.now()
    return jsonify({"otp": otp, "valid_for_seconds": 300})

@app.route('/otp_page', methods=['GET'])
def otp_page():
    return app.send_static_file('generate.html')

@app.route('/verify_otp', methods=['POST'])
def verify_otp():
    data = request.json
    otp = data.get('otp')
    totp = pyotp.TOTP(SECRET, interval=300, digits=4)
    if totp.verify(otp):
        return jsonify({"status": "success", "message": "OTP is valid!"})
    else:
        return jsonify({"status": "fail", "message": "OTP is invalid or expired!"})

if __name__ == "__main__":
    app.run(debug=True,port=7979,host="0.0.0.0")
