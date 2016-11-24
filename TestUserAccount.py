#This script performs some simple tests on the UserAccount class.
import UserAccount

my_username="sivanbm"
my_password="helloworld"
my_secret="I hate the dentist"

#Two things are missing from the line below - fill them in
my_user=UserAccount.UserAccount( my_username , my_password , my_secret  )


#Call the print_password method (function) - it takes one input - a guess for the password.
my_user.print_password("1234")

#Use the wrong password as input here
my_user.print_password("wrong_one")

#Use the right password here
my_user.print_password("helloworld")
