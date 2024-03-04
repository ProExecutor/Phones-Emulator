import os, time, threading
from cryptography.fernet import Fernet

print("Welcome to Len4's first ever Celen App Emulator!\n")
print("A celen app is a .cap format that is used in many chinese smart phones such as huawei or onePlus. The compiled .cap files are pretty easy to emulate with python considering they are made with it!\n\nThis app will decompile and emulate main.cap after you press enter!")

def split(delimiters, string, maxsplit=0):
    import re
    regexPattern = '|'.join(map(re.escape, delimiters))
    return re.split(regexPattern, string, maxsplit)

f = open("main.cap","r")
f = f.read();
#This will split the data into chunks for parsing
f = f.split('�')
app_name = f[1].replace('}',"")
from replit import clear
clear()
current = 0;

#basic parsing definitions
def parse_markup(mk):
 mk = mk.replace("^K ","")
 key = "YxvN8K30fZaeKNU9eSwLc2QgbkZrCPy4bf2HsUiUBKE=".encode()
 f = Fernet(key)
 mk = f.decrypt(mk.encode())

 return mk;
def parse_script(mk):
  mk = mk.replace("main.py&","")
  key = "YxvN8K30fZaeKNU9eSwLc2QgbkZrCPy4bf2HsUiUBKE=".encode()
  f = Fernet(key)
  mk = f.decrypt(mk.encode())
  return mk;

#the actual parsing
while(current != len(f)):
  chunk = f[current]
  if(chunk.startswith("^K")):
    
    a = open("compiled/root/index.html", "w")
    
    a.write(str(parse_markup(chunk).decode()))
    a = open("compiled/root/index.html","r")
  if(chunk.startswith("main.py&")):
    
    a = open("compiled/main.py",'w');
    a.write(str(parse_script(chunk).decode()))
    a = open("compiled/main.py",'r')
   
  current += 1;

a = open("compiled/root/assets.zip",'w')
a.write(f[-1])
a = open("compiled/root/assets.zip","r")
a.close()

#emulation (easy after parsing)
exec(open('compiled/main.py').read())

os.system("firefox --kiosk file:compiled/root/index.html")
