item = {}
shooping_cart = []
i = 0
ask = input('Do you want to Add item( Yes/No): ')
num = int(input('How many items: '))
if ask == 'Yes':
    while i < num:
        item['Name']= input('Enter items name: ')
        item['Price'] = int(input('Enter item price: $'))
        shooping_cart.append(item)
        print(shooping_cart)
        i= i+1
        print(shooping_cart)
           
else:
    while i < num:
        item['Name']= input('Enter name of item to remove: ')
        shooping_cart = []
        shooping_cart.remove(item)
        i = i + 1
#for item in shooping_cart:
 #   print(shooping_cart)


#names = ['Ayobami', 'Aborisade']
#score = []
#score.insert(0, 97)
#score.append(98)

#print(len(names))
#names.insert(0, 'Adebayo')
#names.insert(0, 'Kareem')
#print(names)
#names.sort()
#print(names)
#print(names[3:])
#print(score)

#from array import array
#score = array('d')
#score.append(98)
#score.append(99)
#print(score)
#print(score[0])

#person = {'first': 'Ayobami'}
#person['last'] = 'Aborisade'
#print(person)
#print(person['first'].upper())

#ayobami = {}
#ayobami['first'] = 'Ayobami'
#ayobami['last'] = 'Aborisade'
#mohammed = {}
#mohammed['first'] = 'Mohammed'
#mohammed['last'] = 'Abdulkabir'

#people = []
#people.append(ayobami)
#people.append(mohammed)
#people.append({'first': 'Kola', 'last': 'Olukosi'})

#print(people)
#print(len(people))