import tkinter as tk

def add_stock():
    pass

root = tk.Tk()
root.title("stocks")

#Creating Labels and Entry Boxes
item_name_label = tk.Label(root, text="Stock Ticker:")
item_name_label.grid(row=0, column=0, padx=5, pady=5)
item_name_entry = tk.Entry(root)
item_name_entry.grid(row=0, column=1, padx=5, pady=5)

item_qty_label = tk.Label(root, text="Quantity:")
item_qty_label.grid(row=1, column=0, padx=5, pady=5)
item_qty_entry = tk.Entry(root)
item_qty_entry.grid(row=1, column=1, padx=5, pady=5)

item_price_label = tk.Label(root, text="Price:")
item_price_label.grid(row=2, column=0, padx=5, pady=5)
item_price_entry = tk.Entry(root)
item_price_entry.grid(row=2, column=1, padx=5, pady=5)

#Creating Buttons
add_button = tk.Button(root, text="Add Stock", command=add_stock)
add_button.grid(row=3, column=0, padx=5, pady=5)
root.mainloop()