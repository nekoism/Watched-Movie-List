from libs import welcome_message
from time import sleep
from libs import exit_program
import getpass

def login() :
    print('\nPassword is transparent, keep going')
    user_id = input('User ID  : ')
    password = getpass.getpass('Password : ')
    
    if user_id == 'neko' and password == 'neko123' : 
        print('\nLogin Successfull!!!')
    else :
        print('User ID or Password wrong!!!\n')
        login()



def start ():
    try:    
        watched_movie_list = []
        infile = open('WatchedMovieList.txt', 'r')
        line = infile.readline()
        while line :
            watched_movie_list.append (line.rstrip("\n").split(","))
            line = infile.readline()
        infile.close()
    
    except FileNotFoundError:
        print('File <Watched Movie List.txt> not found')
        print('Starting a new Watched Movie List')
        watched_movie_list = []
        
    
    
    welcome_message ('Watched Movie List')
    
    login()
    
    while True :
        menu = int(input('\nMain Menu : \n1.Watched Movie List\n2.Looking for a movie u has watch\n3.Adding a Movie\n4.Exit\n\nEnter the number menu : '))
        
        if menu == 1 :
            print('\nDisplaying all watched movie')
            sleep(1)
            for i in range (len(watched_movie_list)) :
                print (watched_movie_list[i])
        elif menu == 2 :
            print('Looking for a movie...')
            sleep(1)
            keyword = input('Enter a movie name : ')
            for movie in watched_movie_list :
                if keyword in movie :
                    print()
                    print(movie)
            else :
                print('\n"U hasnt watch that movie or u enter wrong name"')
                continue                  
        elif menu == 3 :
            print('\nAdding a movie...')
            sleep(1)
            nmenu    = input('\nAdd a movie name with CAPITAL: ')
            nrating  = input('Add a rating                 : ')
            ncomment = input('Add a comment                : ')
            ndate    = input('Date u watch DD/MM/YY        : ')
            watched_movie_list.append([nmenu, nrating, ncomment, ndate])             
        elif menu == 4 :
            exit_program()
        else :
            print('Please chosee number betwen 1-4!!!')
            continue
    
        outfile = open('WatchedMovieList.txt', 'w')
        for movie in watched_movie_list :
            outfile.write(','.join(movie) + '\n')
        outfile.close()
    

if __name__ == '__main__':
    start()
    
