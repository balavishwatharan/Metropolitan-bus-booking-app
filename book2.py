from tkinter import *
from tkinter import messagebox
import qrcode
# global variables
e1 = None
e2 = None
e3 = None
e4 = None
e5 = None
master = None

def calculate_price():  #calculating ticket price
    try:
        ticket_price = 140
        total_price = int(e4.get()) * ticket_price

        e5.config(state='normal')
        e5.delete(0, END)
        e5.insert(0, f"{total_price}")
        e5.config(state='readonly') 

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the quantity.")

def save_info():#receipt format
    try:
        generate_qr_code()
        with open("ticket_info.txt", "w") as file:
            file.writelines(f"Online Bus Booking\n" )
            file.writelines(f"Date of Journey:{e3.get()}\n")
            file.writelines(f"===================\n")
            file.writelines(f"    {e1.get()}\n")
            file.writelines(f"       TO      \n")
            file.writelines(f"    {e2.get()}\n")
            file.writelines(f"No.of Passengers : {e4.get()}\n")
            file.writelines(f"--------------------\n")
            file.writelines(f"Total      :{e5.get()}\n")
            file.writelines(f"--------------------\n")
            Label(master, text="Have a safe Journey", fg="green", font=("calibri", 11)).grid(row=15,column=5,pady=2)

        messagebox.showinfo("Success", "Ticket information saved successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
def generate_qr_code(): #QR using qrcode package
    ticket_info = f"Date of Journey: {e3.get()}\nFrom:{e1.get()}\nTo:{e2.get()}\nNumber of Passengers:{e4.get()}\nTotal Price:{e5.get()}"
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=6,
        border=4,
    )
    qr.add_data(ticket_info)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("ticket_qr.png")

def display_info():
    try:
        with open("ticket_info.txt", "r") as file:
            info = file.read()

        ticket_window = Toplevel(master)
        ticket_window.title("Generated Ticket")

        #QR
        qr_img = PhotoImage(file="ticket_qr.png")
        qr_label = Label(ticket_window, image=qr_img)
        qr_label.image = qr_img
        qr_label.pack(padx=20, pady=10)

        #Ticket details
        info_label = Label(ticket_window, text=info)
        info_label.pack(padx=20, pady=20)

    except FileNotFoundError:
        messagebox.showinfo("Info", "No ticket information found. Please save information first.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")

def book():
    global e1, e2, e3, e4, e5,main_screen
    global master

    master = Toplevel()
    master.title("Ticket Purchase Confirmation")
    master.configure(bg='honeydew')
    master.geometry('500x400')

    Label(master, text='Welcome to Ticket Bala.com',bg='mintcream', font=('Helvetica', 17, 'bold')).grid(row=1,column=4,pady=7)
    Label(master, text='From',bg='honeydew',font=("G7 Cube 5",10)).grid(row=5,column=4,padx=4,pady=4)
    Label(master, text='To',bg='honeydew',font=("G7 Cube 5",10)).grid(row=7,column=4,padx=4,pady=2)
    Label(master, text='Date of Journey',bg='honeydew',font=("G7 Cube 5",10)).grid(row=9,column=4,padx=4,pady=2)
    Label(master, text='No.of Passangers',bg='honeydew',font=("G7 Cube 5",10)).grid(row=11,column=4,padx=4,pady=2)
    Label(master, text='Total Price',bg='honeydew',font=("G7 Cube 5",10)).grid(row=13,column=4,padx=4,pady=2)

    e1 = Entry(master)
    e2 = Entry(master)
    e3 = Entry(master)
    e4 = Entry(master)
    e5 = Entry(master, state='readonly') #static-cant change

    e1.grid(row=5, column=5,pady=2)
    e2.grid(row=7, column=5,pady=2)
    e3.grid(row=9, column=5,pady=2)
    e4.grid(row=11, column=5,pady=2)
    e5.grid(row=13, column=5,pady=2)

    Button(master, text="Calculate Price",bg='lime',command=calculate_price,font=("G7 Cube 5",10)).grid(row=18, column=5,pady=5)

    Button(master, text="Submit",bg='lime', command=save_info,font=("G7 Cube 5",10)).grid(row=19, column=5, pady=5)

    Button(master, text="Generate Ticket",bg='lime', command=display_info,font=("G7 Cube 5",10)).grid(row=20, column=5, pady=5)

    mainloop()






