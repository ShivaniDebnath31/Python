# Create a currency.py program that asks the user for the amount they have in yuan, yen, and won and calculates the total in USD.
yuan = int(input('What do you have left in yuan? '))
yen = int(input('What do you have left in yen? '))
won = int(input('What do you have left in won? '))

total = yuan * 0.15 + yen * 0.0077 + won * 0.00080

print(total)