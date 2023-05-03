from tkinter import *
import requests

url = "https://openexchangerates.org/api/latest.json"
app_id = "5eb1d42f11974e569217fba7330f7b05"


def convert_currency():
    try:
        amount = float(amount_entry.get())
        from_currency = from_currency_var.get()
        to_currency = to_currency_var.get()

        params = {"app_id": app_id, "symbols": f"{from_currency},{to_currency}"}
        response = requests.get(url, params=params)
        data = response.json()

        rate = data["rates"][to_currency] / data["rates"][from_currency]
        result = amount * rate

        result_label.config(text=f"{result:.2f}")
    except ValueError:
        result_label.config(text="Invalid input")
    except KeyError:
        result_label.config(text="Invalid currency")


root = Tk()
root.title("Currency Converter")
root.configure(background="black")

#! create input widgets
amount_label = Label(root, text="Amount:", bg="black", fg="white")
amount_entry = Entry(root)
from_currency_label = Label(root, text="From currency:", bg="black", fg="white")
from_currency_var = StringVar(root)
from_currency_var.set("USD")
from_currency_menu = OptionMenu(
    root,
    from_currency_var,
    "USD",
    "EUR",
    "GBP",
    "UAH",
    "PLN",
    "INR",
    "JPY",
    "CNY",
    "CAD",
    "CHF",
)
to_currency_label = Label(root, text="To currency:", bg="black", fg="white")
to_currency_var = StringVar(root)
to_currency_var.set("EUR")
to_currency_menu = OptionMenu(
    root,
    to_currency_var,
    "USD",
    "EUR",
    "GBP",
    "UAH",
    "PLN",
    "INR",
    "JPY",
    "CNY",
    "CAD",
    "CHF",
)
convert_button = Button(
    root, text="Convert", bg="red", fg="white", command=convert_currency
)

result_label = Label(
    root, text="Result:", font=("Arial", 22, "bold"), bg="black", fg="white"
)

#! layout input widgets
amount_label.grid(row=0, column=0, padx=10, pady=10)
amount_entry.grid(row=0, column=1, padx=10, pady=10)
from_currency_label.grid(row=1, column=0, padx=10, pady=10)
from_currency_menu.grid(row=1, column=1, padx=10, pady=10)
to_currency_label.grid(row=2, column=0, padx=10, pady=10)
to_currency_menu.grid(row=2, column=1, padx=10, pady=10)
convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
result_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

root.mainloop()
