from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher

app = Flask(__name__)
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caeser_encrypt():
    data = request.json
    print(f"Received data: {data}")
    if not data:
        return jsonify({"error": "Missing JSON body"}), 400

    plain_text = data.get('plain_text')
    key = data.get('key')

    if plain_text is None or key is None:
        return jsonify({"error": "Missing plain_text or key"}), 400

    encrypt_text = caesar_cipher.encrypt_text(plain_text, int(key))
    return jsonify({'encrypt_message': encrypt_text})


@app.route("/api/caesar/decrypt", methods=["POST"])
def caeser_decrypt():
    data = request.json
    print(f"Received data: {data}")
    if not data:
        return jsonify({"error": "Missing JSON body"}), 400

    cipher_text = data.get('cipher_text')
    key = data.get('key')

    if cipher_text is None or key is None:
        return jsonify({"error": "Missing cipher_text or key"}), 400

    decrypt_text = caesar_cipher.decrypt_text(cipher_text, int(key))
    return jsonify({'decrypt_message': decrypt_text})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)