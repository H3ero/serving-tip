WeedP = {1:'Amnesia', 2:'Kush',3:'Chronic'}
W_price = {1:20,2:25,3:35}

print(' Menu\n 1-Amnesia $20\n 2-Kush $25\n',
'3-Chronic $35\n 0-Quit\n')

W_order = input('Select the number of your stream please  \n')

if W_order == '0':
    quit
else:
    try:
        float(W_order)
        if int(W_order) in WeedP:
            W_qtt = input('How many grams sir? \n')
            try:
                W_total = W_price[int(W_order)]*int(W_qtt)
                W_tipV = input('Do you want to tip?\n Y for "yes"\n Any key for "no" \n').upper()
                try:
                    if W_tipV == 'Y':
                        W_tipV = input(' For % press 1\n For $ press 2 \n')
                        try:
                            if W_tipV == '1':
                                W_tipV1 = float(input('How much % sir? \n'))
                                try:
                                    if W_tipV1 >= float(0.01):
                                        print('\n$',W_price[int(W_order)],'x',W_qtt,'g \nSubtotal $',W_total)
                                        print('\nTip of $',"%.2f"%(W_total*(W_tipV1/100)))
                                        print('\nTotal of $',"%.2f"%(W_total*(1+1*(W_tipV1/100))))
                                        print(15*'=')
                                        print('\n',WeedP[int(W_order )],W_qtt,'g')
                                    else:
                                        print('Not valid ')
                                except ValueError:
                                    print('Not valid ')
                            elif W_tipV == '2':
                                W_tipV1 = float(input('How much sir? \n'))
                                try:
                                    if W_tipV1 >= float(0.01):
                                        print('\n$' ,W_price[int(W_order)],'x',W_qtt,'g\nSubtotal $',W_total)
                                        print('\nTip of $',W_tipV1)
                                        print('\nTotal of $',"%.2f"%(W_total+W_tipV1))
                                        print(15*'=')
                                        print('\n',WeedP[int(W_order)],W_qtt,'g')
                                    else:
                                        print('Not valid ')
                                except ValueError:
                                    print('Not valid ')
                            else:
                                print('Not valid ')
                        except ValueError:
                            print('Not valid ')
                    else:
                         print('\nNo tip given ')
                         print('\n$',W_price[int(W_order)],'x',W_qtt,'g')
                         print('\nTotal of $',"%.2f"%round(W_total))
                         print(15*'=')
                         print('\n',WeedP[int(W_order)],W_qtt,'g')
                except ValueError:
                    print('Not valid ')
            except ValueError:
                print('Not valid ')
        else:
            print('Not valid ')
    except:
        print('\n No option for that on the menu. ')
