gondolt_szám = 3
tipp = input('Melyik számra gondolok 1 és 5 között? ')
tipp = int(tipp)
if gondolt_szám == tipp: # a gondolt szám egyenlő a tippel?
    print('Eltaláltad!')
    print('Bingó!')
else: #különben
    print('Nem talált.')
    print('Probálkoz később újra.')
print('Viszlát!')