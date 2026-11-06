# pin_space_table.py how long the hacker take to guess loop on the range from 4 to 8 
GUESSES_PER_SECOND=10
for digits in range (4,9):
    combinations=10**digits
    seconds=combinations//GUESSES_PER_SECOND
    minutes=seconds//60
    days=seconds//86400
    print(f"{digits} digits:{combinations} PINs,{minutes} minute, {days} days")

