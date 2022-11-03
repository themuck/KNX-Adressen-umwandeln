eingabe = ''

while eingabe != 'quit':

    eingabe = input('KNX Adresse eingeben: \n')

    if eingabe.count('/') == 1:
        print('Format H/U erkannt, konvertiere zu H/M/U')
        array = eingabe.split('/')
        print(array[0]+ '/' + str(int(array[1])//256) + '/' + str(int(array[1])%256)+'\n')

    elif eingabe.count('/') == 2:
        print('Format H/M/U erkannt, konvertiere zu H/U')
        array = eingabe.split('/')
        print(array[0] + '/' + str(int(array[1]) * 256 + int(array[2])) +'\n')

    elif eingabe != 'quit':
        print('Falsches Format, H/M/U oder H/U'+'\n')

