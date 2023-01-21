import math
import random

class Player:
    def __init__(self, coin_amount,grain_amount,wood_amount,metal_amount):
        self.coin_amount = coin_amount
        self.grain_amount = grain_amount
        self.wood_amount = wood_amount
        self.metal_amount = metal_amount

pl1 = Player(5000,100,150,200)


metal_range = [2500,2600,2700,2800,2900,3000]
wood_range = [450,500,550,600,650,700,750,800]
grain_range = [20,25,30,35,40,45,50,55,60]

#amsterdam prices
ams_metal_price = random.choice(metal_range)
ams_wood_price = random.choice(wood_range)
ams_grain_price = random.choice(grain_range)

#paris prices
prs_metal_price = random.choice(metal_range)
prs_wood_price = random.choice(wood_range)
prs_grain_price = random.choice(grain_range)

#london prices
lndn_metal_price = random.choice(metal_range)
lndn_wood_price = random.choice(wood_range)
lndn_grain_price = random.choice(grain_range)



