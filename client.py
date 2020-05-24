# -*- coding: utf-8 -*-
"""
@author: Pranal
"""
import socket


def findCust(s):
    name=input("Enter customer name: ") or "---"
    while(name=="---"):
        print("")
        print("You didnot enter anything!!")
        name=input("Enter customer name: ") or "---"
    s.send(bytes(name.title(),"utf-8"))
    msg=s.recv(1024)
    print(msg.decode("utf-8"))
    
def addCust(s):
    name=input("Enter customer name: ") or "---"
    while(name=="---"):
        print("")
        print("Oops check the name format again!!")
        name=input("Enter customer name: ") or "---"
    age=input("Enter customer age: ") or "---"
    while(age!="---"):
        try:
            int(age)   
            break
        except ValueError as ve:
            print("You didnot enter anything or else Number Format not entered!!")
            age=input("Enter customer age: ") or "---"
    add=input("Enter customer address: ") or "---"
    phone=input("Enter customer phone: ") or "---"
    listset=[name.title(),age,add,phone]
    for x in listset:
        s.sendall(x.encode())
        s.recv(3226)
    msg=s.recv(1024)
    print(msg.decode("utf-8"))
    
def delCust(s):
    name=input("Enter customer name to delete: ") or "---"
    while(name=="---"):
        print("")
        print("You didnot enter anything!!")
        name=input("Enter customer name: ") or "---"
    s.send(bytes(name.title(),"utf-8"))
    msg=s.recv(1024)
    print(msg.decode("utf-8"))

def update(x,s):
    name=input("Enter customer name: ") or "---"
    while(name=="---"):
        print("")
        print("You didnot enter anything!!")
        name=input("Enter customer name: ") or "---"
    s.send(bytes(name.title(),"utf-8"))
    msg=s.recv(1024).decode("utf-8")
    if(msg=="Customer exists"):
        if(x=="4"):
            age=input("Enter customer age: ") or "---"
            while(age!="---"):
                try:
                    int(age)
                    break
                except ValueError:
                    print("You didnot enter anything or else Number Format not entered!!")
                    age=input("Enter customer age: ") or "---"
            s.send(bytes(age,"utf-8"))
            
        elif(x=="5"):
            addr=input("Enter customer address: ") or "---"
            s.send(bytes(addr,"utf-8"))
        
        else:
            phone=input("Enter customer phone: ") or "---"
            s.send(bytes(phone,"utf-8"))
        msg=s.recv(1024).decode("utf-8")
        print(msg)
    else:
        print(msg)
        
def printReport(s):
    
    length=s.recv(4096).decode()
    s.send(bytes("T","utf-8"))
    print(" ")
    print('{:^10} {:^10} {:^25} {:^10}'.format('NAME','AGE','ADDRESS','PHONE'))
    for x in range(int(length)):
         print("---------------------------------------------------------------------------------------------------------")
         msg=s.recv(4096).decode()
#         print(msg)
         s.send(bytes("T","utf-8"))
#         print("------------------------")
         val=list(s.recv(4096).decode().split("|"))
         if(len(val)<3):
             print('{:^10} {:^10} {:^25} {:^10}'.format(msg,val[0],val[1],'---'))
         else:
             print('{:^10} {:^10} {:^25} {:^10}'.format(msg,val[0],val[1],val[2]))
         s.send(bytes("T","utf-8"))

def renderOptions(x,s):
    if(x=="1"):
        findCust(s)
    elif(x=="2"):
        addCust(s)
    elif(x=="3"):
        delCust(s)
    elif(x=="4"):
         update(x,s)
    elif(x=="5"):
        update(x,s)
    elif(x=="6"):
        update(x,s)
    else:
        printReport(s)
       
    

def main():
    s = socket.socket()
    s.connect(('127.0.0.1', 9999))
    while True:
        print("------------------------------------------------")
        print("\nPython DB Menu")
        print("\n")
        print("1. Find Customer")
        print("2. Add Customer")
        print("3. Delete Customer")
        print("4. Update Customer Age")
        print("5. Update Customer Address")
        print("6. Update Customer Phone")
        print("7. Print Report")
        print("8. Exit")
        print("------------------------------------------------")
        x=input("Select: ")
        print("------------------------------------------------")
        if(x=="1" or x=="2" or x=="3" or x=="4" or x=="5"
            or x=="6" or x=="7"):
            s.send(bytes(x,"utf-8"))
            renderOptions(x,s)
        elif(x=="8"):
            s.send(bytes(x,"utf-8"))
            print("           GOODBYE            ")
            s.close()
            break
        else:
            print("Oops!!Check your input again!!!")    
        
        


if __name__=="__main__":
    main()
