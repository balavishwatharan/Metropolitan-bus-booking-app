# snack_page.py

from tkinter import *
from book2 import *
main_screen=None
images=[]
snack_entries= []
snack_prices= [20,20,100,15,10]
frame= None
receipt_window= None


snack_options = [     #Snacks details
    {"name": "Chips", "price": "₹20", "image_path": "chips.png"},
    {"name": "Chocolate", "price": "₹20", "image_path": "chocolate.png"},
    {"name": "Popcorn", "price": "₹100", "image_path": "popcorn.png"},
    {"name": "Water", "price": "₹15", "image_path": "water.png"},
    {"name": "biscuits", "price": "₹10", "image_path": "biscuits.png"}
]

def calculate_snack_price():
    try:
        total_snack_price = sum([int(entry.get()) * price for entry, price in zip(snack_entries, snack_prices)])
        return total_snack_price
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for the quantity.")
        return 0
def generate_receipt():     
    global receipt_window

    # Calculate window
    total_snack_price = calculate_snack_price()

    # receipt
    receipt_window = Toplevel(main_screen)
    receipt_window.title("Snack Receipt")

    # Display receipt
    receipt_text = f"Snack Receipt\n" \
                   f"Total Snack Price: ₹{total_snack_price}\n" \
                   f"=============================\n"
    
    for entry, snack, price in zip(snack_entries, snack_options, snack_prices):
        quantity = int(entry.get())
        if quantity > 0:
            receipt_text += f"{snack['name']} x{quantity} : ₹{quantity * price}\n"
    
    receipt_text += f"=============================\n" \
                    f"Total Price: ₹{total_snack_price}\n"

    Label(receipt_window, text=receipt_text).pack()

def continue_button():
    global main_screen

    # calling calculate
    total_snack_price = calculate_snack_price()

    try:
        # receipt format
        with open("receipt.txt", "w", encoding="utf-8") as file:
            file.writelines(f"Snack Receipt\n")
            file.writelines(f"Total Snack Price: ₹{total_snack_price}\n")
            file.writelines(f"=============================\n")
            for entry, snack, price in zip(snack_entries, snack_options, snack_prices):
                quantity = int(entry.get())
                if quantity > 0:
                    file.writelines(f"{snack['name']} x{quantity} : ₹{quantity * price}\n")
            file.writelines(f"=============================\n")
            file.writelines(f"Total Price: ₹{total_snack_price}\n")

        messagebox.showinfo("Success", "Receipt information saved successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


def create_snack_page():
    global main_screen
    global images
    main_screen = Toplevel()
    main_screen.title("Snack Options")
    main_screen.geometry('500x400')
    main_screen.configure(bg='honeydew')

    canvas = Canvas(main_screen,bg='honeydew')
    scrollbar = Scrollbar(main_screen, orient="vertical", command=canvas.yview)
    scrollbar.pack(side="right", fill="y")
    canvas.pack(side="left", fill="both", expand=True)
    canvas.configure(yscrollcommand=scrollbar.set,bg='honeydew')

    frame = Frame(canvas,bg='honeydew')
    canvas.create_window((0, 0), window=frame, anchor="nw")

    def on_frame_configure(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    frame.bind("<Configure>", on_frame_configure)

    i = 0
    m = 0
    for snack in snack_options:    #create snack frame
        name_frame = Frame(frame, bg='honeydew')
        name_frame.grid(row=i, column=m)
        Label(name_frame, text=snack["name"],font=("G7 Cube 5",8), pady=5,bg='honeydew').pack(padx=10)

        price_frame = Frame(frame, bg='honeydew')
        price_frame.grid(row=i, column=m + 2)
        Label(price_frame, text=snack["price"], padx=5, pady=5,bg='honeydew').pack(padx=10)

        image_frame = Frame(frame, bg='honeydew')
        image_frame.grid(row=i, column=m + 4)
        image = PhotoImage(file=snack["image_path"])
        images.append(image)
        image_label = Label(image_frame, image=image, pady=5,bg='honeydew')
        image_label.image = image
        image_label.pack(padx=10)

        entry_frame = Frame(frame, bg='honeydew')
        entry_frame.grid(row=i, column=m + 6)
        quantity_entry = Entry(entry_frame, width=5)
        quantity_entry.pack(padx=10)
        snack_entries.append(quantity_entry)

        i += 1

    Button(main_screen, text="Continue",font=("G7 Cube 5",8), command=continue_button, bg='lime').pack(side=BOTTOM)
    Button(main_screen, text="Receipt",font=("G7 Cube 5",8),command=generate_receipt, bg='lime').pack(side=BOTTOM)
    Button(main_screen, text="Skip",font=("G7 Cube 5",8), command=lambda:(main_screen.destroy(),book()), bg='lime').pack(side=BOTTOM)
    
    main_screen.mainloop()




