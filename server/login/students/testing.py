
def Register(username, password):
    import sqlalchemy
    engine = sqlalchemy.create_engine('sqlite:///Databases/login.db', echo=True)
    conn = engine.connect()
    # Check if the username already exists
    result = conn.execute(sqlalchemy.text(f"SELECT * FROM logins WHERE username = '{username}'"))
    result=result.fetchall()
    if result != []:
        return "Username already exists. Please choose a different username."
    else:
        conn.execute(sqlalchemy.text(f"INSERT INTO logins (username, password) VALUES ('{username}', '{password}')"))
    conn.commit()
