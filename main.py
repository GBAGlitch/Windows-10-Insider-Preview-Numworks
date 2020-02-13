#Compiled version of developpement Windows
#Windows 10 ver 6935 build 200112.1
#for numworks calculator, I recomand it for the N0110, 
#I recomand you to install this fork of the official Numworks firmware or this program doesn't work
#link of the fork : https://omega-numworks.github.io/
#inclued doom type doom()
#inclued word type word()
#inclued Windows update type update()
#inclued task manager type taskman()
#inclued reboot type bootui(1)

start = 0
from time import *
from math import *
from kandinsky import *
from random import *
from turtle import *
b = color(255,255,255)
ta = ("")
tb = ("")
tc = ("")
td = ("")
te = ("")
tf = ("")
tg = ("")
th = ("")
ti = ("")
tj = ("")
#Microsoft Windows 10
def bootui(a) :
  if a == 1 :
    fill_rect(0,0,640,480,(0,0,0))
    fill_rect(120,50,40,40,(128,128,255))
    fill_rect(120,93,40,40,(128,128,255))
    fill_rect(163,40,50,50,(128,128,255))
    fill_rect(163,93,50,50,(128,128,255))  
    for i in range(10):  
      set_pixel(160,180,(255,255,255))
      set_pixel(161,180,(255,255,255))
      set_pixel(160,181,(255,255,255))
      set_pixel(161,181,(255,255,255))
      sleep(0.1)
      set_pixel(166,186,(255,255,255))
      set_pixel(167,186,(255,255,255))
      set_pixel(166,187,(255,255,255))
      set_pixel(167,187,(255,255,255))
      sleep(0.1)
      set_pixel(161,191,(255,255,255))
      set_pixel(160,191,(255,255,255))
      set_pixel(161,192,(255,255,255))
      set_pixel(160,192,(255,255,255))  
      sleep(0.1)
      set_pixel(157,187,(255,255,255))
      set_pixel(156,186,(255,255,255))
      set_pixel(156,187,(255,255,255))
      set_pixel(157,186,(255,255,255))
      sleep(0.1)
      fill_rect(150,165,40,40,(0,0,0))
      sleep(0.5)
    print("welcome to windows 10 cmd mode \nNo graphical mode")  
  else : 
    print("sorry an error occured, \nor you are already in windows")



task = ["MsMpEng.exe","winlogon.exe","registry","explorer.exe","minecraft.exe","iexplore.exe","MicrosoftEdge.exe","MEMZ.BAT","WIN.COM","Avira.exe","winword.exe","taskman.exe","notepad.exe","battlenet.exe","discord.exe","cmd.exe","000.exe","MEMZ-DESTRUCTIVE.BAT","starcraft.exe","javaw.exe","system","regedit","command.com","edit.com","scandisk.com"]
def taskman() :
  ta = choice(task)
  tb = choice(task)
  tc = choice(task)
  td = choice(task)
  te = choice(task)
  tf = choice(task)
  tg = choice(task)
  th = choice(task)
  ti = choice(task)
  tj = choice(task)
  print("Task Manager - detail")
  print(ta)
  print(tb)
  print(tc)
  print(td)
  print(te)
  print(tf)
  print(tg)
  print(th)
  print(ti)
  print(tj)
def winver() :
  print("About Windows")
  print("Microsoft Windows 10 \nInsider Preview \nbuild 19035 ")
def update() :
  fill_rect(0,0,640,480,(128,128,255))
  draw_string("Working on Windows update",60,100,(0,0,0),(128,128,255))
  draw_string("percent completed",100,140,(0,0,0),(128,128,255))
  ul = float()
  up = float()
  while ul <= 100:
    ulc = str(ul)
    draw_string(ulc,90,125,(0,0,0),(128,128,255))
    fill_rect(130,125,200,15,(128,128,255))
    up = random()
    ul = ul + up
    sleep(0.5)
x = 2
use = 0
a1 = ("")
a2 = ("")
a3 = ("")
a4 = ("")
a5 = ("")
a6 = ("")
a7 = ("")
a8 = ("")
def Word() :
  print("Microsoft Office Word") 
  a1 = ("")
  a2 = ("")
  a3 = ("")
  a4 = ("")
  a5 = ("")
  a6 = ("")
  a7 = ("")
  for i in range(200):
    x = 2
    print("------------------------------")
    print(" |FILE---EDIT---INSERT---SAV|")
    print("------------------------------")
    print("|0|" + a1 + "")
    print("| |" + a2 + "")
    print("| |" + a3 + "")
    print("|1|" + a4 + "")
    print("| |" + a5 + "")
    print("| |" + a6 + "")
    print("|2|" + a7 + "")
    print("------------------------------")
    a1 = input("l1 : ")
    a2 = input("l2 : ")
    a3 = input("l3 : ")
    a4 = input("l4 : ")
    a5 = input("l5 : ")
    a6 = input("l6 : ")
    a7 = input("l7 : ")
