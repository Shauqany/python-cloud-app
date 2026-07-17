from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def nyumbani():
    return "<h1>Mambo vipi Mkuu! Hii ni Python App yangu ya Kwanza kwenye Cloud! ulivyoni save mbele ongezea cloud engineer 🐍🚀</h1>"

if __name__ == "__main__":
    # Kwenye cloud tunatumia PORT inayotolewa na mfumo wa server
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
