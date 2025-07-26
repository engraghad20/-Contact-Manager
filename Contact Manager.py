import tkinter as tk
from tkinter import messagebox
import pickle

class ContactManager:
    def __init__(self, root):
        self.root = root
        self.root.configure(bg="lightblue")
        root.minsize(700, 700)
        root.maxsize(700, 700)
        self.root.title("Contact Manager")
        self.contacts = {}
        
        # Load existing contacts from file if available
        self.load_contacts()
        
        self.create_widgets()

    def create_widgets(self):
        self.header_Label=tk.Label( self.root,
        text = "Your Contact Manager",  
        font = ("Microsoft Himalaya", "36", "bold"),  
       bg="lightblue" ,fg= "darkblue" )
        self.header_Label.pack()
        self.header_Label.place(x=10,y=10)
       
        self.name_label = tk.Label(self.root, text="Name:",font = ("Microsoft Himalaya", "20", "bold"), bg="lightblue" ,fg= "darkblue")
        self.name_label.pack()
        self.name_label.place(x = 190, y = 60)
        self.name_entry = tk.Entry(self.root,font = ("Consolas", "11"), width = 19 )
        self.name_entry.pack()
        self.name_entry.place(x = 190, y = 90)

        self.phone_label = tk.Label(self.root, text="Phone:",font = ("Microsoft Himalaya", "20", "bold"),  bg="lightblue" ,fg= "darkblue")

        
        self.phone_label.pack()
        self.phone_label.place(x = 190, y = 140)

        self.phone_entry = tk.Entry(self.root,font = ("Consolas", "11"),   width = 19  )
        
        self.phone_entry.pack()
        self.phone_entry.place(x = 190, y = 170)

        self.email_label = tk.Label(self.root, text="Email:",font = ("Microsoft Himalaya", "20", "bold"),  bg="lightblue" ,fg= "darkblue")
        self.email_label.pack()
        self.email_label.place(x = 190, y = 220)

        self.email_entry = tk.Entry(self.root,font = ("Consolas", "11"), width = 19)
        self.email_entry.pack()
        self.email_entry.place(x = 190, y = 250)

        self.add_button = tk.Button(self.root, text="Add Contact", font = ("Microsoft Himalaya", "15", "bold"),fg= "darkblue", width = 24,command=self.add_contact)
        self.add_button.pack()
        self.add_button.place(x = 190, y = 300)
        self.view_all_button = tk.Button(self.root, text="View All Contacts", font = ("Microsoft Himalaya", "15", "bold"),fg= "darkblue",width = 24, command=self.view_all_contacts)
        self.view_all_button.pack()
        self.view_all_button.place(x = 190, y = 350)
        self.search_button = tk.Button(self.root, text="Search Contact",font = ("Microsoft Himalaya", "15", "bold"),fg= "darkblue",  width = 24,command=self.search_contact)
        self.search_button.pack()
        self.search_button.place(x = 190, y = 400)
        self.update_button = tk.Button(self.root, text="Update Contact",font = ("Microsoft Himalaya", "15", "bold"), fg= "darkblue",width = 24, command=self.update_contact)
        self.update_button.pack()
        self.update_button.place(x = 190, y = 450)
        self.delete_button = tk.Button(self.root, text="Delete Contact", font = ("Microsoft Himalaya", "15", "bold"),fg= "darkblue",width = 24, command=self.delete_contact)
        self.delete_button.pack()
        self.delete_button.place(x = 190, y = 500)
        self.clear_button = tk.Button(self.root, text="Delete All Contacts",font = ("Microsoft Himalaya", "15", "bold"), fg= "darkblue",width = 24, command=self.clear_entries)
        self.clear_button.pack()
        self.clear_button.place(x = 190, y = 550)
        self.save_button = tk.Button(self.root, text="Save Contacts", font = ("Microsoft Himalaya", "15", "bold"),fg= "darkblue", width = 24,command=self.save_contacts)
        self.save_button.pack()
        self.save_button.place(x = 190, y = 600)
    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        if name.strip() != '' and phone.strip() != '' and email.strip() != '':
            self.contacts[name] = {'phone': phone, 'email': email}
            messagebox.showinfo("Success", f"Contact {name} added successfully!")
            self.clear_entries()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def view_all_contacts(self):
        if self.contacts:
            contact_list = "\n".join(f"Name: {name}\nPhone: {info['phone']}\nEmail: {info['email']}\n" for name, info in self.contacts.items())
            messagebox.showinfo("All Contacts", contact_list)
        else:
            messagebox.showinfo("All Contacts", "No contacts found.")

    def search_contact(self):
        name = self.name_entry.get()
        contact = self.contacts.get(name)
        if contact :
            messagebox.showinfo("Contact Details", f"Name: {name}\nPhone: {contact['phone']}\nEmail: {contact['email']}")
        else:
            messagebox.showinfo("Error", "Contact not found.")
        self.clear_entries()

    def update_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            phone = self.phone_entry.get()
            email = self.email_entry.get()
            self.contacts[name]['phone'] = phone
            self.contacts[name]['email'] = email
            messagebox.showinfo("Success", "Contact updated successfully!")
        else:
            messagebox.showinfo("Error", "Contact not found.")
        self.clear_entries()

    def delete_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", "Contact deleted successfully!")
        else:
            messagebox.showinfo("Error", "Contact not found.")
        self.clear_entries()

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

    def save_contacts(self):
        with open("contacts.pkl", "wb") as file:
            pickle.dump(self.contacts, file)
        messagebox.showinfo("Success", "Contacts saved successfully!")

    def load_contacts(self):
        try:
            with open("contacts.pkl", "rb") as file:
                self.contacts = pickle.load(file)
        except FileNotFoundError:
            pass  # If the file doesn't exist, start with an empty contacts dictionary


if __name__ == "__main__":
    root = tk.Tk()
    app = ContactManager(root)
    root.mainloop()
