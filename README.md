# My Phone Book

A simple and lightweight desktop phone book application for Windows, built with **Python**, **Tkinter/ttk**, and **SQLite**.

This project was built as a practical portfolio project with a focus on clean structure, local data storage, CRUD operations, search, backup/restore, and Windows executable builds.

## Features

- Add, edit, and delete contacts
- Live refresh of the contact list after changes
- Search across multiple contact fields
- View the selected contact's address
- SQLite database backup and restore
- Local database with no separate database server
- Lightweight Windows desktop interface
- Windows x64 and x86 executable builds

## Contact Information

Each contact can contain:

- First Name
- Last Name
- Mobile
- Phone
- Email
- Fax
- Address
- Company
- Group

**First Name** and **Last Name** are required fields.

## Search

The current search works across:

- First Name
- Last Name
- Mobile
- Phone
- Email
- Fax
- Address
- Company
- Group

Search can be performed using the **Search** button or by pressing **Enter** in the search box.

## Backup & Restore

The application includes database backup and restore functionality.

- **Backup:** creates a copy of the current SQLite database at a location selected by the user.
- **Restore:** replaces the current database with a selected backup after confirmation.

> **Important:** Restoring an older backup replaces the current database. Contacts added after that backup was created will not be present in the restored database.

## Technology

- Python 3.8
- Tkinter / ttk
- SQLite
- PyInstaller
- Windows

The application uses only Python standard-library modules at runtime, so no external Python packages are required for normal source execution.

## Database

The application creates and uses the database automatically at:

```text
%USERPROFILE%\My Phone Book\phonebook.db
```

For example:

```text
C:\Users\YourName\My Phone Book\phonebook.db
```

The database is intentionally stored outside the project directory so user data is separated from the application source code.

## Project Structure

```text
My-Phone-Book/
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
├── assets/
├── docs/
├── tests/
│   └── __init__.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

Build output, virtual environments, Python cache files, local databases, and other machine-specific files are excluded from the repository through `.gitignore`.

## Running From Source

### Requirements

- Windows
- Python 3.8

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\activate
```

Run the application:

```powershell
python app\main.py
```

No external package installation is required for the current version.

## Download

Pre-built Windows executables are published in the project's GitHub Releases.

https://github.com/allen-monarch/My-Phone-Book/releases

Available builds:

- Windows x64
- Windows x86 (32-bit)

The executable builds are provided separately from the source repository so the Git repository remains focused on source code and project files.

## Portfolio Project

This project demonstrates practical experience with:

- Python application structure
- Object-oriented programming basics
- Tkinter/ttk GUI development
- SQLite database design and CRUD operations
- Search and filtering logic
- File and database handling
- Backup and restore workflows
- Error handling
- Virtual environments
- Git and GitHub
- PyInstaller executable packaging
- Windows x86/x64 compatibility considerations

## Future Improvements

Possible future improvements include:

- Advanced field-specific search
- Additional automated tests
- Further UI improvements
- Additional packaging and release automation

## Version

**Current version: 1.0.0**

## License

This project currently does not include a license. If the project is later distributed as open-source software, an appropriate license can be added.
