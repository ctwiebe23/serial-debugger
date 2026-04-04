from colorama import Fore, Back, Style

class Log:
    "Logger class for slightly-pretty printing"

    def error(message: str):
        print(Fore.RED + message + Style.RESET_ALL)

    def warn(message: str):
        print(Fore.YELLOW + message + Style.RESET_ALL)

    def debug(message: str):
        print(Fore.BLUE + message + Style.RESET_ALL)

    def info(message: str):
        print(message)

    def error_in(message: str):
        input(Fore.RED + message + Style.RESET_ALL)

    def warn_in(message: str):
        input(Fore.YELLOW + message + Style.RESET_ALL)

    def debug_in(message: str):
        input(Fore.BLUE + message + Style.RESET_ALL)

    def info_in(message: str):
        input(message)
