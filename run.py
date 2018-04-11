import sqlite3 as sql
from flask import Flask, render_template,redirect,url_for

app = Flask(__name__)

@app.route('/')
def index():
     conn = sql.connect("light.db")
     cur = conn.cursor()
     val = cur.execute("select * from status")
     val = str(cur.fetchone())[2:-3]
     print(val)
     cur.close()
     conn.close()
     return render_template("invol.html",flag=val)

@app.route('/switchh')
def switchh():
     conn = sql.connect("light.db")
     cur = conn.cursor()
     val = cur.execute("select * from status")
     val = str(cur.fetchone())[2:-3]
     if val=="1":
          cur.execute("update status set flag = '0'")
          conn.commit()
     elif val=="0":
          cur.execute("update status set flag = '1'")
          conn.commit()
     cur.close()
     conn.close()
     return redirect(url_for('index'));

if __name__=='__main__':
     app.run(debug=True)
