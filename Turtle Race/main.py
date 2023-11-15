def get_number_of_racers():
    racers = 0
    while True:
        racers = input("Please enter number of racers (2-10): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Please enter valid number between (2-10)")
            continue