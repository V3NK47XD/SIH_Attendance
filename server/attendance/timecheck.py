import sqlalchemy
import flask

app = flask.Flask(__name__)

@app.route('/timetable', methods=['GET'])
def timetable():
    return flask.send_from_directory('Static', 'timetable.html')


@app.route('/timecheck', methods=['GET'])
def timecheck():
    engine = sqlalchemy.create_engine('sqlite:///Databases/classrooms.db', echo=True)
    conn = engine.connect()
    
    result = conn.execute(sqlalchemy.text("SELECT * FROM classrooms"))
    result = result.fetchall()
    conn.close()
    
    return flask.jsonify([dict(row) for row in result])

app.run(debug=True, port=8989, host="0.0.0.0")