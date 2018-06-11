films = {
    "Finding Dory": [3,5],
    "Bourne": [18,5],
    "Tarzan": [15,5],
    "Ghost Busters": [12,5]
    }

while True:
    choice = input("What movie do you want to watch?: ").strip().title()

    if choice in films:
        age = int(input("How old are you?").strip())

        if age >= films[choice][0]:
            if films[choice][1] > 0:
                print("Enjoy the movie!")
                films[choice][1] = films[choice][1] - 1
            else:
                print("Sorry we are out of tickets")
                
        else:
            print("You are too young to see this movie")

        
    else:
        print("We do not have that film....")
    
