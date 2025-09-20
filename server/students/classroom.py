def classroom(roll, ip):
    from datetime import datetime, timedelta
    import sqlalchemy

    now = datetime.now()
    today = now.strftime("%A")
    today = "Monday"  # debug override

    ip_to_class = {
        "192.168.81": 'A',
        "192.168.82": 'B',
        "192.168.83": 'C',
        "192.168.84": 'D',
        "192.168.85": 'E',
        "192.168.86": 'F'
    }

    engine = sqlalchemy.create_engine('sqlite:///../attendance/days.db', echo=False)
    conn = engine.connect()
    result = conn.execute(sqlalchemy.text(f"SELECT * FROM {today} WHERE roll = '{roll}'"))
    row = result.fetchall()[0]

    roll = row[0]
    classes = row[1:]
    result_dict = {"roll": roll}

    current_class = None
    current_subject = None
    expected_class = None

    for i in range(0, len(classes), 4):
        class_num = (i // 4) + 1
        start_str, duration, name, subject = classes[i:i+4]

        result_dict[f"class{class_num}"] = {
            f"class{class_num}_start": start_str,
            f"class{class_num}_duration": duration,
            f"class{class_num}_name": name,
            "subject": subject
        }

        # check only if valid start/duration exist
        if start_str and duration:
            class_start = datetime.strptime(start_str, "%H:%M").replace(
                year=now.year, month=now.month, day=now.day
            )
            class_end = class_start + timedelta(minutes=int(duration))

            if class_start <= now <= class_end:
                # found the class!
                current_class = f"class{class_num}"
                current_subject = subject
                expected_class = name
                break  # stop after finding the current class ✅

    # IP-based class
    ip_class = ip_to_class.get(ip, "Unknown IP")

    print("All classes:", result_dict)
    print("Now:", now.strftime("%H:%M"))
    print("Current active class (by time):", current_class)
    print("Expected class from schedule:", expected_class)
    print("Subject:", current_subject)
    print("Class based on IP:", ip_class)

    return {
        "current_class": current_class,
        "current_subject": current_subject,
        "expected_class": expected_class,
        "ip_class": ip_class
    }
#classroom("02", "192.168.81")