def doom():
  r = randint(663,666)
  ammo = 666
  life = 300
  statlist = ["nothing","poisoned","paralized","burned","freezed"]
  killcount = 0
  difficulty = int(input("write difficult : \n1(easy),2(medium),3(hard) : "))
  if difficulty == 1:
    ennemycount = 200
  elif difficulty == 2 :
    ennemycount = 500
  elif difficulty == 4 :
    ennemycount = 1000
    print("secret hardcore activated")
    life = 150
    time.sleep(3)
  elif difficulty == 666:
    ennemycount = 10000
    life = 100
    print("Welcome to the \nIMPOSSIBLE MODE :)") 
    time.sleep(3)
  else:
    ennemycount = 1000
  while ennemycount >= 0 and life >= 1:
    damagetook = randint(0,25)
    crit = randint(1,2)
    if crit == 2:
      damagetook = damagetook * 2
      print("you took several damage")
    infliged = randint(0,50)
    crith = randint(1,2)
    if crith == 2:
      infliged = infliged * 2
      print("you made critical hit")
    print("you took damage")
    print(damagetook)
    print("you killed ennemy")
    print(infliged)
    pot = [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,2,2,3,3,3,3,3,3,3,3,3,10,10,10,10,10,10,10,5,5,5,5,5,5,100,50,1000]
    heal = choice(pot)
    life = life + heal
    print("you have been healed HP")
    print(heal)
  
    life = life - damagetook
    ammo = ammo - infliged
    ennemycount = ennemycount - infliged
    print("you have HP")
    print(life)
    print("ammo : ")
    print("!!!INFINITE!!!")
    print("there is ennemies")
    print(ennemycount)
    t = randint(1,1000000)
    if ennemycount == 666:
      ennemycount == ennemycount + t
      print("666 ennemies left... I added more mobs")  
    
    
    u = input("press 1 : ")
    if u == 666:
        print("Game Over Bro")
        ennemycount = 1000000
        input("press 1")
    if life <= 0:
      print("you loose")
  
      
    if life >= 1  and ennemycount <= 0:
      print("you won")
def doomhlp():
  print("DOOM is a VideoGame of \nFirst Player Shooter game type \nthere is few difficulty\nmode : easy\nmedium\nhard\nand the secret hardcore mode \nand the doom mode :)")
def about():
  print("DOOM id-software 2020 for win32")  
def brainfuck(q,entree=""):
 P=print
 sep="\n\t "
 e=[]
 for l in entree:
  e+=list(l)
 p=0
 dp=0
 c=0
 m=[0]

 while p<len(q):
  c+=1
  if c>=10**6:
   P("Limite max. Votre code semble tourner en rond.")
   break
  elif q[p]==">":
   dp+=1
   if dp==len(m):
    m.append(0)
   p+=1
  elif q[p]=="<":
   dp-=1
   if dp==-1:
    m=[0]+m
    dp=0
   p+=1
  elif q[p]=="+":
   m[dp]+=1
   p+=1
  elif q[p]=="-":
   m[dp]-=1
   p+=1
  elif q[p]==".":
   P(chr(m[dp]),end="")
   p+=1
  elif q[p]==",":
   m[dp]=ord(e.pop(0))
   p+=1
  elif q[p]==":":
   print(m[dp],end=" ")
   p+=1
  elif q[p]==";":
   while e[0] in sep:
    e.pop(0)
   while e and e[0] not in sep:
    m[dp]*=10
    m[dp]+=int(e.pop(0))
   p+=1
  elif q[p]=="[":
   if m[dp]!=0:
    p+=1
    continue
   nbo=1
   while nbo!=0:
    p+=1
    if q[p]=="[":
     nbo+=1
    if q[p]=="]":
     nbo-=1
   p+=1
  elif q[p]=="]":
   if m[dp]==0:
    p+=1
    continue
   nbf=1
   while nbf!=0:
    p-=1
    if q[p]=="]":
     nbf+=1
    if q[p]=="[":
     nbf-=1
  elif q[p]=="!":
   for i in range(len(m)):
    if i==dp:
     P("["+str(m[i])+"]",end=" ")
    else:
     P(m[i],end=" ")
   P()
   p+=1

 P()
bootui(1)
