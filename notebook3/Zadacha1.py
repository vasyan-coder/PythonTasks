import string

#alph = list(string.ascii_lowercase)
alphabet = string.ascii_uppercase + string.ascii_lowercase + 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
d = {}
for x in range(len(alphabet)):
    d.update({alphabet[x]: bin(ord(alphabet[x]))[2:]})
print(d)
