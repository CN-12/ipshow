from flask import Flask
import socket

app = Flask(__name__)

@app.route('/')
def ip():
    a = socket.gethostbyname(socket.gethostname())
    ipconfig = "당신의 IP는 " + a
    return "<h2>{}<h2>".format(ipconfig)

if __name__ == "__main__":
    app.run(debug=True)