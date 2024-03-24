import os
from tkinter import *
from bookpage import *

def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.configure(bg='honeydew')
    register_screen.geometry("500x400")
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
    Label(register_screen, text="Please enter details below", bg="honeydew").pack()
    Label(register_screen, text="",bg='honeydew').pack()
    username_label = Label(register_screen, text="Username * ",bg="honeydew",font=("G7 Cube 5",10))
    username_label.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_label = Label(register_screen, text="Password * ",bg="honeydew",font=("G7 Cube 5",10))
    password_label.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="",bg="honeydew").pack()
    Button(register_screen, text="Register", width=10, height=1,font=("G7 Cube 5",10), bg="limegreen", command=register_user).pack()
    additional_terms_text = (
        "By registering, you agree to the following:\n"
        "1. You will provide accurate and truthful information during registration.\n"
        "2. You are responsible for maintaining the confidentiality of your account credentials.\n"
        "3. Any misuse of the platform may result in the termination of your account.\n"
        "4. We reserve the right to modify or update these terms at any time.\n"
        "5. Your personal information will be handled as per our Privacy Policy."
    )
    Label(register_screen, text=additional_terms_text, bg="honeydew", font=("calibri", 10)).pack(side="bottom", pady=10)
def login():
    main_screen.withdraw()
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.configure(bg="honeydew")
    login_screen.geometry("500x400")
    Label(login_screen,bg='honeydew', text="Please enter details below to login").pack()
    Label(login_screen, text="",bg="honeydew").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ",bg="honeydew",font=("G7 Cube 5",10)).pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="",bg="honeydew").pack()
    Label(login_screen, text="Password * ",bg="honeydew",font=("G7 Cube 5",10)).pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="",bg="honeydew").pack()
    Button(login_screen,bg='lime', text="Login", width=10, height=1, command=login_verify).pack()
    terms_conditions_text = (
        "By logging in, you agree to abide by our Terms and Conditions.\n"
        "For more details, please read our Privacy Policy."
    )
    Label(login_screen, text=terms_conditions_text, bg="honeydew", font=("calibri", 12)).pack(side="bottom", pady=10)

def register_user():
    username_info = username.get()
    password_info = password.get()
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
    username_entry.delete(0, END)
    password_entry.delete(0, END)
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_success()
        else:
            password_not_recognized()
    else:
        user_not_found()

def login_success():
    Label(login_screen, text="Login Success", fg="green", font=("calibri", 11)).pack()
    login_screen.withdraw()
    bus_booking_page(main_screen)

def password_not_recognized():
    Label(login_screen, text="Invalid Password", fg="red", font=("calibri", 11)).pack()

def user_not_found():
    Label(login_screen, text="User Not Found", fg="red", font=("calibri", 11)).pack()

def main_account_screen():   
    global main_screen
    main_screen = Tk()    
    main_screen.geometry("500x400") 
    main_screen.title("Account")
    main_screen.configure(bg='honeydew')
    Label(text="Bus Bee.com",fg="black", bg="mintcream", width="300", height="2", font=("G7 Cube 5", 25)).pack() 
    Label(text="",bg="honeydew").pack()
    #Photo
    photo=PhotoImage(file="bus.png")
    resized_image = photo.subsample(2)
    image_label = Label(main_screen,image=resized_image,bg='honeydew')
    image_label.pack(pady=40)
    #Frame
    button_frame = Frame(main_screen)
    button_frame.pack()
    Button(button_frame,text="Login",font=("G7 Cube 5",8),bg="chartreuse", height="2", width="15", command=login).pack(side="left", padx=5) 
    Label(text="",bg="honeydew").pack()
    Button(button_frame,text="Register",font=("G7 Cube 5",8),bg="chartreuse", height="2", width="15", command=register).pack(side="left", padx=5) 
    main_screen.mainloop()

main_account_screen()
