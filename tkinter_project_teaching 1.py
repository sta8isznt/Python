#import statements
import tkinter as tk 
from tkinter import messagebox
import sqlite3

#fucttionalitties

def init_db():
    conn = sqlite3.connect("Stocks.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stocks(
            ticker TEXT PRIMARY KEY,
            quantity INTEGER,
            price REAL
        )
    ''')
    conn.commit()
    conn.close()
    
def add_stock():
    ticker = stock_entry.get().strip().upper()
    quantity = quantity_entry.get().strip()
    price = price_entry.get().strip()

    quantity = int(quantity)
    price = float(price)

    conn = sqlite3.connect('Stocks.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO stocks (ticker, quantity, price) VALUES (?,?,?)
                   ''', (ticker, quantity, price))
    conn.commit()
    conn.close()

    stock_entry.delete(0, tk.END)
    quantity_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)

#coontect to database 
init_db()




#GUI
root = tk.Tk()
root.title("Stocks")

#labels
stock_label = tk.Label(root , text="Stock")
stock_label.grid(row=0,column=0,padx=5,pady=5)
quantity_label = tk.Label(root , text="Quanity")
quantity_label.grid(row=1,column=0,padx=5,pady=5)
price_label = tk.Label(root, text = "Price")
price_label.grid(row=2,column=0,padx=5,pady=5)


#textfields
stock_entry = tk.Entry(root)
stock_entry.grid(row=0 , column=1,padx=5,pady=5)
quantity_entry = tk.Entry(root)
quantity_entry.grid(row=1,column=1,padx=5,pady=5)
price_entry = tk.Entry(root)
price_entry.grid(row=2 , column=1,padx=5,pady=5)

#buttons
add_stock_button = tk.Button(root,text="Add Stock",command=add_stock)
add_stock_button.grid(row=3,column=0,padx=5,pady=5)



#main loop
root.mainloop()
