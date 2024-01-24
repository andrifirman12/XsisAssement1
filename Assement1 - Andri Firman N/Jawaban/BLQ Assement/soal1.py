def soal2(money):
    #* Items
    items_dict = {
        "Kaca Mata": (500, 600, 700, 800),
        "Baju": (200, 400, 350),
        "Sepatu": (400, 350, 200, 30),
        "Buku": (100, 50, 150),
    }

    #* Cart
    cart = ""
    my_item = 0
    start_money = money

    #* Loop Until Money get 0
    while money != 0:
        for x in items_dict:
            for y in range(0, len(items_dict[x])-1):
                price = items_dict[x][y]
                if money >= price :
                    money = money - price
                    my_item +=1
                    cart = cart + "*" + str(x) + " " + str(items_dict[x][y]) + "\n"
                    break

    #* Print Result
    div = "-------------------------------------------------------"
    return print(div + "\nMoney Input : " + str(start_money) + "\nCurrent Money : " + str(money) + "\nTotal Item : " + str(my_item) + "\n" + cart + div)

soal2(1000)
soal2(1150)