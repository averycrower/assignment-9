import tkinter as tk

root = tk.Tk()
root.title("agree to start")
root.geometry("350x250")

#disable the name and email box until the agree button is checked
name_label = tk.Label(root, text="Name:")
name_entry = tk.Entry(root, state="disabled")

email_label = tk.Label(root, text="Email:")
email_entry = tk.Entry(root, state="disabled")

#fake submit button that doesnt work
def fake_submit():
    status_label.config(text="Error... Maybe try another time?")

submit_button = tk.Button(root, text="Submit", command=fake_submit)

#agreement checkbox
def toggle_fields():
    if agree_var.get() == 1:
        name_entry.config(state="normal")
        email_entry.config(state="normal")
        status_label.config(text="")
    else:
        name_entry.config(state="disabled")
        email_entry.config(state="disabled")
        status_label.config(text="You must agree to even begin.")

agree_var = tk.IntVar()
agree_checkbox = tk.Checkbutton(root, text="I agree to the terms without seeing them", variable=agree_var, command=toggle_fields)

#layout pf box
agree_checkbox.pack(pady=10)
name_label.pack()
name_entry.pack()
email_label.pack()
email_entry.pack(pady=5)
submit_button.pack(pady=10)

status_label = tk.Label(root, text="", fg="red")
status_label.pack()

root.mainloop()
