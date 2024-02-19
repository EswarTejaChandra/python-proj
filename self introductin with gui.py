import tkinter as tk
from tkinter import messagebox


def verify():
    # Validate student data here (e.g., check name, age, gmail, phone number, etc.)
    name = entry_name.get()
    age = entry_age.get()
    gmail = entry_gmail.get()
    phone_number = entry_phone.get()
    roll_number = entry_roll.get()
    section = entry_section.get()
    year_of_study = entry_year.get()
    percentage = entry_percentage.get()
    backlogs = entry_backlogs.get()

    if name and age and gmail and phone_number and roll_number and section and year_of_study and percentage and backlogs:
        messagebox.showinfo("Verification", "Student data verified successfully!")
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

def submit():
    # Handle the submission of student data here
    pass

def cancel():
    # Handle the cancellation of student data here
    pass

# Create the main window
root = tk.Tk()
root.title("Student Entries")

# Create labels, entry fields, checkboxes, and radio buttons
label_name = tk.Label(root, text="Name:")
entry_name = tk.Entry(root)

label_age = tk.Label(root, text="Age:")
entry_age = tk.Entry(root)

label_gmail = tk.Label(root, text="Gmail:")
entry_gmail = tk.Entry(root)

label_phone = tk.Label(root, text="Phone Number:")
entry_phone = tk.Entry(root)

label_roll = tk.Label(root, text="Roll Number:")
entry_roll = tk.Entry(root)

label_section = tk.Label(root, text="Section:")
entry_section = tk.Entry(root)

label_year = tk.Label(root, text="Year of Study:")
entry_year = tk.Entry(root)

label_percentage = tk.Label(root, text="Percentage:")
entry_percentage = tk.Entry(root)

label_backlogs = tk.Label(root, text="Backlogs:")
entry_backlogs = tk.Entry(root)

checkbox_hostel = tk.Checkbutton(root, text="Hostel Accommodation")
checkbox_transport = tk.Checkbutton(root, text="Transport Required")

radio_var = tk.StringVar()
radio_var.set("Male")
radio_male = tk.Radiobutton(root, text="Male", variable=radio_var, value="Male")
radio_female = tk.Radiobutton(root, text="Female", variable=radio_var, value="Female")

# Place widgets using grid layout
label_name.grid(row=0, column=0, padx=10, pady=5)
entry_name.grid(row=0, column=1, padx=10, pady=5)

label_age.grid(row=1, column=0, padx=10, pady=5)
entry_age.grid(row=1, column=1, padx=10, pady=5)

label_gmail.grid(row=2, column=0, padx=10, pady=5)
entry_gmail.grid(row=2, column=1, padx=10, pady=5)

label_phone.grid(row=3, column=0, padx=10, pady=5)
entry_phone.grid(row=3, column=1, padx=10, pady=5)

label_roll.grid(row=4, column=0, padx=10, pady=5)
entry_roll.grid(row=4, column=1, padx=10, pady=5)

label_section.grid(row=5, column=0, padx=10, pady=5)
entry_section.grid(row=5, column=1, padx=10, pady=5)

label_year.grid(row=6, column=0, padx=10, pady=5)
entry_year.grid(row=6, column=1, padx=10, pady=5)

label_percentage.grid(row=7, column=0, padx=10, pady=5)
entry_percentage.grid(row=7, column=1, padx=10, pady=5)

label_backlogs.grid(row=8, column=0, padx=10, pady=5)
entry_backlogs.grid(row=8, column=1, padx=10, pady=5)

checkbox_hostel.grid(row=9, column=0, padx=10, pady=5)
checkbox_transport.grid(row=9, column=1, padx=10, pady=5)

radio_male.grid(row=10, column=0, padx=10, pady=5)
radio_female.grid(row=10, column=1, padx=10, pady=5)

# Create a verify button
verify_button = tk.Button(root, text="Verify", command=verify)
verify_button.grid(row=11, columnspan=2, padx=10, pady=10)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit, bg="blue")
submit_button.grid(row=12, column=0, padx=10, pady=10)

# Create a cancel button
cancel_button = tk.Button(root, text="Cancel", command=cancel, bg="red")
cancel_button.grid(row=12, column=1, padx=10, pady=10)

# Start the event loop
root.mainloop()
