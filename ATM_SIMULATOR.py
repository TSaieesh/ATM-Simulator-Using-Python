'''     USE THIS USERNAME AND PIN
                    user1  ---  1111
                    user2  ---  2222
                    user3  ---  3333
                    user4  ---  4444
'''

#GIVING INSTRUCTIONS TO USER
print('USE THIS USERNAME AND PIN\nuser1  ---  1111\nuser2  ---  2222\nuser3  ---  3333\nuser4  ---  4444')


#creating lists of users , pins and amounts
users=['user1','user2','user3','user4']
pins=['1111','2222','3333','4444']
amounts=[1000,2000,3000,4000]
count=0

#checking given user exists or not
while True:
    user=input('\nENTER USER NAME : ')
    user=user.lower()
    if user in users:
        if user==users[0]:
            n=0
        elif user==users[1]:
            n=1
        elif user==users[2]:
            n=2
        else:
            n=3
        break
    else:
        print('-'*20)
        print('\nINVALID USERNAME')
        print('-'*20)

#comparing pin
while count<3:
    print('-'*20)
    pin=str(input('\nENTER ATM PIN : '))
    print('-'*20)
    if pin.isdigit():
        if user=='user1':
            if pin==pins[0]:
                break
            else:
                count+=1
                print('-'*20)
                print('\nINVALID PIN')
                print('-'*20)
        if user=='user2':
            if pin==pins[1]:
                break
            else:
                count+=1
                print('-'*20)
                print('\nINVALID PIN')
                print('-'*20)
        if user=='user3':
            if pin==pins[2]:
                break
            else:
                count+=1
                print('-'*20)
                print('\nINVALID PIN')
                print('-'*20)
        if user=='user4':
            if pin==pins[3]:
                break
            else:
                count+=1
                print('-'*20)
                print('\nINVALID PIN')
                print('-'*20)
    else:
        print('-'*20)
        print('PIN CONSISTS OF 4 DIGITS')
        print('-'*20)
        count+=1
    
#for invalid pin
if count==3:
    print('-'*20)
    print('\n3 UNSUCCECCFULL PIN ATTEMPTS , EXITING..\n !!!! YOUR CARD IS BLOCKED !!!!')
    print('-'*20)
    exit()

#after logging in successfully
print('-'*20)
print('*'*20)
print('\nLOGIN SUCCESSFUL , CONTINUE ')
print('*'*20)
print('-'*20)
print('\n')
print('-'*20)
print('*'*20)
print('GOOD MORINING ',users[n].upper(),' WELCOME TO ATM')
print('*'*20)
print('-'*20)
print('------------ATM SYSTEM------------')

#banking
while True:
    print('-'*20)
    print('*'*20)
    #asking user action
    response=input('SELECT FROM FOLLOWING OPTIONS : \nStatement__(S)\nWithdraw___(W)\nDeposit____(D)\nChange Pin_(P)\nQuit_______(Q)\n::')
    response=response.lower()
    print('*'*20)
    print('-'*20)
    valid_responses=['s','w','d','p','q']
    #for statement
    if response=='s':
        print('-'*20)
        print(users[n].upper(),' YOU HAVE ',amounts[n],' RUPEES ON YOUR ACCOUNT.')
        print('-'*20)
    #for withdraw
    elif response=='w':
        print('-'*20)
        cash_with=int(input('ENTER AMOUNT YOU WOULD LIKE TO WITHDRAW : '))
        print('-'*20)
        if cash_with%100 != 0:
            print('-'*20)
            print('AMOUNT MUST BE MULTIPLY OF 100......!')
            print('-'*20)
        elif cash_with>amounts[n]:
           print('-'*20)
           print('YOU HAVE INSUFFICINET BALANCE')
           print('-'*20)
        else:
            amounts[n]=amounts[n]-cash_with
            print('-'*20)
            print('YOUR NEW BALANCE IS : ',amounts[n])
            print('-'*20)
    #for deposit
    elif response=='d':
        print('-'*20)
        cash_dep=int(input('ENTER AMOUNT YOU WANT TO DEPOSIT : '))
        print('-'*20)
        if cash_dep%100 != 0:
            print('-'*20)
            print('AMOUNT MUST BE MULTIPLY OF 100......!')
            print('-'*20)
        else:
            amounts[n]=amounts[n]+cash_dep
            print('-'*20)
            print('YOUR NEW BALANCE IS : ',amounts[n])
            print('-'*20)
    #to change pin
    elif response=='p':
        print('-'*20)
        new_pin=str(input('\nENTER NEW PIN : '))
        print('-'*20)
        if new_pin.isdigit() and new_pin!=pins[n] and len(new_pin)==4:
            print('-'*20)
            new_cpin=str(input('\nCONFIRM PIN : '))
            print('-'*20)
            if new_cpin!=new_pin:
                print('-'*20)
                print('\nPIN MISMATCH')
                print('-'*20)
            else:
                pins[n]=new_pin
                print('\nYOUR PIN IS CHANGED...')
                print('-'*20)
        else:
            print('-'*20)
            print('...NEW PIN CONSISTS OF 4 DIGITS AND MUST BE DIFFERENT TO PREVIOUS PIN...')
            print('-'*20)
    #to quit
    elif response=='q':
        exit()
    #other than valid response
    else:
        print('-'*20)
        print('\nGIVE A VALUABLE RESPONSE')
        print('-'*20)