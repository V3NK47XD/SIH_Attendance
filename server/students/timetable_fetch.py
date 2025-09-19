
def get_data(roll,day):
    import sqlalchemy
    import json
    engine = sqlalchemy.create_engine('sqlite:///../attendance/days.db', echo=True)
    conn = engine.connect()
    result = conn.execute(sqlalchemy.text(f"SELECT * FROM {day} WHERE roll = '{roll}'"))
    result = result.fetchall()
    print(result)
    # unpack tuple
    row = result[0]

    # first element is roll
    roll = row[0]

    # remaining are grouped in 4s (start, duration, name, subject)
    classes = row[1:]
    result = {"roll": roll}

    for i in range(0, len(classes), 4):
        class_num = (i // 4) + 1
        result[f"class{class_num}"] = {
            f"class{class_num}_start": classes[i],
            f"class{class_num}_duration": classes[i+1],
            f"class{class_num}_name": classes[i+2],
            "subject": classes[i+3]
        }

    # pretty JSON
    json_result = json.dumps(result, indent=4)
    print(json_result)

    return json_result