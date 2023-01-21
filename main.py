import tkinter as tk
import construct
import maincalc
from PIL import Image, ImageTk

menu = tk.Tk()

#first window
construct.build.create_window(menu, "930x760", "The Sea Trader")

#sea condition
global loc
loc = ""
trl_loc = "london"


def hideLabel():
    l1 = construct.build.createLabel(menu, f"Location:           ", 570, 10, 15)

def createLabel11(place):
    l1 = construct.build.createLabel(menu, "Location:              ", 570, 10, 15)
    if place == 'Amster':
        l1 = construct.build.createLabel(menu, "Location: Amster", 570, 10, 15)
    elif place == 'Paris':
        l1 = construct.build.createLabel(menu, f"Location: Paris", 570, 10, 15)
    elif place == 'London':
        l1 = construct.build.createLabel(menu, f"Location: London", 570, 10, 15)

def checkBuy(metrial,playerMoney,kindOf):
    if metrial <= playerMoney:
        construct.build.createLabel(menu, "Coins: " + str(playerMoney - metrial), 840, 10, 10)
        construct.build.createLabel(menu, "Grain: " + str(kindOf + metrial) , 840, 40, 10)
    else:
        print("u cant buy")

def checkSell(metrialAmount, playerMoney, playerMetrial,kindOff):
    if metrialAmount <= playerMoney:
        if kindOff == 'grain':
            construct.build.createLabel(menu, "Coins: " + str(playerMoney + metrialAmount), 840, 10, 10)
            construct.build.createLabel(menu, "Grain: " + str(playerMetrial - metrialAmount), 840, 40, 10)
        elif kindOff == 'wood':
            construct.build.createLabel(menu, "Coins: " + str(playerMoney + metrialAmount), 840, 10, 10)
            construct.build.createLabel(menu, "Wood: " + str(playerMetrial - metrialAmount), 840, 70, 10)
        elif kindOff == 'metal':
            construct.build.createLabel(menu, "Coins: " + str(playerMoney + metrialAmount), 840, 10, 10)
            construct.build.createLabel(menu, "Metal: " + str(playerMetrial - metrialAmount), 840, 100, 10)
    else:
        print("u cant sell")






#true inventory (takes from object)
player_coins = str(maincalc.pl1.coin_amount)
player_grain = str(maincalc.pl1.grain_amount)
player_wood = str(maincalc.pl1.wood_amount)
player_metal = str(maincalc.pl1.metal_amount)

#inventory
construct.build.createLabel(menu, "Inventory: " , 735,10, 15)
construct.build.createLabel(menu, "Coins: " + player_coins, 840,10, 10)
construct.build.createLabel(menu, "Grain: " + player_grain, 840,40, 10)
construct.build.createLabel(menu, "Wood: " + player_wood, 840,70, 10)
construct.build.createLabel(menu, "Metal: " + player_metal, 840,100, 10)

#buttons
#buy buttons
construct.build.createBtn(menu, "Buy: Grain", 570, 140, 100, 50, lambda:checkBuy(int(lndn_grain),int(player_coins),int(player_grain)), 15, "pictures/grain2.jpg")
construct.build.createBtn(menu, "Buy: Wood", 695, 140, 100, 50, lambda:checkBuy(int(lndn_wood),int(player_coins),int(player_wood)), 15, "pictures/wood2.jpg")
construct.build.createBtn(menu, "Buy: Metal", 820, 140, 100, 50, lambda:checkBuy(int(lndn_metal),int(player_coins),int(player_metal)), 15, 'pictures/metal.jpg')

#sell buttons
construct.build.createBtn(menu, "Sell: Grains", 570, 200, 100,50, lambda:checkSell(int(lndn_grain),int(player_coins),int(player_grain),'grain'), 15, 'pictures/grain2.jpg')
construct.build.createBtn(menu, "Sell: Wood", 695, 200, 100,50, lambda:checkBuy(int(lndn_wood),int(player_coins),int(player_wood)), 15, 'pictures/wood2.jpg')
construct.build.createBtn(menu, "Sell: Metal", 820, 200, 100,50, lambda:checkBuy(int(lndn_metal),int(player_coins),int(player_metal)), 15, 'pictures/metal.jpg')

#travel buttons
construct.build.createBtn(menu, "Amsterdam", 570, 260, 100,50, lambda:createLabel11("Amster") , 15, 'pictures/travel.jpg')
construct.build.createBtn(menu, "Paris", 695, 260, 100,50, lambda:createLabel11("Paris"), 15, 'pictures/travel.jpg')
construct.build.createBtn(menu, "London", 820, 260, 100,50, lambda:createLabel11("London"), 15, 'pictures/travel.jpg')

#location
l1 = construct.build.createLabel(menu, f"Location:           ", 570, 10, 15)





#bank button
construct.build.createBtn(menu, "Bank", 570, 320, 350,50,lambda:print("bank"), 30, "pictures/bank.jpg")

#rest button
construct.build.createBtn(menu, "Rest a Day", 570, 380, 350,50, lambda:print("rest"), 30, 'pictures/restaday.jpg')


#icon adding
construct.build.create_icon(menu, 'pictures/gameco.jpg')

#basic window
construct.build.create_img(menu, 5, 10, 550, 425, 'pictures/ship1.jpg')

#amsterdam imported prices
ams_metal = str(maincalc.ams_metal_price)
ams_wood = str(maincalc.ams_wood_price)
ams_grain = str(maincalc.ams_grain_price)

#amsterdam labels
construct.build.create_img(menu, 5, 450, 305, 300, 'pictures/oldamsterdam.jpg')
construct.build.createLabel(menu, "Amsterdam", 5,450, 15)
construct.build.createLabel(menu, "Grain: " + ams_grain, 5, 500, 15)
construct.build.createLabel(menu, "Wood: " + ams_wood, 5, 550, 15)
construct.build.createLabel(menu, "Metal: " + ams_metal, 5, 600, 15)

#paris prices
prs_metal = str(maincalc.prs_metal_price)
prs_wood = str(maincalc.prs_wood_price)
prs_grain = str(maincalc.prs_grain_price)

#paris
construct.build.create_img(menu, 310, 450, 305, 300, 'pictures/oldparis.jpg')
construct.build.createLabel(menu, "Paris", 310,450, 15)
construct.build.createLabel(menu, "Grain: " + prs_grain, 310, 500, 15)
construct.build.createLabel(menu, "Wood: " + prs_wood, 310, 550, 15)
construct.build.createLabel(menu, "Metal: " + prs_metal, 310, 600, 15)

#london prices
lndn_metal = str(maincalc.lndn_metal_price)
lndn_wood = str(maincalc.lndn_wood_price)
lndn_grain = str(maincalc.lndn_grain_price)

#landon
construct.build.create_img(menu, 615, 450, 305, 300, 'pictures/oldlondon.jpg')
construct.build.createLabel(menu, "London", 615,450, 15)
construct.build.createLabel(menu, "Grain: " + lndn_grain, 615, 500, 15)
construct.build.createLabel(menu, "Wood: " + lndn_wood, 615, 550, 15)
construct.build.createLabel(menu, "Metal: " + lndn_metal, 615, 600, 15)

menu.mainloop()



