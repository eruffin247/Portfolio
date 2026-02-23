# Tkinkter is the built-in python module for creating gui. I'm using it to create a simple user interface to display the generated password. It is not necessary for generating the password, but it makes it more user-friendly.
import secrets
import tkinter as tk

characters ="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890-=!@#$%^&*()_+"

# This assigns tk.Tk() to window. tk.Tk() is what creates the main application window.
# window.title sets the title of the main window.
# window.geometry sets the window size.
window = tk.Tk()
window.title("Secure Password Generator", )
window.geometry("600x300")

# def is used to define a user-made function. In this case, I'm creating a function named "gen_password" that will be used to generate a random secure password.
def generate_password():
    password = ""
    for _ in range(15):
        password += secrets.choice(characters)
    result_label.config(text=f"Your new password is: {password}")

# tk.Button creates an interactive button widget. The "text" portion is what is displayed on the widget button itself. The "command" portion tells the code what to do once the button is clicked.
# pack places the "generate_button" inside the window.
generate_button = tk.Button(window, text = "Generate password", command = generate_password)
generate_button.pack(pady=10)

# tk.Label creates a text label widget. (.Button is interactive, .Label is just text).
result_label = tk.Label(window, text = "", font = ("Times New Roman", 12))
result_label.pack(pady=20)

window.mainloop()