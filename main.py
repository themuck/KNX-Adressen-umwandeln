loop = True

print('KNX Gruppenadressen Konverter von the_muck V0.01 \n')

while loop:

    eingabe = input('KNX Adresse eingeben: ')

    if eingabe.count('/') == 1:
        print('Format H/U erkannt, konvertiere zu H/M/U.')
        array = eingabe.split('/')
        if int(array[0]) > 31 or int(array[1]) > 2047:
            print('Falscher Adressbereich!' + '\n')
        else:
            print('-> ' +array[0]+ '/' + str(int(array[1])//256) + '/' + str(int(array[1])%256)+'\n')

    elif eingabe.count('/') == 2:
        print('Format H/M/U erkannt, konvertiere zu H/U.')
        array = eingabe.split('/')
        if int(array[0]) > 31 or int(array[1]) > 7 or int(array[2]) > 255:
            print('Falscher Adressbereich!' + '\n')
        else:
            print('-> ' + array[0] + '/' + str(int(array[1]) * 256 + int(array[2])) +'\n')

    else:
        print('Falsches Format, H/M/U oder H/U!'+'\n')

