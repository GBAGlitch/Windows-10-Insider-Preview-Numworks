#Compiled version of developpement Windows
#Windows 10 ver 6935 build 200112.1
#for numworks calculator
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
  print("DOOM id-software 1993 for DOS")
def snake(v = 1):
  score = 0
  dx,dy = 0,1
  vert,rouge = (0,252,0),(248,0,0)
  s = [[160,110]]
  food = True
  pt = monotonic()
  while True:
    ct = monotonic()
    dt = ct-pt
    if food:
      fx = 10 * randint(0,31)
      fy = 10 * randint(0,21)
      food = False
    fill_rect(fx,fy,10,10,rouge)
    k = get_keys()
    if "up" in k: dx,dy = 0,-1
    if "down" in k : dx,dy = 0,1
    if "left" in k: dx,dy = -1,0
    if "right" in k: dx,dy = 1,0
    if dt>.2-.02*v:
      pt = monotonic()
      x = s[0][0] + 10*dx
      y = s[0][1] + 10*dy
      if x<0 or x>310 or y<0 or y>210 or get_pixel(x,y)==vert:
        draw_string("oups !!",5,10)
        fill_rect(x,y,10,10,rouge)
        return score
      s.insert(0,[x,y])
      if get_pixel(x,y)!=rouge:
        q = s.pop()
        fill_rect(q[0],q[1],10,10,(248,255,248))
      else:
        score += 1
        draw_string(str(score),5,10)
        food=True
      fill_rect(s[0][0],s[0][1],10,10,vert)
v=[0]*16
chiffres = [31599,18724,29671,31207,18925,31183,31695,18727,31727,31215]
sco = 0
def aff(n,x,y):
  if n>0:
    for k,c in enumerate(str(n)):
      for i in range(16):
        if chiffres[int(c)]>>i & 1 == 1:
          fill_rect(x+12*k+(i%3)*3,y+(i//3)*3,3,3,(110,110,90))
def ajout():
  vides = [i for i,x in enumerate(v) if x==0]
  if len(vides) != 0:
    v[choice(vides)] = choice([2,2,2,4])
  plateau()
  
def gauche(r):
  return ([x for x in r if x!=0]+[0]*4)[:4]
def simp(r):
  global sco
  r = gauche(r)
  for i in range(1,4):
    if r[i] == r[i-1]:
      r[i-1] *= 2
      r[i] = 0
      sco += r[i-1]
  return gauche(r)    
def calcul(ligne,pas):
  for i in range(4):
    pos = simp([v[ligne[k]+pas*i] for k in range(4)])
    for k in range(4):
      v[ligne[k]+pas*i] = pos[k]
  ajout()
def plateau():
  global sco
  fill_rect(3,6,208,208,(190,170,160))
  for i in range(16):
    g = max(0,int(-v[i]/2+255))
    fill_rect(5+50*(i%4),8+50*(i//4),47,47,(g,g,g))
    aff(v[i],7+50*(i%4)+24-6*len(str(v[i])),25+50*(i//4))
  draw_string(("0000"+str(sco))[-5:],250,10)
def 2048():
  ajout()
  while True:
    tou={}
    while len(tou)==0:
       tou=get_keys()
    if "left" in tou: calcul([0,1,2,3],4)
    elif "right" in tou: calcul([3,2,1,0],4)
    elif "up" in tou: calcul([0,4,8,12],1)
    elif "down" in tou: calcul([12,8,4,0],1)
    sleep(.3)
bootui(1)
#
#
#
#
#
#
#
#
#
#these line are here for nothing, only for have 300 lines
