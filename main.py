from colorama import Fore, Style

def email_protector():
    # Print ASCII art
    print(Fore.GREEN + """
    ██████╗░██╗░░░░░██╗███████╗░█████╗░
    ██╔══██╗██║░░░░░██║██╔════╝██╔══██╗
    ██████╦╝██║░░░░░██║█████╗░░██║░░██║
    ██╔══██╗██║░░░░░██║██╔══╝░░██║░░██║
    ██████╦╝███████╗██║███████╗╚█████╔╝
    ╚═════╝░╚══════╝╚═╝╚══════╝░╚════╝░
    """)
    print(Style.RESET_ALL)
    print("Email Protector made by Ally")

    # Prompt for email address
    email = input("Enter your email address: ")

    # Print the email address with a message
    print("\nDone! Your email address is:", Fore.YELLOW + email)
    print(Style.RESET_ALL)

if __name__ == "__main__":
    email_protector()
