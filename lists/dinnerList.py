'''
If you could invite anyone, living or deceased, to dinner, who would you invite? Make a list that includes at least three people you’d like to invite to dinner. Then use your list to print a message to each person, inviting them to dinner.
'''

list = ['Rafael Nadal','Juan Ramon Rallo']
mensaje = ""
list.insert(0,'Nassim Taleb')
list.append('Mike Rother')
list.pop(len(list)-1)
for name in map(str,list):
    mensaje += f"I would like to invite {name} to dinner with my family."

print(mensaje)
list.append('Pedro X')
list.remove('Pedro X')

