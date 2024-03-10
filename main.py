import time
import random

def animate_connection():
    # Animation for attempting connection
    print("Attempting connection to AWS:AMERICA:192.0.0.1:LOCALHOST")
    time.sleep(2)
    print("Attempting connections")

    # Simulate random flow of connections
    countries = ["CANADA", "EGYPT", "GERMANY", "INDIA", "JAPAN"]
    for _ in range(5):
        country = random.choice(countries)
        print(f"AWS:{country}:192.0.0.1:LOCALHOST")
        time.sleep(1)

    # Simulate connecting to Cairo
    print("Connected to AWS:CAIRO:192.0.0.1:LOCALHOST")
    time.sleep(5)
    print("PING - 82 ms")
    time.sleep(2)
    print("""
    Welcome to Protector!
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWNKXWWWWWWWWWWWWWWWWWWNKNWWWWWWWW
WWWWWWWN0oo0NWWWNXKOOKXWWWWNKdo0WWWWWWWW
WWWWWWWKxkOk0XNWWW0kOXWWWNXKkkkxKWWWWWWW
WWWWWWMXkdccOXXWWWWNNWWWWXKx;ckkXMWWWWWW
WWWWWWWNKl. .':xOkk0Oxoxo'.  .dXNWWWWWWW
WWWWWWWWNl      'lxkdd:.     .dNWWWWWWWW
WWWWWWWWN0xxdollO0o::d0xllodokXNWWWWWWWW
WWWWWWWWKKNWWWWWNo.  .kWWWNNNNK0NWWWWWWW
WWWWWWWWX0kodO0KK: . .oNX0xllkOKWWWWWWWW
WWWWWWWWWWXx,,d0KxodollOXx,,xNWWWWWWWWWW
WWWWWWWWWWM0, ;ONNWWWWNNK: ,0WWWWWWWWWWW
WWWWWWWWWWWWk;:xO0KXXK0Ox:'xWWWWWWWWWWWW
WWWWWWWMWWWWWkldxkOO0OxxdcdXWWWWWWWWWWWW
WWWWWWWWWWWWWN0xxxxkOkddx0NWWWWWWWWWWWWW
WWWWWWWWWWWWWWWNKOxkOkOKNWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWNXXXXNWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW

    """)

    # Asking for username and password
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username.lower() == "ally":
        print("WELCOME OWNER!!!")
        option = input("What do you want to do? (1. Protect email, 2. Destroy servers, 3. Secret option): ")
        if option == "1":
            email = input("Enter email: ")
            print("Processing...")
            time.sleep(5)
            print("Done.")
        elif option == "2":
            print("Destroying servers...")
            time.sleep(5)
            print("Servers destroyed.")
        elif option == "3":
            print("Accessing secret option...")
            time.sleep(5)
            print("Secret option executed.")
        else:
            print("Invalid option.")

if __name__ == "__main__":
    animate_connection()
