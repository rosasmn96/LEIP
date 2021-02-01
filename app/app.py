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
    contactAgencies = (cursor.execute("SELECT AGENCY FROM PHONEDIRECTORY").fetchall())
    contactCounties = (cursor.execute("SELECT COUNTY FROM PHONEDIRECTORY").fetchall())
    contactTownships = (cursor.execute("SELECT TOWNSHIP FROM PHONEDIRECTORY").fetchall())
    contactCincyDirectories = (cursor.execute("SELECT CINCINNATI_PHONE_DIRECTORY FROM PHONEDIRECTORY").fetchall())
    contactNumbers = (cursor.execute("SELECT PHONE_NUMBER FROM PHONEDIRECTORY").fetchall())
    return render_template('PhoneDirectory.html', contactAgencies=contactAgencies, contactCounties=contactCounties, contactTownships=contactTownships, contactCincyDirectories=contactCincyDirectories, contactNumbers=contactNumbers)

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
    ispRow = cursor.execute("SELECT * FROM ISP WHERE NAME = '" + ispName + "'").fetchone()
    return render_template('ISPResults.html', ispRow=ispRow)

if __name__ == '__main__':
    app.run()