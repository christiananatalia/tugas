from flask import Flask, render_template, redirect, send_from_directory, url_for, request
from werkzeug.utils import secure_filename
from AESCipher.aes import AESCipher
import os

#Untuk menjalankan web di .py
app = Flask(__name__)
app.config.from_object('config')

@app.route("/",methods=["GET","POST"])
def index():
    return render_template("index.html",title="File Encrypter")

@app.route("/upload",methods=["POST"])
def upload():
    file = request.files["files"]
    filename = os.path.join(app.config['UPLOAD_FOLDER'],secure_filename(file.filename))
    file.save(filename) 
    aes = AESCipher(filename)
    aes.encrypt()
    os.remove(filename)
    return redirect(url_for('download',filename=os.path.basename(aes.out_filename)))

@app.route("/flag")
def flag():
    flag_enc = os.path.join(app.config["CURRENT_PATH"],"AESCipher/example/")
    return send_from_directory(flag_enc,"flag_af864e91e69326efb355fc22ff44282a.txt.enc")

@app.route("/download/<path:filename>")
def download(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)





