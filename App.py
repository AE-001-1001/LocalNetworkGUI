# Main App File
import os
from time import strftime
from AppBackEnd import App

def main():
    """App main function"""
    os.system('cls' if os.name == 'nt' else 'clear')
    current_time = strftime("%H:%M:%S")
    App.new_window(None,"Main Window {}".format(current_time))
    return None
        

if __name__ == '__main__':
    main()
    