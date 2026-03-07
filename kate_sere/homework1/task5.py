
name = input('What is your name? ')
purchase = input('What do you want to buy? ')
cost = int(input('How much is it? '))
availability = int(input('How much do you have now? '))
saving = int(input('How much can you save per month? '))
not_enough_money = int(cost) - int(availability)
months_before_purchase = int((not_enough_money/saving))
print (f'Привет {name} На покупку {purchase} тебе не хватает {not_enough_money}')
print(f'Возможность покупки: {availability >= cost}')
print (f'До покупки оставлось {months_before_purchase} месяцев')

