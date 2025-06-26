"""
Blood Donor Manager
A simple Tkinter-based app for managing blood donor records in memory.
Suitable for class 12th Computer Science project.
"""

import tkinter as tk
from tkinter import messagebox, simpledialog

# In-memory donor data: list of dictionaries
donors = []

# Helper functions
def add_donor(name, age, blood_group, contact):
    donor = {
        'Name': name,
        'Age': age,
        'Blood Group': blood_group,
        'Contact': contact
    }
    donors.append(donor)

def get_all_donors():
    return donors

def search_donors_by_blood_group(blood_group):
    return [d for d in donors if d['Blood Group'].lower() == blood_group.lower()]

def update_donor(index, name, age, blood_group, contact):
    if 0 <= index < len(donors):
        donors[index] = {
            'Name': name,
            'Age': age,
            'Blood Group': blood_group,
            'Contact': contact
        }
        return True
    return False

def delete_donor(index):
    if 0 <= index < len(donors):
        donors.pop(index)
        return True
    return False

# GUI Functions
def add_donor_gui():
    def save():
        name = name_var.get()
        age = age_var.get()
        blood_group = bg_var.get()
        contact = contact_var.get()
        if not (name and age and blood_group and contact):
            messagebox.showerror("Error", "All fields are required!")
            return
        add_donor(name, age, blood_group, contact)
        messagebox.showinfo("Success", "Donor added successfully!")
        add_win.destroy()

    add_win = tk.Toplevel(root)
    add_win.title("Add Donor")
    tk.Label(add_win, text="Name:").grid(row=0, column=0)
    tk.Label(add_win, text="Age:").grid(row=1, column=0)
    tk.Label(add_win, text="Blood Group:").grid(row=2, column=0)
    tk.Label(add_win, text="Contact:").grid(row=3, column=0)
    name_var = tk.StringVar()
    age_var = tk.StringVar()
    bg_var = tk.StringVar()
    contact_var = tk.StringVar()
    tk.Entry(add_win, textvariable=name_var).grid(row=0, column=1)
    tk.Entry(add_win, textvariable=age_var).grid(row=1, column=1)
    tk.Entry(add_win, textvariable=bg_var).grid(row=2, column=1)
    tk.Entry(add_win, textvariable=contact_var).grid(row=3, column=1)
    tk.Button(add_win, text="Save", command=save).grid(row=4, column=0, columnspan=2)

def view_donors_gui():
    view_win = tk.Toplevel(root)
    view_win.title("All Donors")
    text = tk.Text(view_win, width=60, height=20)
    text.pack()
    all_donors = get_all_donors()
    if not all_donors:
        text.insert(tk.END, "No donors found.\n")
    else:
        for idx, donor in enumerate(all_donors):
            text.insert(tk.END, f"{idx+1}. Name: {donor['Name']}, Age: {donor['Age']}, Blood Group: {donor['Blood Group']}, Contact: {donor['Contact']}\n")

def search_donor_gui():
    def search():
        bg = bg_var.get()
        results = search_donors_by_blood_group(bg)
        text.delete(1.0, tk.END)
        if not results:
            text.insert(tk.END, "No donors found for this blood group.\n")
        else:
            for donor in results:
                text.insert(tk.END, f"Name: {donor['Name']}, Age: {donor['Age']}, Blood Group: {donor['Blood Group']}, Contact: {donor['Contact']}\n")

    search_win = tk.Toplevel(root)
    search_win.title("Search by Blood Group")
    tk.Label(search_win, text="Blood Group:").pack()
    bg_var = tk.StringVar()
    tk.Entry(search_win, textvariable=bg_var).pack()
    tk.Button(search_win, text="Search", command=search).pack()
    text = tk.Text(search_win, width=60, height=10)
    text.pack()

def update_donor_gui():
    def update():
        try:
            idx = int(idx_var.get()) - 1
        except ValueError:
            messagebox.showerror("Error", "Invalid index!")
            return
        name = name_var.get()
        age = age_var.get()
        bg = bg_var.get()
        contact = contact_var.get()
        if update_donor(idx, name, age, bg, contact):
            messagebox.showinfo("Success", "Donor updated!")
            update_win.destroy()
        else:
            messagebox.showerror("Error", "Invalid donor index!")

    update_win = tk.Toplevel(root)
    update_win.title("Update Donor")
    tk.Label(update_win, text="Donor Index (from View All):").grid(row=0, column=0)
    tk.Label(update_win, text="New Name:").grid(row=1, column=0)
    tk.Label(update_win, text="New Age:").grid(row=2, column=0)
    tk.Label(update_win, text="New Blood Group:").grid(row=3, column=0)
    tk.Label(update_win, text="New Contact:").grid(row=4, column=0)
    idx_var = tk.StringVar()
    name_var = tk.StringVar()
    age_var = tk.StringVar()
    bg_var = tk.StringVar()
    contact_var = tk.StringVar()
    tk.Entry(update_win, textvariable=idx_var).grid(row=0, column=1)
    tk.Entry(update_win, textvariable=name_var).grid(row=1, column=1)
    tk.Entry(update_win, textvariable=age_var).grid(row=2, column=1)
    tk.Entry(update_win, textvariable=bg_var).grid(row=3, column=1)
    tk.Entry(update_win, textvariable=contact_var).grid(row=4, column=1)
    tk.Button(update_win, text="Update", command=update).grid(row=5, column=0, columnspan=2)

def delete_donor_gui():
    def delete():
        try:
            idx = int(idx_var.get()) - 1
        except ValueError:
            messagebox.showerror("Error", "Invalid index!")
            return
        if delete_donor(idx):
            messagebox.showinfo("Success", "Donor deleted!")
            delete_win.destroy()
        else:
            messagebox.showerror("Error", "Invalid donor index!")

    delete_win = tk.Toplevel(root)
    delete_win.title("Delete Donor")
    tk.Label(delete_win, text="Donor Index (from View All):").pack()
    idx_var = tk.StringVar()
    tk.Entry(delete_win, textvariable=idx_var).pack()
    tk.Button(delete_win, text="Delete", command=delete).pack()

# Main window
root = tk.Tk()
root.title("Blood Donor Manager")
root.geometry("400x400")

# Buttons
tk.Button(root, text="Add Donor", width=25, command=add_donor_gui).pack(pady=10)
tk.Button(root, text="View All Donors", width=25, command=view_donors_gui).pack(pady=10)
tk.Button(root, text="Search by Blood Group", width=25, command=search_donor_gui).pack(pady=10)
tk.Button(root, text="Update Donor Info", width=25, command=update_donor_gui).pack(pady=10)
tk.Button(root, text="Delete Donor", width=25, command=delete_donor_gui).pack(pady=10)
tk.Button(root, text="Exit", width=25, command=root.destroy).pack(pady=10)

root.mainloop()
