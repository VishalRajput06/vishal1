from tkinter import *
from tkinter import ttk
import requests
import json

# Colors
cor0 = "#FFFFFF"
cor1 = "#333333"
cor2 = "#EB5D51"

# Initialize main window
window = Tk()
window.geometry('315x400')
window.title('Currency Converter')
window.configure(bg=cor2)
window.resizable(height=FALSE, width=FALSE)

# Header label
label = Label(window, text='Currency Converter', height=3, bg=cor2, fg='white', font=('Ivy 12 bold'))
label.place(x=85, y=0)

# Frames
top = Frame(window, width=500, height=60, bg=cor2)
top.grid(row=0, column=1)

main = Frame(window, width=500, height=400, bg=cor0)
main.grid(row=1, column=0)

# Convert function
def convert():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    # Input currencies and amount
    currency_1 = combo1.get()
    currency_2 = combo2.get()
    amount = value.get()

    try:
        amount = float(amount)  # Validate input as a float
    except ValueError:
        result.config(text="Invalid Amount")
        return

    querystring = {"from": currency_1, "to": currency_2, "amount": amount}

    headers = {
        "x-rapidapi-key": "c9a9b32df0msh3454297ef156af1p127862jsn3085881a44ac",  
        "x-rapidapi-host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        try:
            data = response.json()
            converted_amount = data.get("result", {}).get("convertedAmount")
            if converted_amount is not None:
                formatted = "{:,.2f}".format(converted_amount)
                result.config(text=f"{formatted} {currency_2}")
            else:
                result.config(text="Conversion Error")
        except json.JSONDecodeError:
            result.config(text="Error parsing response")
    else:
        result.config(text="result_failed")

# Main Frame
result = Label(main, text="", width=17, height=2, pady=7, relief=SOLID, anchor=CENTER, font=('Ivy 15 bold'), bg=cor0, fg=cor1)
result.place(x=50, y=10)

currency = ['CAD', 'BRL', 'EUR', 'INR', 'USD']

from_label = Label(main, text="From", width=8, height=1, pady=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=cor0, fg=cor1)
from_label.place(x=48, y=90)

combo1 = ttk.Combobox(main, width=8, justify=CENTER, font=('Ivy 12 bold'))
combo1['values'] = currency
combo1.place(x=50, y=115)

to_label = Label(main, text="To", width=8, pady=0, relief="flat", anchor=NW, font=('Ivy 10 bold'), bg=cor0, fg=cor1)
to_label.place(x=158, y=90)

combo2 = ttk.Combobox(main, width=8, justify=CENTER, font=('Ivy 12 bold'))
combo2['values'] = currency
combo2.place(x=168, y=115)

value = Entry(main, width=23, justify=CENTER, font=('Ivy 12 bold'), relief=SOLID)
value.place(x=50, y=190)

Button = Button(main, text="Convert", width=20, padx=5, height=1, bg=cor2, fg=cor0, font=('Ivy 12 bold'), command=convert)
Button.place(x=50, y=240)

window.mainloop(
