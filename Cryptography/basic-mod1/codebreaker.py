with open("/opt/CTFs/PicoGym/basic-mod1/message.txt", "r") as file:
    line = file.read()
    linelist = line.split()
    # print(linelist)
    modtext = []
    for x in linelist:
        x = int(x) % 37
        # print(x)
        modtext.append(x)
    # print(modtext)
    newstring = ' '.join(str(e) for e in modtext)
    # print(newstring)
    intab = newstring
    zipstring1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",0,1,2,3,4,5,6,7,8,9,"_"]
    zipstring2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
    chrdict = dict(zip(zipstring2, zipstring1))
    print(chrdict)
    translist = []
    for x in modtext:
        print(x)
        letter = chrdict.get(x)
        print(letter)
        translist.append(letter)
    
    print(translist)
transstring = ''.join(str(e) for e in translist)
print(f'picoCTF{{{transstring}}}')
    

    
file.close()

