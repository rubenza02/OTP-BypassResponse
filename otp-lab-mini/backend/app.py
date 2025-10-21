from flask import Flask, request, jsonify

app = Flask(__name__)

# Al arrancar, solo existe este OTP válido (laboratorio)
VALID_USER = "alice"
VALID_OTP = "123456"

@app.route("/verify_otp", methods=["POST"])
def verify_otp():
    """
    Recibe JSON: {"user":"...", "otp":"..."}
    - Si coincide con (alice, 123456) => 200 {"result":"ok"}
    - Si no => 404 {"error":"invalid"}
    """
    data = request.get_json(force=True, silent=True) or {}
    user = (data.get("user") or "").strip()
    otp  = (data.get("otp")  or "").strip()

    if user == VALID_USER and otp == VALID_OTP:
        return jsonify({"result": "ok"}), 200

    return jsonify({"error": "invalid"}), 404

@app.route("/")
def root():
    return "OTP Minimal Backend OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
