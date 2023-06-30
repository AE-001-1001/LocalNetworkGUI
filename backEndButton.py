from ctypes import windll, c_ulong
from tkinter import simpledialog,messagebox
import os 
import time
from sys import argv
from win32dll import SMALL_RECT, byref
class BackEndButtons:
        def __init__(self):
            super().__init__()
            
        def PROCESSOR_IDENTIFIER():
            """Prints a message when the button is clicked"""
            data_to_return = ["PROCESSOR_IDENTIFIER", "PROCESSOR_ARCHITECTURE", "PROCESSOR_LEVEL", "PROCESSOR_REVISION", "NUMBER_OF_PROCESSORS"]
            for i in data_to_return:
                print(i + ": " + os.environ[i])
            return 0
        # create a function that will use ip to get location of ip
        def ip_location():
            """Get the location of an ip address"""
            # automatically get ip address that are running in background
            ip = simpledialog.askstring("IP Address", "Enter IP Address")
            # return all the information about the ip address
            os.system("curl ipinfo.io/{}".format(ip))

        # create a function that will check the internet speed by pinging ookla
        def internet_speed():
            """Check the internet speed"""
            # check if the user has speedtest installed
            # if the user has speedtest installed
            if os.path.exists("speedtest.exe"):
                # run the speedtest
                os.system("speedtest.exe")
                if os.path.exists("speedtest.exe"):
                    # delete the zip file
                    os.system("del ookla-speedtest-1.2.0-win64.zip")
                    os.system("del speedtest.md")
            # if already installed don't ask the user if they want to install speedtest
            else:
                                # download the speedtest
                os.system("curl -O https://install.speedtest.net/app/cli/ookla-speedtest-1.2.0-win64.zip")
                # unzip the speedtest windows 64 bit
                os.system("tar -xvf ookla-speedtest-1.2.0-win64.zip")
                # run the speedtest
                os.system("speedtest.exe")
                # delete the zip file
                os.system("del ookla-speedtest-1.2.0-win64.zip")
            return 0
        
        def GetTurtle():
            """Get the turtle module"""
            # get the turtle module
            
            return 

        def sort_tasklist():
            """Sort the output of tasklist from smallest to largest"""
            return os.system("tasklist | sort /R")

        
        def AttachToPID():
            """Attach to a process id"""
            id = simpledialog.askstring("PID", "Enter PID")
            inject = messagebox.askyesno("Inject", "Do you want to inject?")

            # get data from the tasklist of given pid
            if inject == True:
                kernal32 = windll.kernel32
                print("Injecting...")
                # get the handle of the process
                hProcess = kernal32.OpenProcess(0x38, False, id)
                # check if the handle is valid
                if hProcess is not None:
                    # get the address of the loadlibraryA function
                    lpLoadLibraryA = kernal32.GetProcAddress(kernal32.GetModuleHandleA("kernel32.dll"), "LoadLibraryA")
                    # allocate memory for the dll name
                    lpBuffer = kernal32.VirtualAllocEx(hProcess, 0, len(argv[0]), 0x734, 0x40)
                    # write the dll name to the allocated memory
                    kernal32.WriteProcessMemory(hProcess, lpBuffer, argv[0], len(argv[0]), byref(c_ulong(0)))
                    # create a thread that will run the dll
                    kernal32.CreateRemoteThread(hProcess, None, 0, lpLoadLibraryA, lpBuffer, 0, byref(c_ulong(0)))
                    # create a remote thread that will write to the console
                    kernal32.CreateRemoteThread(hProcess, None, 0, 0x7FFD0000, 0x7FFD0000, 0, byref(c_ulong(0)))
                    # create a variable that will hold the handle of the process
                    hProcess = kernal32.OpenProcess(0x1F0FFF, True, id)
                    # use COORD to get the size of the console
                    # use SMALL_RECT to get the size of the console
                    rect = SMALL_RECT()
                    # use rect to get the size of the console
                    for i in os.popen("mode con").read().split(" "):
                        if i.isdigit():
                            rect.Right = int(i)
                            break
                    # use rect to get the size of the console
                    for i in os.popen("mode con").read().split(" "):
                        if i.isdigit():
                            rect.Bottom = int(i)
                            print(i)
                            break
                    
                    for i in os.popen("mode con").read().split(" "):
                        if i.isdigit():
                            rect.Left = int(i)
                            print(i)
                            break
                    
                    for i in os.popen("mode con").read().split(" "):
                        if i.isdigit():
                            rect.Top = int(i)
                            print(i)
                            break
                    

                    # use windll to get the size of the console
                    windll.kernel32.SetConsoleWindowInfo(hProcess, True, byref(rect))
                    
                    a = kernal32.CreateRemoteThread(hProcess, None, 0, 0x7FFD0000, 0x7FFD0000, 0, byref(c_ulong(0)))
                    if a:
                        kernel32 = kernal32
                        print(argv[0] + " " + str(a))
                        print("Injected")
                        kernel32.CloseHandle(hProcess)
                        # print out the data from handle
                        print("Handle: " + str(hProcess))
                        time.sleep(5)
                        print("Closed Handle after 5 seconds")
                        return True
                    else:
                        print("Error: " + str(kernal32.GetLastError()))
                        pass
                        try:
                            hProcess = kernal32.OpenProcess(0x1F0FFF, True, id)
                        except:
                            print("Failed to attach to handle %s" % id)
                            return False
                        # use hex to print the handle
                        #print(sys.stderr, hex(kernal32.GetLastError))
                    # close the handle
                    kernal32.CloseHandle(hProcess)
            else:
                print("Failed to inject")
                return False
            return 0