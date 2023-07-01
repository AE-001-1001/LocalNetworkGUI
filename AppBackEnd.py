# imports
import os
from time import strftime
import tkinter as Tk
from tkinter import Button
from tkinter import Menu,simpledialog
from backEndButton import *
from AppReq import *
import win32dll
import random as r
import scapy.all as scapy
import uuid
import socket

class App:
    def __init__(self, name):
        self.name = name
        self.new_window(name)
        
    def new_window(self,name):
        """Create a new window"""
        root = Tk.Tk()
        root.geometry('455x345')
        os.system(f'title {name}')
        for i in range(1):
            root.update()
            root.title(name)
            break

        def update_total_memory():
            """Update the total physical memory"""
            # get the total free physical memory
            total_memory = os.popen("wmic OS get FreePhysicalMemory /Value").read()
            # print the total physical memory
            os.system('cls')
            print("Total Physical Memory: {}".format(total_memory))
            # update the total physical memory every 1000 milliseconds
            return root.after(1000, update_total_memory)
        
        # create a function that will count when New Window is activated

        def update_time_in_titletk():
            """Update the time in the title"""
            current_time = strftime("%H:%M:%S")
            root.title("Current Time: {}".format(current_time))
            # update the time in the title every 1000 milliseconds
            root.after(1000, update_time_in_titletk)
            # create a clock in the window
            return 0
        
        def update_total_virtual_memory():
            """Update the total virtual memory"""
            # get the total free virtual memory
            total_virtual_memory = os.popen("wmic OS get FreeVirtualMemory /Value").read()
            # print the total virtual memory
            os.system('cls')
            print("Total Virtual Memory: {}".format(total_virtual_memory))
            # update the total virtual memory every 1000 milliseconds
            root.after(1000, update_total_virtual_memory)
            return 0

        #create a function that will get ip of given website
        def get_ip():
            """gets the ip of a website"""
            website = simpledialog.askstring("Input", "Enter a website", parent=root)
            # get the ip of the website
            ip = os.popen("curl -4 {}".format(website)).read()
            print(ip)
            return 0


        def syn_ack():
            """Send a syn_ack packet"""
            # get the ip address
            ip = simpledialog.askstring("IP Address", "Enter IP Address")
            count = simpledialog.askinteger("Count", "Enter Count") 
            # send a syn_ack packet 
            while True:
                # build the packet
                source_port = scapy.RandShort()
                packet = scapy.IP(dst=ip)/scapy.TCP(sport=source_port, dport=80, flags="S")
                scapy.send(packet, verbose=0, count=count)
                print(f'Sent {count} packets to {ip} with Port: {source_port}')
                os.system("ipconfig /flushdns")
                if Exception:
                    break
                return print("Crtl + C to stop")

        def ScanOpenPorts():
            a = os.popen("netstat -ano").read()
            with open("OpenPorts.csv", "w") as f:
                f.writelines(a)
            return 0

        def get_mac():

            # configure socket to not open new connections
            socket.setdefaulttimeout(0.5)
            mac = []
            try:
                # use os to get the ip address
                hostname = socket.gethostname()
                IPAddr = socket.gethostbyname(hostname)
                mac = uuid.getnode()
                mac = ':'.join(("%012X" % mac)[i:i+2] for i in range(0, 12, 2))
                print("Hostname: {}".format(hostname))
                print("IP Address: {}".format(IPAddr))
                print("MAC Address: {}".format(mac))
            except:
                pass

            return 0

        def get_network_info():
            """Get the network info"""
            try:
                # get the network info
                network_info = os.popen("ipconfig").read()
                # print the network info
                print(network_info)
                # get all the mac addresses for the network adapters
                address = os.popen('arp -a').read()
                # print the mac addresses
                print(address)
            except Exception as e:
                print(f'Error: {e}')
                return 1
            return 0
        

        def exitting():
            print("Exiting...")
            time.sleep(3)
            exit()

        # the buttons on the window
        PROC = Button(root, text="PROCESSOR", command=BackEndButtons.PROCESSOR_IDENTIFIER)
        IPA = Button(root, text="IP Address", command=lambda: (os.system("curl ipinfo.io/ip")))
        IPL = Button(root, text="IP Location", command=BackEndButtons.ip_location)
        IS = Button(root, text="Internet Speed", command=BackEndButtons.internet_speed)
        SSA = Button(root, text="Send SYN_ACK", command=syn_ack)
        ARP = Button(root, text="All Running Processes", command=BackEndButtons.sort_tasklist)
        ATP = Button(root, text="Attach to PID", command=BackEndButtons.AttachToPID)
        CC = Button(root, text="Clear Console", command=lambda: os.system('cls'))
        EX = Button(root, text="Exit", command=exitting)
        
        # array of buttons 
        Scan = Button(root, text="Scan Open Ports", command=ScanOpenPorts)
        Get_IP = Button(root, text="Get IP", command=get_ip)
        Request = Button(root, text="Request Website", command=CustomRequester.get)
        Post = Button(root, text="Post Website", command=CustomRequester.Post)
        Get_MAC = Button(root, text="Get MAC Address", command=get_mac)
        Get_Network_Info = Button(root, text="Get Network Info", command=get_network_info)
        Kernal32 = Button(root,text="Kernal32", command=lambda: win32dll.Regular())



        buttons = [PROC, IPA, IPL, IS, SSA, ARP, ATP, CC, EX ]

        another_buttons = [Scan, Get_IP, Request,
                           Get_MAC, Get_Network_Info,
                           Post, Kernal32
                           ]


        for zyx in buttons:
            # if the text in the button is longer than 10 characters, make the button wider
            zyx.config(font=("Sans", 9), background="black", foreground="white", activebackground="black", activeforeground="white")
        for xyz in another_buttons:
            xyz.config(font=("Sans", 9), background="black", foreground="white", activebackground="black", activeforeground="white")
            
        for ZYX in range(len(another_buttons)):
            # move these buttons to the right side of the window and move them instead of lined up from the left, line them up from the right
            another_buttons[ZYX].place(x=0, y=30*ZYX, width=100)
            another_buttons[ZYX].bind("<Enter>", lambda event, ZYX=ZYX: another_buttons[ZYX].config(background="white", foreground="black"))
            another_buttons[ZYX].bind("<Leave>", lambda event, ZYX=ZYX: another_buttons[ZYX].config(background="black", foreground="white"))
            print("Initialized: {}".format(another_buttons[ZYX]).replace("!", "").replace(".", ""))
            root.update()

        for i in range(len(buttons)):
            # align the buttons to the left to match the size of the window
            buttons[i].place(x=344, y=30*i, width=100)
            buttons[i].bind("<Enter>", lambda event, i=i: buttons[i].config(background="white", foreground="black"))
            buttons[i].bind("<Leave>", lambda event, i=i: buttons[i].config(background="black", foreground="white"))
            print("Initialized: {}".format(buttons[i]).replace("!", "").replace(".", ""))
            root.update()



        #Menu bar at the top of window
        menu = Menu(root)
        root.config(menu=menu)
    
        cursors = ["arrow", "circle", "clock", 
                   "cross", "dotbox", "exchange",
                   "fleur", "heart","boat",
                   "iron_cross"," left_ptr"," left_side",
                   " left_tee"," leftbutton"," ll_angle",
                   " lr_angle","hand2","hand1", "pencil",
                   "pirate","plus","question_arrow"," right_ptr",
                   " right_side"," right_tee"," rightbutton",
                   " sb_down_arrow"," sb_h_double_arrow"," sb_left_arrow",
                   " sb_right_arrow"," sb_up_arrow"," sb_v_double_arrow",
                   "shuttle","sizing","spider","spraycan","star",
                   "target","tcross","top_left_arrow","top_left_corner",
                   "top_right_corner","top_side","top_tee","trek",
                   "ul_angle","umbrella","ur_angle","watch","xterm",
                   "X_cursor"]
        
        menu.add_checkbutton(label='Time', command=update_time_in_titletk)
        menu.add_checkbutton(label='Date', command=lambda: print(strftime("%d/%m/%Y/%H:%M:%S/%a")))
        menu.add_checkbutton(label="GPU Information", command=lambda: os.system("nvidia-smi "))
        menu.add_checkbutton(label='CPU Usage', command=lambda: os.system("wmic cpu get loadpercentage /value"))
        menu.add_checkbutton(label='Memory Usage', command=update_total_memory)
        menu.add_checkbutton(label='Virtual Memory Usage', command=update_total_virtual_memory)
        menu.add_checkbutton(label='Deploy IP Addresses Reader', command=lambda: os.system("netstat | findstr /R /C:\"[0-9]*\\.[0-9]*\\.[0-9]*\\.[0-9]*\""))
        menu.add_checkbutton(label='Change Cursor', command=lambda: root.config(cursor=r.choice(cursors)))
        menu.configure(background="black", foreground="black", activebackground="black", activeforeground="black")

        root.config(menu=menu, background="black", bd=5, relief="sunken", border=3, highlightbackground="darkblue", highlightcolor="blue", highlightthickness=3, cursor=cursors[19])        
        root.mainloop()
