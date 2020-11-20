from flask import Flask, render_template, request
import cx_Oracle
import os
import pandas

ispName = ""

app = Flask(__name__)

def ispdb():
    os.environ['PATH'] = '/Oracle/instantclient_19_8'
    os.environ['TNS_ADMIN'] = '/Users/madis/Documents/ITNS&SD Sem 10/Senior Design 1/Project/LEIP Database/Wallet'
    con = cx_Oracle.connect('ADMIN', 'L31P_P@$$-w0rd!', 'leip_high')
    cursor = con.cursor()
    cursor.execute("SELECT * FROM ISP WHERE NAME = 'Apple Inc'")
    ispdata = pandas.DataFrame(cursor.fetchall())
    print(ispdata)

ispdb()

#@app.route('/isp')
#def isp():
    #if request.method == "POST":
        #ispName = request.form['ispName']
        
   # return render_template('isp.html')

#if __name__ == "__main__":
    #app.run()