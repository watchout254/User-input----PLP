def calculate_discount(price, dis_percent):
    if dis_percent >= 20:
        discntd_price = price * (dis_percent / 100)
        mwisho_price = price - discntd_price
        return mwisho_price
    else:
        return price
    
print("Welcome to Mukenyas Shop");
origi = int(input("Whats the original price of the item you've bought(KES)? "))
dis = int(input("Whats the discount percentage of the item(20%)? "))

mwisho = calculate_discount(origi,dis)

print(f"Final price after the discount is: KES {mwisho}")