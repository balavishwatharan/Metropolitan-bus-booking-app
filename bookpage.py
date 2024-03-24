from tkinter import *
from snacks import *


def book_bus():   #for backend data printing 
    from_location = from_var.get()
    to_location = to_var.get()
    date_of_journey = date_var.get()
    num_passengers = num_passengers_var.get()


    print("From:", from_location)
    print("To:", to_location)
    print("Date of Journey:", date_of_journey)
    print("Number of Passengers:", num_passengers)

def bus_booking_page(main_screen): #actual page
    global booking_screen
    booking_screen = Toplevel(main_screen)
    booking_screen.configure(bg='honeydew')
    booking_screen.title("Bus Booking Page")
    booking_screen.geometry("500x400")

    Label(booking_screen, text="Bus Booking", bg="honeydew", width="400", height="2", font=("Calibri", 13)).pack()

    global from_var, to_var, date_var, num_passengers_var
    from_var = StringVar()
    to_var = StringVar()
    date_var = StringVar()
    num_passengers_var = StringVar()

    Label(booking_screen, text="From:",font=("G7 Cube 5",10),bg='honeydew').pack()
    from_entry = Entry(booking_screen, textvariable=from_var)
    from_entry.pack(pady=2)

    Label(booking_screen, text="To:",font=("G7 Cube 5",10),bg='honeydew').pack()
    to_entry = Entry(booking_screen, textvariable=to_var)
    to_entry.pack(pady=2)

    Label(booking_screen, text="Date of Journey:",font=("G7 Cube 5",10),bg='honeydew').pack()
    date_entry = Entry(booking_screen, textvariable=date_var)
    date_entry.pack(pady=2)

    Label(booking_screen, text="Number of Passengers:",font=("G7 Cube 5",10),bg='honeydew').pack()
    num_passengers_entry = Entry(booking_screen, textvariable=num_passengers_var)
    num_passengers_entry.pack(pady=2)

    Button(booking_screen, text="Submit", width=10, height=1,font=("G7 Cube 5",10), bg="lime", command=lambda:(booking_screen.destroy(),book_bus(),create_snack_page())).pack(pady=5)
    booking_screen.mainloop()



