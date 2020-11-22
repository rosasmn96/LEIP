from flask import Flask, render_template, request
import cx_Oracle
import os

app = Flask(__name__)

ispName = ""

@app.route('/isp', methods=['GET'])
def isp():
    return render_template('isp.html')

@app.route('/ispResult', methods=['POST'])
def ispPost():
    ispName = request.form['ispName']
    os.environ['PATH'] = '/Oracle/instantclient_19_8'
    os.environ['TNS_ADMIN'] = '/Users/madis/Documents/ITNS&SD Sem 10/Senior Design 1/Project/LEIP Database/Wallet'
    con = cx_Oracle.connect('ADMIN', 'L31P_P@$$-w0rd!', 'leip_high')
    cursor = con.cursor()
    ispRow = cursor.execute("SELECT * FROM ISP WHERE NAME = '" + ispName + "'").fetchone()
    return render_template('ispResult.html', ispRow=ispRow)    

if __name__ == "__main__":
    app.run()