# If Statement
# Let us consider the movie "Avengers: Endgame". This is a 13+ movie.

print("Enter your year of birth")
dob = int(input())
current_year = 2023
age = current_year - dob
print('-----------------------------------------------------')

if(age < 13):
    print("\nYou are not allowed to watch this movie since you are underage")
    print('Please come back in',13-age,'years')
else:
    print("You are allowed to watch this movie\n")
    print('Dont forget to watch the sequels and prequels')
    print('Have a nice time at the movies')

print('Thankyou for using this program!!', 'Have a nice day!!')
print('------------------------------------------------')
