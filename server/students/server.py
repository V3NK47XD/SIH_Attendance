import flask
from login import Login
from register import Register
import json
import sessions
import timetable_fetch

app = flask.Flask(__name__)
app.static_folder = './Static'

@app.route('/login',methods=['GET'])
def login():
    return flask.send_from_directory(app.static_folder, 'login.html')

@app.route('/register',methods=['GET'])
def register():
    return flask.send_from_directory(app.static_folder, 'register.html')

@app.route('/loginbackend',methods=['POST'])
def loginbackend():
    global sendStatus
    data = flask.request.get_json()
    print("\n",data)
    sendStatus = Login(data['username'], data['password'])
    statusjson = json.dumps({"session_key": sendStatus[0], "message": sendStatus[1]})
    return statusjson

@app.route('/registerbackend',methods=['POST'])
def registerbackend():
    global sendStatus
    data = flask.request.get_json()
    print("\n",data)
    sendStatus = Register(data['username'], data['password'])
    return sendStatus

@app.route('/logout',methods=['GET'])
def logoutpage():
    return flask.send_from_directory(app.static_folder, 'logout.html')

@app.route('/logoutbackend',methods=['POST'])
def logoutbackend():
    data = flask.request.get_json()
    print("\n",data)
    session_key = data['session_key']
    sessions.logout(session_key)
    return "Logged out successfully."

@app.route('/sessioncheck',methods=['POST'])
def sessioncheck():
    key=flask.request.get_data().decode('utf-8')
    print("Key :", key )
    session_exists = sessions.sessionchecker(key)
    print("Session :", session_exists)
    if session_exists:
        return session_exists
    else:
        return "0"

@app.route('/middle',methods=['GET'])
def middle():
    return flask.send_from_directory(app.static_folder, 'Pages/middle.html')

@app.route('/otp',methods=['GET'])
def otp():
    return flask.send_from_directory(app.static_folder, 'Pages/otp_input.html')

@app.route('/timetable',methods=['GET'])
def timetable():
    return flask.send_from_directory(app.static_folder, 'Pages/timetable.html')

@app.route('/timetable_api',methods=['POST'])
def timetable_api():
    fetch_json = flask.request.get_json()
    timetable_data = timetable_fetch.get_data(fetch_json['roll'], fetch_json['day'])
    return timetable_data

@app.route('/',methods=['GET'])
def index():
    return flask.send_from_directory(app.static_folder, 'nothing.html')

app.run(debug=True,port=6969,host="0.0.0.0")
 