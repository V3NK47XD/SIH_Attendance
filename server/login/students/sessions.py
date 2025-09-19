def sessioncreate(username):
    import random
    import string
    import sqlalchemy
    engine = sqlalchemy.create_engine('sqlite:///Databases/sessions.db', echo=True)
    conn = engine.connect()
    key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=32))
    conn.execute(sqlalchemy.text(f"INSERT INTO sessions (username, session_key) VALUES ('{username}', '{key}')"))
    conn.commit()
    return key

def sessioncheck(key):
    import sqlalchemy
    engine = sqlalchemy.create_engine('sqlite:///Databases/sessions.db', echo=True)
    conn = engine.connect()
    result = conn.execute(sqlalchemy.text(f"SELECT * FROM sessions WHERE session_key = '{key}'"))
    result=result.fetchall()
    if result == []:
        return False
    else:
        return True

def logout(key):
    import sqlalchemy
    engine = sqlalchemy.create_engine('sqlite:///Databases/sessions.db', echo=True)
    conn = engine.connect()
    conn.execute(sqlalchemy.text(f"DELETE FROM sessions WHERE session_key = '{key}'"))
    conn.commit()
    return "Logged out successfully."