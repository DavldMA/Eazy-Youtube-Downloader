from colorama import Fore, Style
import os
import downloader

def loadMenu():
    while True:
        print(f"{Fore.MAGENTA}[+] Choose an option:{Style.RESET_ALL}")
        print(f"{Fore.BLUE}[+] 1. Download as Audio{Style.RESET_ALL}")
        print(f"{Fore.BLUE}[+] 2. Download as Video{Style.RESET_ALL}")
        print(f"{Fore.BLUE}[+] 3. Download Both{Style.RESET_ALL}")
        print(f"{Fore.RED}[+] 0. Close Program{Style.RESET_ALL}\n")

        choice = input(f"{Fore.YELLOW}[+] Enter the number of your choice (0-3): {Style.RESET_ALL}")

        if choice == '1':
            url = downloader.getLink()
            downloader.download(url, True)
        elif choice == '2':
            url = downloader.getLink()
            downloader.download(url, False)
        elif choice == '3':
            url = downloader.getLink()
            downloader.download(url, True)
            downloader.download(url, False)
        elif choice == '0':
            print(f"{Fore.RED}[-] Closing program.{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}[-] Invalid choice. Please enter a number between 0 and 3. Press enter to continue.{Style.RESET_ALL}")
            input()
        os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    loadMenu()