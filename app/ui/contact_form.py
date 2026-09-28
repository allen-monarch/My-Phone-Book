import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
from models.contact import Contact
from database.db import add_contact, get_contact_by_id, update_contact


def open_contact_form(parent, on_saved=None, contact_id=None):
    window = tk.Toplevel(parent)

    if contact_id is None:
        window.title("Add Contact")
    else:
        window.title("Edit Contact")

        
    window.geometry("500x680")
    window.minsize(450, 630)

    title_label = ttk.Label(
        window,
        text="Add New Contact" if contact_id is None else "Edit Contact",
        font=("Segoe UI", 16, "bold")
    )
    title_label.pack(pady=20)

    # -------------------------
    # Form
    # -------------------------

    form_frame = ttk.Frame(window)
    form_frame.pack(
        fill="x",
        padx=30,
        pady=(0,20)
    )

    first_name_label = ttk.Label(
        form_frame,
        text="First Name:"
    )
    first_name_label.grid(
        row=0,
        column=0,
        sticky="w",
        pady=5
    )

    first_name_entry = ttk.Entry(
        form_frame
    )
    first_name_entry.grid(
        row=0,
        column=1,
        sticky="ew",
        pady=5
    )

    last_name_label = ttk.Label(
        form_frame,
        text="Last Name:"
    )
    last_name_label.grid(
        row=1,
        column=0,
        sticky="w",
        pady=5
    )

    last_name_entry = ttk.Entry(
        form_frame
    )
    last_name_entry.grid(
        row=1,
        column=1,
        sticky="ew",
        pady=5
    )

    mobile_label = ttk.Label(
        form_frame,
        text="Mobile:"
    )
    mobile_label.grid(
        row=2,
        column=0,
        sticky="w",
        pady=5
    )

    mobile_entry = ttk.Entry(
        form_frame
    )
    mobile_entry.grid(
        row=2,
        column=1,
        sticky="ew",
        pady=5
    )

    phone_label = ttk.Label(
        form_frame,
        text="Phone:"
    )
    phone_label.grid(
        row=3,
        column=0,
        sticky="w",
        pady=5
    )

    phone_entry = ttk.Entry(
        form_frame
    )
    phone_entry.grid(
        row=3,
        column=1,
        sticky="ew",
        pady=5
    )

    email_label = ttk.Label(
        form_frame,
        text="Email:"
    )
    email_label.grid(
        row=4,
        column=0,
        sticky="w",
        pady=5
    )

    email_entry = ttk.Entry(
        form_frame
    )
    email_entry.grid(
        row=4,
        column=1,
        sticky="ew",
        pady=5
    )

    fax_label = ttk.Label(
        form_frame,
        text="Fax:"
    )
    fax_label.grid(
        row=5,
        column=0,
        sticky="w",
        pady=5
    )

    fax_entry = ttk.Entry(
        form_frame
    )
    fax_entry.grid(
        row=5,
        column=1,
        sticky="ew",
        pady=5
    )

    address_label = ttk.Label(form_frame,text="Address:")
    address_label.grid(row=6, column=0, sticky="nw", pady=5)
    

    address_entry = tk.Text(
        form_frame,
        height=4,
        width=30,
        font=("Segoe UI", 10),
        background="white",
        wrap="word",
    )

    address_entry.grid(
        row=6,
        column=1,
        sticky="ew",
        pady=5
    )

    company_label = ttk.Label(
        form_frame,
        text="Company:"
    )
    company_label.grid(
        row=7,
        column=0,
        sticky="w",
        pady=5
    )

    company_entry = ttk.Entry(
        form_frame
    )
    company_entry.grid(
        row=7,
        column=1,
        sticky="ew",
        pady=5
    )

    group_label = ttk.Label(
        form_frame,
        text="Group:"
    )
    group_label.grid(
        row=8,
        column=0,
        sticky="w",
        pady=5
    )

    group_entry = ttk.Entry(
        form_frame
    )
    group_entry.grid(
        row=8,
        column=1,
        sticky="ew",
        pady=5
    )

    # -------------------------
    # Load Contact Data for Edit
    # -------------------------

    contact = None

    if contact_id is not None:
        contact = get_contact_by_id(contact_id)

    if contact:
        first_name_entry.insert(0, contact[1])
        last_name_entry.insert(0, contact[2])
        mobile_entry.insert(0, contact[3])
        phone_entry.insert(0, contact[4])
        email_entry.insert(0, contact[5])
        fax_entry.insert(0, contact[6])
        address_entry.insert("1.0", contact[7])
        company_entry.insert(0, contact[8])
        group_entry.insert(0, contact[9])


    form_frame.columnconfigure(
        1,
        weight=1
    )

    # -------------------------
    # Save Contact
    # -------------------------

    def save_contact():
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()

        if not first_name.strip():
            messagebox.showwarning(
               "Validation",
                "First Name is required."
            )

            first_name_entry.focus()
            return

        # valid email

        if not last_name.strip():
            messagebox.showwarning(
                "Validation",
                "Last Name is required."
            )

            last_name_entry.focus()
            return

        email = email_entry.get().strip()
        if email and ("@" not in email or "." not in email.split("@")[-1]):
            messagebox.showwarning(
                "Validation",
                "Please enter a valid email address."
            )

            email_entry.focus()
            return


        mobile = mobile_entry.get()
        phone = phone_entry.get()
        fax = fax_entry.get()
        address = address_entry.get("1.0", "end-1c")
        company = company_entry.get()
        group_name = group_entry.get()

        contact = Contact(
            first_name=first_name,
            last_name=last_name,
            mobile=mobile,
            phone=phone,
            email=email,
            fax=fax,
            address=address,
            company=company,
            group_name=group_name
        )
        try:
            if contact_id is None:
                add_contact(contact)
                message = "Contact added successfully!"

            else:
                update_contact(contact_id, contact)
                message = "Contact updated successfully!"

        except sqlite3.Error as error:
            print("DATABASE ERROR:", error)

            messagebox.showerror(
                "Database Error",
                "Could not save contact."
            )

            return

        if on_saved: 
            on_saved()

        messagebox.showinfo(
            "Success",
            message
        )

        print(message)

        window.destroy()

    # -------------------------
    # Buttons
    # -------------------------

    button_frame = ttk.Frame(window)
    button_frame.pack(
        side="bottom",
        fill="x",
        padx=30,
        pady=20
    )

    cancel_button = ttk.Button(
        button_frame,
        text="Cancel",
        command=window.destroy
    )
    cancel_button.pack(
        side="right",
        padx=5
    )

    save_button = ttk.Button(
        button_frame,
        text="Save",
        command=save_contact
    )
    save_button.pack(
        side="right",
        padx=5
    )

    return window