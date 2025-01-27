#!/usr/bin/env python3

from flask import Flask, render_template, request, redirect
import sqlite3, os


app = Flask(__name__)

@app.route("/",methods=["GET"])
def index():
    return render_template('index.html')

@app.route("/")
@app.route("/murder")
def murder():
    fid = request.args.get('id')
    conn = sqlite3.connect('murder.db')
    cursor = conn.cursor()
    cursor.execute("SELECT filename from crows WHERE id=(?)", fid)
    filename = cursor.fetchone()
    cursor.close()
    try:
        full_filename = f'static/{filename[0]}'
    except TypeError:
        #return render_template('index.html')
        return redirect("/")

    return render_template('murder.html', murder_image=full_filename)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

