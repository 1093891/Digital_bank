import os
import mysql.connector as mysql


def _connect_to_database():
    # Connect to the MySQL database

    connection = mysql.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        user=os.getenv('DB_USER', 'root'),
        password=os.getenv('DB_PASSWORD', '0000'),
        database=os.getenv('DB_NAME', 'digitall_bank'),
        port=int(os.getenv('DB_PORT', 3306))
    )
    return connection


def get_users():
    connection = None
    cursor = None
    try:
        connection = _connect_to_database()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users")
        users = cursor.fetchall()
        return users
    except mysql.Error as e:
        print(f"Error fetching users: {e}")
        return []
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

def get_user_by_id(user_id):
    connection = None
    cursor = None
    try:
        connection = _connect_to_database()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        return user
    except mysql.Error as e:
        print(f"Error fetching user by id: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def get_user_by_email(email):
    connection = None
    cursor = None
    try:
        connection = _connect_to_database()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
        user = cursor.fetchone()
        return user
    except mysql.Error as e:
        print(f"Error fetching user by email: {e}")
        return None
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def create_user(user):
    connection = None
    cursor = None
    try:
        connection = _connect_to_database()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO users (full_name, email, password) VALUES (%s, %s, %s)",
                       (user['name'], user['email'], user['password']))
        connection.commit()
        return True
    except mysql.Error as e:
        print(f"Error creating user: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


def update_user_username(user_id, new_username):
    connection = None
    cursor = None
    try:
        connection = _connect_to_database()
        cursor = connection.cursor()
        cursor.execute("UPDATE users SET full_name = %s WHERE id = %s", (new_username, user_id))
        connection.commit()
        return True
    except mysql.Error as e:
        print(f"Error updating user username: {e}")
        return False
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

