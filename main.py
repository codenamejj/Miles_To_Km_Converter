from tkinter import *

FONT = "Ariel"

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=50, pady=50)
window.minsize(height=200, width=300)
window.maxsize(height=200, width=300)

mile_entry = Entry()
mile_entry.config(width=7)
mile_entry.grid(column=1, row=0)

miles_label = Label()
miles_label.config(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_to_label = Label()
is_equal_to_label.config(text="is equal to")
is_equal_to_label.grid(column=0, row=1)

km_count = Label()
km_count.config(text=0)
km_count.grid(column=1, row=1)

km_label = Label()
km_label.config(text="Km")
km_label.grid(column=2, row=1)


def convert_to_km():
    miles = float(mile_entry.get())
    km = round(miles * 1.60934, 2)
    print(km)
    km_count.config(text=km)


calculate_button = Button()
calculate_button.config(text="Calculate", width=7, command=convert_to_km)
calculate_button.grid(column=1, row=2)

window.mainloop()
