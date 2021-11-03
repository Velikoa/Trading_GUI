#GUI application

import Tkinter as tk
import Share_price_info as kio_file
import GUI_testing as stats
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("TkAgg")            #This is the backend of matplotlib
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
import GUI_testing as testing


#Creating the parent window
root = tk.Tk()
f = tk.Frame(root)

#Title for window
root.title("My first GUI")

#Size of the window - min and max
root.maxsize(850, 850)
root.minsize(250, 250)

#Setting a fixed size of window on opening
root.geometry("800x750")

#Setting the background colour
root.configure(background="white")


#Welcome label - pack tells Tk to fit the text to the given window
title = tk.Label(root, text="Trading Platform", fg="black", font="Helvetica 20 bold", bg="grey")
title.grid(row=0, columnspan=3)

#Logo for top
topimg = tk.PhotoImage(file="stock_market.gif")
stock_img = tk.Label(root, image=topimg, bg="black")
stock_img.grid(row=1, columnspan=3)

#Button to start trading
trade_btn = tk.Label(root, text="Select the company you wish to analyse from the list below:", wraplength=200, justify="left", bg="black", fg="white", width=50, height=2)
trade_btn.grid(row=2, column=1, sticky="W", padx=5, pady=5)

#Entry to type which share you want to find info for
# search = tk.Entry(root)
# search.grid(row=2, column=1, sticky="W")

#Function to print out what has been searched for in the Entry bar
# def search_bar():
#     print search.get()
#     kio_file.share_price()
#     #if search.get() == "kio":
#         #use the information from the share info script
#         #kio_file.share_price()

#Serach button that prints out whatever was typed into the search Entry - command is the same as the function being called to print
#tk.Button(root, text="Search", command=search_bar) .grid(row=3, column=1, sticky="W")

#Button to leave trading platform. When pressed closes program.
exit_btn = tk.Button(root, text="Exit Platform", bg="black", fg="white", width=20, height=2, command=root.destroy)
exit_btn.grid(row=4, column=2, sticky="E")



#Label that prints the share info when the "KIO info" button is clicked
currentPrice = tk.StringVar(root, "Click for share info")    #You need to do this in order to use the "textvariable" later in the Label.
currentMovement = tk.StringVar(root, "Click for share info")

def setValues():
    price = kio_file.kio_price
    print price
    currentPrice.set(price)
    #Call the function - notice placing the () at the end.
    movement = kio_file.share_movement()
    print movement
    currentMovement.set(movement)

def moving_averages():
    sma = testing.moving_averages()
    print sma

def MACD():
    MACD = testing.MACD()
    print MACD

def kio_annual_graph():
    annual_price = stats.price_over_one_year()
    #f = Figure(figsize=(5, 5), dpi=100)

    canvas = FigureCanvasTkAgg(annual_price, master=root)
    canvas.show()
    canvas.get_tk_widget().grid(row=1, column=3, sticky="E")

def forex():
    forex = testing.share_vs_currency()
    print forex

def KIO_vs_IronOre():
    IronOre = testing.iron_ore_price_vs_share()
    print IronOre

def RSI():
    rsi = testing.RSI()
    print rsi

#When click on the share interested in, a new window will open for that share.
def kio_window():
    top = tk.Toplevel()    #Create the variable inside otherwise if its global the window opens up before you click.
    top.title("Kumba Iron Ore")
    # Setting a fixed size of window on opening
    top.geometry("1000x850")
    # Setting the background colour
    top.configure(background="white")

    #The main heading
    title_kio = tk.Label(top, text="Kumba Iron Ore", font="Helvetica 20 bold")
    title_kio.grid(row=0, column= 0)

    kio_img = tk.PhotoImage(file="kumba_locations.gif")
    kio_top_img = tk.Label(top, image=kio_img, bg="black")
    kio_top_img.image = kio_img    #keep a reference of the image or else it will not display.
    kio_top_img.grid(row=1, column=0)


    # When button is clicked, the function as part of the "command" widget in the button code will run and the "textvariable" here
    # which is linked to it will also be activated.
    kio_printout = tk.Label(top, textvariable=currentPrice, bg='black', fg="white", width=30, height=3)
    kio_printout.grid(row=4, column=0, padx=3, pady=5)

    kio_printout = tk.Label(top, textvariable=currentMovement, bg='black', fg="white", width=30, height=3)
    kio_printout.grid(row=5, column=0, padx=3, pady=5)

    # When push the button the share details print out
    kio = tk.Button(top, text="KIO info", bg="black", fg="white", width=30, height=2, command=setValues)
    kio.grid(row=4, column=0, sticky="W", padx=5, pady=5)

    #Button to exit kio
    exit_kio = tk.Button(top, text="Exit", bg="black", fg="white", width=30, height=2, command=top.destroy)
    exit_kio.grid(row=10, column=0, sticky="E")

    #Placing the time vs price graph in the window

    kio = tk.Button(top, text="Time vs Price Graph - One Year", bg="black", fg="white", width=30, height=2, command=kio_annual_graph)
    kio.grid(row=7, column=0, sticky="W", padx=5, pady=5)

    kio_sma = tk.Button(top, text="9-day & 21-day simple moving averages", bg="black", fg="white", width=30, height=2, command=moving_averages)
    kio_sma.grid(row=8, column=0, sticky="W", padx=7, pady=7)

    #MACD Button and info
    kio_MACD = tk.Button(top, text="MACD", bg="black", fg="white", width=30, height=2, command=MACD)
    kio_MACD.grid(row=9, column=0, sticky="W", padx=5, pady=5)

    #KIO price versus the USD-ZAR
    kio_forex = tk.Button(top, text="KIO price versus USD-ZAR movement", bg="black", fg="white", width=30, height=2, command=forex)
    kio_forex.grid(row=8, column=0, sticky="E")

    #KIO price versus the Iron Ore Spot Price
    KIO_Spot = tk.Button(top, text="KIO Share vs Iron Ore Spot Price", bg="black", fg="white", width=30, height=2, command=KIO_vs_IronOre)
    KIO_Spot.grid(row=7, column=0, sticky="E")

    #RSI
    KIO_RSI = tk.Button(top, text="RSI", bg="black", fg="white", width=30, height=2, command=RSI)
    KIO_RSI.grid(row=9, column=0, sticky="E")


window = tk.Button(root, text="Click for KIO Info", width=20, height=2, command=kio_window)
window.grid(row=6, column=0, sticky="W", padx=5, pady=5)







#print root.grid_size()




#Run the program
root.mainloop()
