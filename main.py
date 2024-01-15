# pip install beautifulsoup4 requests

# Imports
from tkinter import *
from tkinter import ttk, messagebox
import requests
import bs4

HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

# Set Up Window
root = Tk()
root.title("Simple Stock Scraper")
root.geometry("400x200")

def fetch_stock_price(symbol):
	t = requests.get(f"https://www.google.com/search?q={symbol}+stock+price", headers=HEADERS)
	soup = bs4.BeautifulSoup(t.text, "html.parser")
	try:
		s = soup.find("div", class_="iBp4i").text.split()
		s.append(soup.find("div", class_="nXE3Ob").text.split()[8])
		s[1] = float(s[1])
		return s
	except AttributeError:
		return -1

def __fetch():
	res = fetch_stock_price(ebox.get())
	if res == -1:
		messagebox.showerror(title="Invalid", message="Stock data was not found or stock symbol was invalid.")
	else:
		res[2] = res[2][1:len(res[2]) - 1]
		if res[1] < 0:
			s2 = f"Down {res[2]} by {res[1]}"
		else:
			s2 = f"Up {res[2]} by +{res[1]}"
		messagebox.showinfo(title=ebox.get().upper() + " Price", message = f"{res[0]} {res[3]}, {s2} {res[3]}")
	ebox.delete(0, END)

# Widgets
check_button = Button(root, text="Calculate Price", command=__fetch)
check_button.pack()
check_label = Label(root, text = "Enter Stock Symbol:")
check_label.pack()
ebox = Entry(root)
ebox.pack()

# Run The GUI
root.tk.call('source', 'forest-dark.tcl') # Source - https://github.com/rdbende/Forest-ttk-theme
ttk.Style().theme_use('forest-dark') ###########################################################
root.mainloop()