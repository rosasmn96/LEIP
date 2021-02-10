from flask import Flask, render_template, request
import cx_Oracle
import os
import array as arr

app = Flask(__name__, static_folder='C:\\LEIP\\app\\assets')

@app.route('/', methods=['GET'])
def home():
    return render_template('Home.html')

@app.route('/sexoffenderinfo', methods=['GET'])
def sexOffenderInfo():
    return render_template('SexOffender.html')

@app.route('/phonedirectory', methods=['GET'])
def phoneDirectory():
    os.environ['PATH'] = '/Oracle/instantclient_19_8'
    os.environ['TNS_ADMIN'] = '/Users/madis/Documents/ITNS&SD Sem 10/Senior Design 1/Project/LEIP Database/Wallet'
    con = cx_Oracle.connect('ADMIN', 'L31P_P@$$-w0rd!', 'leip_high')
    cursor = con.cursor()
    pdAgency = cursor.execute("SELECT agency FROM phonedirectory ORDER BY agency").fetchall()
    pdCounty = cursor.execute("SELECT county FROM phonedirectory ORDER BY agency").fetchall()
    pdTownship = cursor.execute("SELECT township FROM phonedirectory ORDER BY agency").fetchall()
    pdCincyPhoneDirectory = cursor.execute("SELECT cincinnati_phone_directory FROM phonedirectory ORDER BY agency").fetchall()
    pdPhoneNumber = cursor.execute("SELECT phone_number FROM phonedirectory ORDER BY agency").fetchall()
    return render_template('PhoneDirectory.html', pdAgency=pdAgency, pdCounty=pdCounty, pdTownship=pdTownship, pdCincyPhoneDirectory=pdCincyPhoneDirectory, pdPhoneNumber=pdPhoneNumber)
    

@app.route('/preservedigitalevidence', methods=['GET'])
def digitalEvidence():
    return render_template('Evidence.html')

@app.route('/isp', methods=['GET'])
def isp():
    return render_template('ISP.html')

@app.route('/ispResult', methods=['POST'])
def ispPost():
    ispName = request.form['ispName']
    os.environ['PATH'] = '/Oracle/instantclient_19_8'
    os.environ['TNS_ADMIN'] = '/Users/madis/Documents/ITNS&SD Sem 10/Senior Design 1/Project/LEIP Database/Wallet'
    con = cx_Oracle.connect('ADMIN', 'L31P_P@$$-w0rd!', 'leip_high')
    cursor = con.cursor()
    ispRow = cursor.execute("SELECT * FROM isp WHERE name = '" + ispName + "'").fetchone()
    return render_template('ISPResults.html', ispRow=ispRow)

if __name__ == '__main__':
    app.run()