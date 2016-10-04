while True:
    invoer = input("Geef een string met vier letters: ")
    if len(invoer) != 4:
        print(str(invoer)+' heeft '+str(len(invoer))+' letters')
    else:
        print('Inlezen van correcte string: '+invoer+' is geslaagd')
        break
