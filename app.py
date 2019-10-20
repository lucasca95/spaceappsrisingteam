from flask import Flask

app = Flask (__name__)

@app.route('/', methods=['POST'])
def index():
    return "Server andando2"

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5555)