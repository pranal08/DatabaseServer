# -*- coding: utf-8 -*-
"""
@author: Pranal
"""
import socket
from collections import OrderedDict

dictRecords={}
sortedDict={}
keyList=[]

def loadDict():
    fileobj=open("data.txt","r")
    testlist=fileobj.readlines()
    fileobj.seek(0)
    for x in range(len(testlist)):
        test=fileobj.readline().strip().split('|')
        if(test[0]=="" or test[0]==" " or test[0]==None):
            continue
        else:
           dictRecords[test[0]]=test[1:4] 
           if(dictRecords.get(test[0])[0]=="" or dictRecords.get(test[0])[0]==" " or dictRecords.get(test[0])[0]==None):
              dictRecords.get(test[0])[0]="---"
           if(dictRecords.get(test[0])[1]=="" or dictRecords.get(test[0])[1]==" " or dictRecords.get(test[0])[1]==None):
              dictRecords.get(test[0])[1]="---" 
           if(len(dictRecords.get(test[0]))==3):
               if(dictRecords.get(test[0])[2]=="" or dictRecords.get(test[0])[2]==" " or dictRecords.get(test[0])[2]==None):
                   dictRecords.get(test[0])[2]="---" 
              
    fileobj.close()



def addToDict(record):
#    file2=open("data.txt","a")
#    line=record[0]
    dictRecords[record[0]]=record[1:4]
#    for x in range(1,4):
#        line=line+"|"+record[x].strip()
#    #print(line)
#    file2.write(line)
#    file2.write("\n")
    
        
def performOps(x,c):
    if(x=="1"):
        name=c.recv(1024)
        cust=name.decode("utf-8")
        if(dictRecords.get(cust)==None):
            c.send(bytes("Customer not found","utf-8"))
        else:
            if(len(dictRecords.get(cust))<3):
                record="Name: "+cust+"\n"+"Age: "+dictRecords.get(cust)[0].strip()+"\n"+"Address: "+dictRecords.get(cust)[1].strip()+"\n"+"Phone: ---"
            else:
                record="Name: "+cust+"\n"+"Age: "+dictRecords.get(cust)[0].strip()+"\n"+"Address: "+dictRecords.get(cust)[1].strip()+"\n"+"Phone: "+dictRecords.get(cust)[2].strip()    
            c.send(bytes(record,"utf-8"))
    elif(x=="2"):
        record=[]
        for x in range(4):
            field=c.recv(1024)
            c.send(bytes("T","utf-8"))
            record.append(field.decode("utf-8"))
        if(dictRecords.get(record[0])==None):
            addToDict(record)
            print("")
            c.send(bytes("Record added successfully!!","utf-8"))
        else:
            c.send(bytes("Customer already exists!!","utf-8"))
    elif(x=="3"):
        name=c.recv(1024).decode("utf-8")
        check=dictRecords.pop(name,"None")
        if(check=="None"):
            c.send(bytes("Customer doesnot exist","utf-8"))
        else:
            c.send(bytes("Customer record deleted ","utf-8"))
    elif(x=="4" or x=="5" or x=="6"):
        name=c.recv(1024).decode("utf-8")
        if(dictRecords.get(name)==None):
            c.send(bytes("Customer not found","utf-8"))
        else:
            c.send(bytes("Customer exists","utf-8"))
            data=c.recv(1024).decode("utf-8")
            if(x=="4"):
                dictRecords.get(name)[0]=data
            elif(x=="5"):
                dictRecords.get(name)[1]=data
            else:
                dictRecords.get(name)[2]=data
            c.send(bytes("Customer Record has been Updated","utf-8"))
#        print(dictRecords)
    elif(x=="7"):
        length=str(len(dictRecords))
        c.send(length.encode())
        c.recv(32)
        sortedDict=OrderedDict(sorted(dictRecords.items()))
        sList=list(sortedDict.keys())
        for x in sList:
#            print("each item : "+x);
            c.send(x.encode())
            c.recv(32)
            print("")
            prac="|".join(dictRecords.get(x))
            c.send(prac.encode())
            c.recv(32)

def main2(c):    
    while c:
        option=c.recv(1024).decode("utf-8")
        if(option=="8"):
            break;
        else:
            performOps(option,c)
        
        
                
def main():
    dictRecords.clear()
    loadDict() 
    servsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servsocket.bind(('', 9999))
    servsocket.listen(5)
    print("listening")

    while True:
         c, addr = servsocket.accept()
         print("Connection from",addr)
         main2(c)



if __name__=="__main__":
    main()
