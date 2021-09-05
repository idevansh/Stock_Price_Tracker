import requests
from bs4 import BeautifulSoup
from tkinter import *


def PriceParser(company_url):
    url = requests.get(company_url)
    content = url.content
    soup = BeautifulSoup(content, "html.parser")
    price = soup.find("span", {"class": "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)"})
    price = price.get_text()
    price = str(price)
    if "," in price:
        price = price.replace(",", "")
    return price



def increment(company_url):
    url = requests.get(company_url)
    content = url.content
    soup = BeautifulSoup(content, "html.parser")
    increment_of_stock = soup.find("span", {"class": "Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)"})
    if increment_of_stock == None:
        increment_of_stock = soup.find("span", {"class":"Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)"})
    return increment_of_stock.get_text()


def color_decider(increment):
    increment = str(increment)
    if increment.startswith("-"):
        return "red"
    else:
        return "green"

def run(company_name, need):
        if company_name == "facebook" and need == "price":
            return  PriceParser("https://finance.yahoo.com/quote/FB?p=FB&.tsrc=fin-srch")
        elif company_name == "facebook" and need == "incre":
            return increment("https://finance.yahoo.com/quote/FB?p=FB&.tsrc=fin-srch")
        elif company_name == "microsoft" and need == "price":
            return  PriceParser("https://finance.yahoo.com/quote/MSFT?p=MSFT&.tsrc=fin-srch")
        elif company_name == "microsoft" and need == "incre":
            return increment("https://finance.yahoo.com/quote/MSFT?p=MSFT&.tsrc=fin-srch")
        elif company_name == "apple" and need == "price":
            return PriceParser("https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch")
        elif company_name == "apple" and need == "incre":
            return increment("https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch")
        elif company_name == "google" and need == "price":
            return PriceParser("https://finance.yahoo.com/quote/GOOGL?p=GOOGL&.tsrc=fin-srch")
        elif company_name == "google" and need == "incre":
            return increment("https://finance.yahoo.com/quote/GOOGL?p=GOOGL&.tsrc=fin-srch")



root = Tk()
root.minsize(644, 343)
root.maxsize(644, 343)
root.title("Stock Prices Tracker")
facebook_display = Label(root, text="Facebook : ", font=('Helvatical bold',20))
facebook_price_display = Label(root, text=run("facebook", 'price'), font=('Helvatical bold',20))
facebook_incre_display = Label(root, text=run("facebook", 'incre'), fg = color_decider(run("facebook", 'incre')), font=('Helvatical bold',20))
facebook_display.grid(row= 0, column=0)
facebook_price_display.grid(row= 0, column=1)
facebook_incre_display.grid(row=0, column=2)
google_display = Label(root, text="Google : ", font=('Helvatical bold',20))
google_price_display = Label(root, text=run("google", "price"), font= ("Helvatical bold", 20))
google_incre_display = Label(root, text=run("google", "incre") , font = ("Helvatica bold", 20) , fg= color_decider(run("google", "incre")))
microsoft_display = Label(root, text="Microsoft : ", font=("Helvatica bold", 20))
microsoft_price_display = Label(root, text=run("microsoft", "price"), font=("Helvatica bold", 20))
microsoft_incre_display = Label(root, text=run("microsoft", "incre"), fg = color_decider(run("microsoft", "incre")), font=("Helvatica bold", 20))
apple_display = Label(root, text="Apple : ", font=("Helvatica bold", 20))
apple_price_display = Label(root, text=run("apple", "price"), font=("Helvatica bold", 20))
apple_incre_display = Label(root, text=run("apple", "incre"), fg = color_decider(run("apple", "incre")), font=("Helvatica bold", 20))
apple_display.grid(row=3, column=0)
apple_price_display.grid(row=3, column=1)
apple_incre_display.grid(row=3, column=2)
microsoft_display.grid(row=2, column=0)
microsoft_price_display.grid(row=2, column=1)
microsoft_incre_display.grid(row=2, column=2)
google_display.grid(row=1, column=0)
google_price_display.grid(row= 1, column=1)
google_incre_display.grid(row=1, column=2)
facebook_display.mainloop()
facebook_price_display.mainloop()
facebook_incre_display.mainloop()
google_display.mainloop()
google_price_display.mainloop()
google_incre_display.mainloop()
microsoft_display.mainloop()
microsoft_price_display.mainloop()
microsoft_incre_display.mainloop()
apple_display.mainloop()
apple_price_display.mainloop()
apple_incre_display.mainloop()