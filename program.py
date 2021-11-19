import hashlib
loop = True
help = "This program allows you to:\n [1] or [list] - Lists contents of a baza.txt file.\n [2] or [add] - Inserts new entry into baza.txt file, format: name surrname \n [3] or [delete] - Deletes entry specified with line nr. e.g. delete 1\n [4] or [save-sum] - Store md5 checkum in baza.sum file.\n [5] or [check-sum] - Compares current md5 checksum with checksum stored in baza.sum file.\n To exit program type [q] or [quit]." 
print("Type h for help.")
while loop:
    commands = input().split(' ')
    if commands[0] == 'h' or commands[0] == 'help':
        print(help)
    elif commands[0] == '1' or commands[0] == 'list':
        try:
            with open('baza.txt','r') as baza:
                print(baza.read())
        except:
            print("File baza.txt does not exist or you have no permissions to read it. Aborting program")
            break
    elif commands[0] == '2' or commands[0] == 'add':
        try:
            commands[1]
            commands[2]
            ip_addr = 2
            ip_status = True
            with open('baza.txt','r') as baza:
                baza_lines = baza.readlines()
                for line in baza_lines:
                    index = int(line[0].replace('.','')) + 1
                while ip_status:
                    ip_status = False
                    for line in baza_lines:
                        if ip_addr == int(line.split(' ')[3].split('.')[3]):
                            ip_addr += 1
                            ip_status = True
            if ip_addr < 255:
                with open('baza.txt', 'a') as baza:
                    baza.write(str(index) + '. '+  commands[1] + ' ' +  commands[2] + ' 10.0.0.' + str(ip_addr) + '\n' )
                    print("Record added")
            else:
                print("No free addresses left")
        except:
            print("Provide name and surname as parameters. Type h for help")
    elif commands[0] ==  '3' or commands[0] == 'delete':
        try:
            commands[1]
            with open('baza.txt','r') as baza:
                baza_lines = baza.readlines()
            
            with open('baza.txt','w') as baza:
                status = True
                for line in baza_lines:
                    if line[0].replace('.','') != commands[1]:
                        baza.write(line)
                    else:
                        status = False
                if status is True:
                    print("Wrong line number provided. Nothing has been deleted")
                else:
                    print("Record deleted")
        except:
            print("You need to provide record id. Check h for help.")
    elif commands[0] == '4' or commands[0] == 'save-sum':
        try:
            md5Sum = hashlib.md5()
            with open('baza.txt', 'rb') as baza:
                for chunk in iter(lambda: baza.read(4096), b''):
                    md5Sum.update(chunk)
            with open('baza.sum', 'w') as bazaSum:
                bazaSum.write(md5Sum.hexdigest())
        except:
            print("baza.txt does not exists or you have no permissions to read it")
    elif commands[0] == '5' or commands[0] == 'check-sum':
        try:
            md5Sum = hashlib.md5()
            with open('baza.txt', 'rb') as baza:
                for chunk in iter(lambda: baza.read(4096), b''):
                    md5Sum.update(chunk)
            with open('baza.sum', 'r') as bazaSum:
                if bazaSum.readline() == str(md5Sum.hexdigest()):
                   print("baza.txt has not been changed")
                else:
                    print("baza.txt has been changed")
        except:
            print("Check if needed files (baza.txt, baza.sum) exists and you have read permissions")
    elif commands[0] == 'q' or commands[0] == 'quit':
        break
    else:
        print("Incorrect syntax. Please type h or help for help")
