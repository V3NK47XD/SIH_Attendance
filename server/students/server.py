import flask
from login import Login
from register import Register
import json
import sessions
import timetable_fetch
import classroom 
import photo_handle
from flask_cors import CORS

app = flask.Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
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

@app.route('/verify_class',methods=['POST'])
def classroom_page():
    ip = flask.request.remote_addr
    ip=str(ip)
    roll = flask.request.get_json()['name']
    print("IP Address:", ip)
    #ret = classroom.classroom(roll, ip)
    ret = classroom.classroom("02", "192.168.81")
    print(ret)
    return json.dumps(ret)

@app.route('/photo_upload',methods=['POST'])
def photo_upload():
    data = flask.request.get_json()
    dataURL = data['image']
    roll = data['name']
    #print(dataURL[0:30])  # Print the beginning of the data URL for verification
    result_face = photo_handle.face_compare(roll, dataURL)
    print(result_face)
    # Here, you would typically process and save the photo data
    return flask.jsonify({"message":result_face })

@app.route('/photo',methods=['GET'])
def photo():
    return flask.send_from_directory(app.static_folder, 'Pages/photo.html')
    

@app.route('/',methods=['GET'])
def index():
    return flask.send_from_directory(app.static_folder, 'nothing.html')

app.run(debug=True,port=6969,host="0.0.0.0",ssl_context=('server.crt', 'server.key'))
 