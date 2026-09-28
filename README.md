# My Phone Book

A simple desktop phone book application for Windows, built with Python,
Tkinter, and SQLite.

## Features

-   Add new contacts
-   Edit existing contacts
-   Delete contacts
-   Search contacts
-   Refresh the contact list
-   View the selected contact's address
-   Create database backups
-   Restore the database from a backup
-   SQLite database for local data storage
-   Simple and lightweight desktop interface

## Contact Information

Each contact can contain:

-   First Name
-   Last Name
-   Mobile
-   Phone
-   Email
-   Fax
-   Address
-   Company
-   Group

First Name and Last Name are required fields.

## Technology

-   Python 3.8
-   Tkinter / ttk
-   SQLite
-   Windows desktop application

The application does not require a separate database server. All contact
data is stored locally in a SQLite database.

## Project Structure

``` text
Phone Book/
│
├── app/
│   ├── main.py
│   ├── database/
│   │   └── db.py
│   ├── models/
│   │   └── contact.py
│   └── ui/
│       ├── main_window.py
│       └── contact_form.py
│
├── data/
│   └── phonebook.db
│
├── tests/
├── assets/
├── docs/
├── README.md
├── requirements.txt
└── .gitignore
```

## Running From Source

Make sure Python 3.8 is installed.

Create and activate a virtual environment:

``` powershell
python -m venv .venv
.venv\Scripts\activate
```

Run the application:

``` powershell
python app\main.py
```

## Database

The application's database is:

``` text
data\phonebook.db
```

The database is created automatically when the application starts if it
does not already exist.

## Backup

Use the **Backup** button to create a copy of the current SQLite
database.

The application allows the user to choose where the backup file should
be saved.

It is recommended to keep backup files in a safe location.

## Restore

Use the **Restore** button to select a previous database backup.

Restoring a backup replaces the current database with the selected
backup.

The application asks for confirmation before replacing the current
database.

**Important:** Any contacts that were added after the selected backup
was created will not exist in the restored database.

## Search

The current search searches across the available contact information,
including:

-   First Name
-   Last Name
-   Mobile
-   Phone
-   Email
-   Fax
-   Address
-   Company
-   Group

The search can be performed using the **Search** button or by pressing
**Enter** in the search box.

## Notes

-   The application is designed to remain simple and easy to use.
-   Contact data is stored locally.
-   No internet connection is required for normal operation.
-   The current version uses a general search. More advanced
    field-specific search can be added in a future version.
-   The address field supports multiline text. Right-to-left text
    editing may have limitations because of the underlying Tkinter text
    widget.

## Version

Current development version: **1.0**
