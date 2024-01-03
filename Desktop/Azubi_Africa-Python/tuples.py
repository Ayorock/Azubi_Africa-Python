color = {"Red" : "Rot", "Green" : "Grun", "Blue": "Blau", "Yellow": "Gelb"}
print (color)
add_colore = input("Mention color in English:  ")
add_colorg = input("Mention the German translation: ")
color[add_colore] = add_colorg
print (color)
print(color.keys())

eng_color = input("Enter the English color: ")
print("The German Translation is ", color[eng_color])

