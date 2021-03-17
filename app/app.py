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
    pdAgency = cursor.execute("SELECT agency FROM phonedirectory ORDER BY agency, cincinnati_phone_directory").fetchall()
    pdCounty = cursor.execute("SELECT county FROM phonedirectory ORDER BY agency, cincinnati_phone_directory").fetchall()
    pdTownship = cursor.execute("SELECT township FROM phonedirectory ORDER BY agency, cincinnati_phone_directory").fetchall()
    pdCincyPhoneDirectory = cursor.execute("SELECT cincinnati_phone_directory FROM phonedirectory ORDER BY agency, cincinnati_phone_directory").fetchall()
    pdPhoneNumber = cursor.execute("SELECT phone_number FROM phonedirectory ORDER BY agency, cincinnati_phone_directory").fetchall()
    return render_template('PhoneDirectory.html', pdAgency=pdAgency, pdCounty=pdCounty, pdTownship=pdTownship, pdCincyPhoneDirectory=pdCincyPhoneDirectory, pdPhoneNumber=pdPhoneNumber)
    

@app.route('/preservedigitalevidence', methods=['GET'])
def digitalEvidence():
    return render_template('Evidence.html')

@app.route('/isp', methods=['GET', 'POST'])
def isp():
    httpMethod = 'GET'
    os.environ['PATH'] = '/Oracle/instantclient_19_8'
    os.environ['TNS_ADMIN'] = '/Users/madis/Documents/ITNS&SD Sem 10/Senior Design 1/Project/LEIP Database/Wallet'
    con = cx_Oracle.connect('ADMIN', 'L31P_P@$$-w0rd!', 'leip_high')
    cursor = con.cursor()
    ispNames = cursor.execute("SELECT name FROM isp ORDER BY name").fetchall()
    ispName = 'Apple Inc'
    ispContact = cursor.execute("SELECT contact_or_attn FROM isp WHERE name='" + ispName + "'").fetchone()
    ispLocation = cursor.execute("SELECT location FROM isp WHERE name='" + ispName + "'").fetchone()
    ispFaxNumber = cursor.execute("SELECT fax_number FROM isp WHERE name='" + ispName + "'").fetchone()
    ispEmail = cursor.execute("SELECT email FROM isp WHERE name='" + ispName + "'").fetchone()
    ispInfo = cursor.execute("SELECT info FROM isp WHERE name='" + ispName + "'").fetchone()
    ispLastUpdated = cursor.execute("SELECT last_updated FROM isp WHERE name='" + ispName + "'").fetchone()
    ispLEGuide = cursor.execute("SELECT le_guide FROM isp WHERE name='" + ispName + "'").fetchone()
    ispTimeZone = cursor.execute("SELECT time_zone FROM isp WHERE name='" + ispName + "'").fetchone()
    if request.method == 'POST':
        httpMethod = 'POST'
        ispIndex = int(request.form['ispIndex'])
        ispName = ''.join(ispNames[ispIndex])
        ispContact = cursor.execute("SELECT contact_or_attn FROM isp WHERE name='" + ispName + "'").fetchone()
        if ispContact == (None,):
            ispContact = 'N/A'
        else:
            ispContact = ''.join(ispContact)
        ispLocation = cursor.execute("SELECT location FROM isp WHERE name='" + ispName + "'").fetchone()
        if ispLocation == (None,):
            ispLocation = 'N/A'
        else:
            ispLocation = ''.join(ispLocation)
        ispFaxNumber = cursor.execute("SELECT fax_number FROM isp WHERE name='" + ispName + "'").fetchone()
        if ispFaxNumber == (None,):
            ispFaxNumber = 'N/A'
        else:
            ispFaxNumber = ''.join(ispFaxNumber)
        ispEmail = cursor.execute("SELECT email FROM isp WHERE name='" + ispName + "'").fetchone()
        if ispEmail == (None,):
            ispEmail = 'N/A'
        else:
            ispEmail = ''.join(ispEmail)
        ispInfo = cursor.execute("SELECT info FROM isp WHERE name='" + ispName + "'").fetchone()
        if ispInfo == (None,):
            ispInfo = 'N/A'
        else:
            ispInfo = ''.join(ispInfo)
        ispLastUpdated = cursor.execute("SELECT last_updated FROM isp WHERE name='" + ispName + "'").fetchone()
        if ispLastUpdated == (None,):
            ispLastUpdated = 'N/A'
        else:
            ispLastUpdated = ''.join(ispLastUpdated)
        ispLEGuide = cursor.execute("SELECT le_guide FROM isp WHERE name='" + ispName + "'").fetchone()
        if ispLEGuide == (None,):
            ispLEGuide = 'N/A'
        else:
            ispLEGuide = ''.join(ispLEGuide)
        ispTimeZone = cursor.execute("SELECT time_zone FROM isp WHERE name='" + ispName + "'").fetchone()
        if ispTimeZone == (None,):
            ispTimeZone = 'N/A'
        else:
            ispTimeZone = ''.join(ispTimeZone)
    return render_template('ISP.html', httpMethod=httpMethod, ispNames=ispNames, ispName=ispName, ispContact=ispContact, ispLocation=ispLocation, ispFaxNumber=ispFaxNumber, ispEmail=ispEmail, ispInfo=ispInfo, ispLastUpdated=ispLastUpdated, ispLEGuide=ispLEGuide, ispTimeZone=ispTimeZone)

if __name__ == '__main__':
    app.run()