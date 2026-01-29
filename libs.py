def welcome_message (title) :
    frame = '*' * (len(title)+ 6)
    print (frame)
    print (f'*  {title}  *')
    print (frame)
    

def exit_program() :
    from time import sleep
    print('Program akan dihentikan ')
    sleep(1)
    print('3....')
    sleep(1)
    print('2....')
    sleep(1)
    print('1....')
    exit()
    