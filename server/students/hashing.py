
def hash(password):
    import bcrypt
    # Hash the password using bcrypt
    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed.decode('utf-8')