import bcrypt
from database.db import execute_query, insert_query


def hash_password(password):
    return bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()


def verify_password(password, hashed):
    return bcrypt.checkpw(
        password.encode(),
        hashed.encode()
    )


def register_user(name, email, password, role):

    existing = execute_query(
        "SELECT * FROM users WHERE email=?",
        (email,)
    )

    if existing:
        return False

    hashed_password = hash_password(password)

    insert_query(
        """
        INSERT INTO users
        (full_name,email,password,role)
        VALUES (?,?,?,?)
        """,
        (
            name,
            email,
            hashed_password,
            role
        )
    )

    return True


def login_user(email, password):

    user = execute_query(
        "SELECT * FROM users WHERE email=?",
        (email,)
    )

    if not user:
        return None

    user = user[0]

    if verify_password(password, user["password"]):
        return user

    return None