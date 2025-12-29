## project 2 Login system 
# this will allow an user to login within 3 attempts
# If the user details are not correct It will tell to correct the details 

username = "admin"
password = "1234"
success = False

# loop for 3 attempts 
for attempt in range(3):
    enter_username = input("Enter username: ")
    enter_password = input("Enter password: ")

   # Checking weather the details are matched or not
    if enter_username == username and enter_password == password:
        print("Login successful")
        success = True
        break
    else:
        print("Invalid credentials")
#if user can't login within 3 attempts system will get locked automatically 
if not success:
    print("Account locked after 3 failed attempts")
  
