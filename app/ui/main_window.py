import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import sqlite3
import shutil

from database.db import get_contacts, delete_contact, search_contacts , DATABASE_PATH
from ui.contact_form import open_contact_form



def create_main_window():
    root = tk.Tk()

    style = ttk.Style()

    style.configure(
        "TButton",
        font=("Segoe UI", 10),
        padding = (10,6)
    )

    style.configure(
    "Search.TButton",
    font=("Segoe UI", 9),
    padding=(8, 0)
    )
    
    style.configure(
        "TLabel",
        font=("Segoe UI", 10)
    )

    style.configure(
        "TEntry",
        font=("Segoe UI", 10)
    )

    style.configure(
    "Treeview.Heading",
    font=("Segoe UI", 10, "bold"),
    padding=(8, 6)
    )  

    style.configure(
    "Treeview",
    font=("Segoe UI", 10),
    rowheight=30 ,
    padding=(5, 0)
    )

    style.map(
    "Treeview",
    background=[
        ("selected", "#2F6FED")
    ],
    foreground=[
        ("selected", "white")
    ]
    )



    root.title("My Phone Book")
    root.geometry("1500x800")
    root.minsize(850, 500)

    # -------------------------
    # Main Container
    # -------------------------

    main_frame = ttk.Frame(root, padding=10)
    main_frame.pack(fill="both", expand=True)

    # -------------------------
    # Header
    # -------------------------

    header_frame = ttk.Frame(main_frame)
    header_frame.pack(fill="x", pady=(20, 15))

    title_label = ttk.Label(
        header_frame,
        text="📒 My Phone Book",
        font=("Segoe UI", 18, "bold")
    )
    title_label.pack(
        side="left",
        padx = (0,20)
    )

    search_entry = ttk.Entry(
        header_frame,
        width=40
    )
    search_entry.pack(side="right")

    

    # -------------------------
    # Toolbar
    # -------------------------

    toolbar_frame = ttk.Frame(main_frame)
    toolbar_frame.pack(fill="x", pady=(20, 8))

    add_button = ttk.Button(
    toolbar_frame,
    text="➕ Add Contact"
    )

    add_button.pack(side="left", padx=(0, 5))

    edit_button = ttk.Button(
        toolbar_frame,
        text="🖍 Edit"
    )
    edit_button.pack(side="left", padx=(0, 5))

    delete_button = ttk.Button(
        toolbar_frame,
        text="🗑 Delete"
    )
    delete_button.pack(side="left", padx=(0, 5))

    refresh_button = ttk.Button(
    toolbar_frame,
    text="♻️ Refresh"
    )
    refresh_button.pack(side="left", padx=(0, 5))

    backup_button = ttk.Button(
        toolbar_frame,
        text="🛢️Backup"
    )
    backup_button.pack(side="left", padx=(0, 5))

    restore_button = ttk.Button(
        toolbar_frame,
        text="🔄 Restore"
    )

    restore_button.pack(
        side="left",
        padx=(0, 5)
    )

    # -------------------------
    # Contact Table
    # -------------------------

    table_frame = ttk.Frame(main_frame)
    table_frame.pack(fill="both", expand=True)

    columns = (
    "name",
    "last_name",
    "mobile",
    "phone",
    "email",
    "fax",
    "address",
    "company",
    "group"
    )

    contact_table = ttk.Treeview(
        table_frame,
        columns=columns,
        show="headings"
    )

    contact_table.heading("name", text="Name")
    contact_table.heading("last_name", text="Last Name")
    contact_table.heading("mobile", text="Mobile")
    contact_table.heading("phone", text="Phone")
    contact_table.heading("email", text="Email")
    contact_table.heading("fax", text="Fax")
    contact_table.heading("address", text="Address")
    contact_table.heading("company", text="Company")
    contact_table.heading("group", text="Group")

    contact_table.column("name", width=90)
    contact_table.column("last_name", width=120)
    contact_table.column("mobile", width=90)
    contact_table.column("phone", width=90)
    contact_table.column("email", width=120)
    contact_table.column("fax", width=60)
    contact_table.column("address", width=220)
    contact_table.column("company", width=100)
    contact_table.column("group", width=40)

    contact_table.pack(
        side="left",
        fill="both",
        expand=True
    )

    # -------------------------
    # Vertical Scrollbar
    # -------------------------

    scrollbar = ttk.Scrollbar(
        table_frame,
        orient="vertical",
        command=contact_table.yview
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )

    contact_table.configure(
        yscrollcommand=scrollbar.set
    )

    # -------------------------
    # Address Preview
    # -------------------------

    address_preview_frame = ttk.Frame(main_frame)
    address_preview_frame.pack(
        fill="x",
        pady=(8, 0)
    )

    address_preview_label = ttk.Label(
        address_preview_frame,
        text="Selected Address:"
    )

    address_preview_label.pack(
        anchor="w"
    )

    address_preview = tk.Text(
        address_preview_frame,
        height=3,
        font=("Segoe UI", 10),
        background="white",
        wrap="word"
    )

    address_preview.pack(
        fill="x",
        pady=(3, 0)
    )

    address_preview.configure(
        state="disabled"
    )


    # -------------------------
    # Status Bar
    # -------------------------

    status_frame = ttk.Frame(main_frame)
    status_frame.pack(fill="x", pady=(10, 0))

    contacts_label = ttk.Label(
        status_frame,
        text="Contacts: 0",
        font=("Segoe UI", 9)
    )

    contacts_label.pack(side="left")

    database_label = ttk.Label(
        status_frame,
        text="Database: Connected"
    )
    database_label.pack(side="right")


    # -------------------------
    # Load Contacts
    # -------------------------

    def show_selected_address(event=None):
        selected_items = contact_table.selection()

        address_preview.configure(state="normal")
        address_preview.delete("1.0", "end")

        if not selected_items:
            address_preview.configure(state="disabled")
            return

        selected_item = selected_items[0]

        values = contact_table.item(
            selected_item,
            "values"
        )

        address = values[6]

        address_preview.insert(
            "1.0",
            address
        )

        address_preview.configure(state="disabled")

    
    def load_contacts():
        contact_table.delete(*contact_table.get_children())
        contacts = get_contacts()

        print("Contacts from DB:", contacts)


        for contact in contacts:
            contact_table.insert(
                "",
                "end",
                iid=str(contact[0]),
                values=(
                    contact[1],
                    contact[2],
                    contact[3],
                    contact[4],
                    contact[5],
                    contact[6],
                    contact[7],
                    contact[8],
                    contact[9]
                )
            )

        contacts_label.config(
            text="Contacts: {}".format(len(contacts))
        )


    def perform_search():
        search_text = search_entry.get().strip()

        if not search_text:
            load_contacts()
            return

        contacts = search_contacts(search_text)

        for item in contact_table.get_children():
            contact_table.delete(item)

        for contact in contacts:
            contact_table.insert(
                "",
                "end",
                iid=str(contact[0]),
                values=(
                    contact[1],
                    contact[2],
                    contact[3],
                    contact[4],
                    contact[5],
                    contact[6],
                    contact[7],
                    contact[8],
                    contact[9]
                )
            )

    # search_entry.bind("<Return>", lambda event: perform_search())
    search_button = ttk.Button(
        header_frame,
        text=" 🔎 Search",
        command=perform_search,
        style="Search.TButton"
    )

    search_button.pack(
        side="right",
        padx=(5, 5)
    )
    
    search_entry.bind("<Return>",lambda event: perform_search())

    
    def open_edit_form():
        selected_items = contact_table.selection()

        if not selected_items:
            print("No contact selected.")
            return

        selected_item = selected_items[0]

        contact_id = int(selected_item)

        open_contact_form(
            root,
            on_saved=load_contacts,
            contact_id=contact_id
        )

    def delete_selected_contact():
        selected_items = contact_table.selection()

        if not selected_items:
            messagebox.showwarning(
                "Delete Contact",
                "Please select a contact first."
            )
            return

        selected_item = selected_items[0]
        contact_id = int(selected_item)

        confirmed = messagebox.askyesno(
            "Delete Contact",
            "Are you sure you want to delete this contact?"
        )

        if not confirmed:
            return

        try:
            delete_contact(contact_id)

        except Exception as error:
            print("DATABASE ERROR:", error)

            messagebox.showerror(
                "Database Error",
                "Could not delete contact."
            )

            return

        load_contacts()

        messagebox.showinfo(
            "Success",
            "Contact deleted successfully!"
        )


        
    def open_add_form():
        open_contact_form(root, load_contacts)



    def backup_database():
        backup_path = filedialog.asksaveasfilename(
            title="Save Phone Book Backup",
            defaultextension=".db",
            filetypes=[
                ("SQLite Database", "*.db"),
                ("All Files", "*.*")
            ],
            initialfile="phonebook_backup.db"
        )

        if not backup_path:
            return

        try:
            shutil.copy2(
                DATABASE_PATH,
                backup_path
            )        

        except OSError as error:
            print("BACKUP ERROR:", error)

            messagebox.showerror(
                "Backup Error",
                "Could not create backup."
            )

            return

        messagebox.showinfo(
            "Backup",
            "Backup created successfully!"
        )

        print("Backup created:", backup_path)


    def restore_database():
        backup_path = filedialog.askopenfilename(
            title="Select Phone Book Backup",
            filetypes=[
                ("SQLite Database", "*.db"),
                ("All Files", "*.*")
            ]
        )

        if not backup_path:
            return

        confirmed = messagebox.askyesno(
            "Restore Database",
            "Restoring this backup will replace the current database.\n\n"
            "Are you sure you want to continue?"
        )
        if not confirmed:
            return

        try:
            shutil.copy2(
                backup_path,
                DATABASE_PATH
            )

        except OSError as error:
            print("RESTORE ERROR:", error)

            messagebox.showerror(
                "Restore Error",
                "Could not restore database."
            )

            return

        load_contacts()

        messagebox.showinfo(
            "Restore",
            "Database restored successfully!"
        )



    edit_button.config(command=open_edit_form)

    delete_button.config(command=delete_selected_contact)

    add_button.config(command=open_add_form)

    refresh_button.config(command=load_contacts)

    backup_button.config(command=backup_database)

    restore_button.config(command=restore_database)

    contact_table.bind(
        "<<TreeviewSelect>>",
        show_selected_address
    )

    load_contacts()


    return root