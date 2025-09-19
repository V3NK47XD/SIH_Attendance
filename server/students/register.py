
def Register(username, password):
    import sqlalchemy
    engine = sqlalchemy.create_engine('sqlite:///Databases/login.db', echo=True)
    conn = engine.connect()
    
    result = conn.execute(sqlalchemy.text(f"SELECT * FROM logins WHERE username = '{username}'"))
    result=result.fetchall()
    if result != []:
        conn.close()
        return "Username already exists. Please choose a different username."
    else:
        from hashing import hash
        hashed = hash(password)
        conn.execute(sqlalchemy.text(f"INSERT INTO logins (username, password) VALUES ('{username}', '{hashed}')"))
    conn.commit()
    conn.close()
    return "Registration successful"