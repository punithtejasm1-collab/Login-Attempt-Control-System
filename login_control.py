MAX_ATTEMPTS = 3

username = "admin"
password = "1234"

attempts = 0

while attempts < MAX_ATTEMPTS:
    user = input("Enter Username: ")
    pwd = input("Enter Password: ")

    if user == username and pwd == password:
        print("Login Successful!")
        break
    else:
        attempts += 1
        print("Incorrect Username or Password")
        print("Attempts Left:", MAX_ATTEMPTS - attempts)

if attempts == MAX_ATTEMPTS:
    print("Access Temporarily Restricted")
    print("Too many failed login attempts")
