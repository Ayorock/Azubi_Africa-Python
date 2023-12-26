food_charge = int(input('Enter the Charge for Food:  '))
tip_charge = 0.18*food_charge
sale_tax = 0.07*food_charge
grand_total = food_charge + tip_charge + sale_tax

print(f'Tip = ${tip_charge}')
print(f'Sales Tax = ${sale_tax}')
print(f'Grand Total = ${grand_total}')
