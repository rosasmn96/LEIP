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
    os.environ['PATH'] = '/Oracle/instantclient_19_8'
    os.environ['TNS_ADMIN'] = '/Users/madis/Documents/ITNS&SD Sem 10/Senior Design 1/Project/LEIP Database/Wallet'
    con = cx_Oracle.connect('ADMIN', 'L31P_P@$$-w0rd!', 'leip_high')
    cursor = con.cursor()
    ispName = cursor.execute("SELECT name FROM isp ORDER BY name").fetchall()
    return render_template('ISP.html', ispName=ispName)

@app.route('/ispresult', methods=['POST'])
def ispPost():
    ispIndex = int(request.form['ispIndex'])
    os.environ['PATH'] = '/Oracle/instantclient_19_8'
    os.environ['TNS_ADMIN'] = '/Users/madis/Documents/ITNS&SD Sem 10/Senior Design 1/Project/LEIP Database/Wallet'
    con = cx_Oracle.connect('ADMIN', 'L31P_P@$$-w0rd!', 'leip_high')
    cursor = con.cursor()
    ispNameColumn = cursor.execute("SELECT name FROM isp ORDER BY name").fetchall()
    ispName = ''.join(ispNameColumn[ispIndex])
    ispContact = ''.join(cursor.execute("SELECT contact_or_attn FROM isp WHERE name='" + ispName + "'").fetchone())
    ispLocation = ''.join(cursor.execute("SELECT location FROM isp WHERE name='" + ispName + "'").fetchone())
    ispFaxNumber = ''.join(cursor.execute("SELECT fax_number FROM isp WHERE name='" + ispName + "'").fetchone())
    ispEmail = ''.join(cursor.execute("SELECT email FROM isp WHERE name='" + ispName + "'").fetchone())
    ispInfo = ''.join(cursor.execute("SELECT info FROM isp WHERE name='" + ispName + "'").fetchone())
    ispLastUpdated = ''.join(cursor.execute("SELECT last_updated FROM isp WHERE name='" + ispName + "'").fetchone())
    ispLEGuide = ''.join(cursor.execute("SELECT le_guide FROM isp WHERE name='" + ispName + "'").fetchone())
    ispTimeZone = ''.join(cursor.execute("SELECT time_zone FROM isp WHERE name='" + ispName + "'").fetchone())
    return render_template('ISPResults.html', ispName=ispName, ispContact=ispContact, ispLocation=ispLocation, ispFaxNumber=ispFaxNumber, ispEmail=ispEmail, ispInfo=ispInfo, ispLastUpdated=ispLastUpdated, ispLEGuide=ispLEGuide, ispTimeZone=ispTimeZone)

if __name__ == '__main__':
    app.run()