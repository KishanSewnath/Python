infile = open('C:/Users/Kishan Sewnath/Desktop/kaartnummers.txt', 'r')
linelist = infile.readlines()
zin = 'Deze file telt {} regels'
zinnetje = (zin.format(len(linelist)))
print(zinnetje)
zinstukmax = max(linelist)
zinstukmax1 = zinstukmax[:6]
regel = linelist.index(zinstukmax) +1
zin1 = 'Het grootste kaartnummer is: {} en dat staat op regel {}'
zinnetje1 = (zin1.format(zinstukmax1, regel))
print(zinnetje1)
