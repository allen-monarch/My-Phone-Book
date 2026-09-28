import sqlite3
import os


DATABASE_DIRECTORY = os.path.join(
    os.path.expanduser("~"),
    "My Phone Book"
)

os.makedirs(DATABASE_DIRECTORY, exist_ok=True)

DATABASE_PATH = os.path.join(
    DATABASE_DIRECTORY,
    "phonebook.db"
)


def get_connection():
    return sqlite3.connect(DATABASE_PATH)



def initialize_database():
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                mobile TEXT,
                phone TEXT,
                email TEXT,
                fax TEXT,
                address TEXT,
                company TEXT,
                group_name TEXT,
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
        """)

        connection.commit()

    except sqlite3.Error:
        connection.rollback()
        raise

    finally:
        connection.close()



def add_contact(contact):
    connection = get_connection()
    try:

        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO contacts (
                first_name,
                last_name,
                mobile,
                phone,
                email,
                fax,
                address,
                company,
                group_name,
                created_at,
                updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now'), datetime('now'))
        """, (
            contact.first_name,
            contact.last_name,
            contact.mobile,
            contact.phone,
            contact.email,
            contact.fax,
            contact.address,
            contact.company,
            contact.group_name
        ))

        connection.commit()

    except sqlite3.Error:
        connection.rollback()
        raise

    finally:
        connection.close()



def get_contacts():
    connection = get_connection()

    try:

        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                id,
                first_name,
                last_name,
                mobile,
                phone,
                email,
                fax,
                address,
                company,
                group_name,
                created_at,
                updated_at
            FROM contacts
            ORDER BY id DESC
        """)

        contacts = cursor.fetchall()
        return contacts

    except sqlite3.Error:
        raise

    finally:
        connection.close()



def get_contact_by_id(contact_id):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            SELECT
                id,
                first_name,
                last_name,
                mobile,
                phone,
                email,
                fax,
                address,
                company,
                group_name,
                created_at,
                updated_at
            FROM contacts
            WHERE id = ?
        """, (contact_id,))

        contact = cursor.fetchone()
        return contact

    except sqlite3.Error:
        raise

    finally :
        connection.close()


def update_contact(contact_id, contact):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            UPDATE contacts
            SET
                first_name = ?,
                last_name = ?,
                mobile = ?,
                phone = ?,
                email = ?,
                fax = ?,
                address = ?,
                company = ?,
                group_name = ?,
                updated_at = datetime('now')
            WHERE id = ?
        """, (
            contact.first_name,
            contact.last_name,
            contact.mobile,
            contact.phone,
            contact.email,
            contact.fax,
            contact.address,
            contact.company,
            contact.group_name,
            contact_id
        ))

        connection.commit()

    except sqlite3.Error:
        connection.rollback()
        raise

    finally:
        connection.close()


def delete_contact(contact_id):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        cursor.execute("""
            DELETE FROM contacts
            WHERE id = ?
        """, (contact_id,))

        connection.commit()

    except sqlite3.Error:
        connection.rollback()
        raise

    finally:
        connection.close()

        

def search_contacts(search_text):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        search_pattern = "%" + search_text + "%"

        cursor.execute("""
            SELECT
                id,
                first_name,
                last_name,
                mobile,
                phone,
                email,
                fax,
                address,
                company,
                group_name,
                created_at,
                updated_at
            FROM contacts
            WHERE first_name LIKE ?
            OR last_name LIKE ?
            OR mobile LIKE ?
            OR phone LIKE ?
            OR email LIKE ?
            OR fax LIKE ?
            OR address LIKE ?
            OR company LIKE ?
            OR group_name LIKE ?
            ORDER BY id DESC
        """, (
            search_pattern,
            search_pattern,
            search_pattern,
            search_pattern,
            search_pattern,
            search_pattern,
            search_pattern,
            search_pattern,
            search_pattern
        ))

        contacts = cursor.fetchall()

        return contacts

    except sqlite3.Error:
        raise

    finally:
        connection.close()
