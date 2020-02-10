#coding: utf-8
import random,sys,time,os
m='\033[31;1m'
k='\033[93m'
h='\x1b[92m'
b='\033[94m'
p='\033[95m'
c='\033[1;36m'
z='\033[0m'
time.sleep(0.5)
def logo():
   ogol=0
   while True:
        os.system('clear')
        print(m+'Menu Logo Cowsay :'+z)
        print(m+'['+p+'a'+m+']'+h+' GhostBusters'+z)
        print(m+'['+p+'b'+m+']'+h+' Stegosaurus'+z)
        print(m+'['+p+'c'+m+']'+h+' Beavis.zen'+z)
        print(m+'['+p+'d'+m+']'+h+' Daemon'+z)
        print(m+'['+p+'e'+m+']'+h+' Dragon'+z)
        print(m+'['+p+'f'+m+']'+h+' Elephant'+z)
        print(m+'['+p+'g'+m+']'+h+' Hello Kitty'+z)
        print(m+'['+p+'h'+m+']'+h+' Eyes'+z)
        print(m+'['+p+'i'+m+']'+h+' Skeleton'+z)
        print(m+'['+p+'j'+m+']'+h+' Ren'+z)
        print(m+'['+p+'k'+m+']'+h+' Tux'+z)
        print(m+'['+p+'R'+m+']'+k+' Back'+z)
        print(m+'['+p+'X'+m+']'+m+' Exit'+z)
        num=input(p+'PILIH NOMOR '+m+'>'+k+'>'+h+'> '+c)
        if num=='' :
          print(m+'Tidak Boleh Kosong !'+z)
          time.sleep(1)
          ogol+=1
        elif num=='a' :
            gb=input(p+'Nickname Kamu '+m+'>'+k+'>'+h+'> '+c)
            os.system('clear')
            os.system('cowsay -f ghostbusters '+str(gb))
            time.sleep(3)
            ogol+=2
        elif num=='b' :
            so=input(p+'Nickname Kamu '+m+'>'+k+'>'+h+'> '+c)
            os.system('clear')
            os.system('cowsay -f stegosaurus '+str(so))
            time.sleep(3)
            ogol+=3
        elif num=='c' :
            bz=input(p+'Nickname Kamu '+m+'>'+k+'>'+h+'> '+c)
            os.system('clear')
            os.system('cowsay -f beavis.zen '+str(bz))
            time.sleep(3)
            ogol+=4
        elif num=='d' :
            dn=input(p+'Nickname Kamu '+m+'>'+k+'>'+h+'> '+c)
            os.system('clear')
            os.system('cowsay -f daemon '+str(dn))
            time.sleep(3)
            ogol+=5
        elif num=='e' :
            dg=input(p+'Nickname Kamu '+m+'>'+k+'>'+h+'> '+c)
            os.system('clear')
            os.system('cowsay -f dragon '+str(dg))
            time.sleep(3)
            ogol+=6
        elif num=='f' :
            ep=input(p+'Nickname Kamu '+m+'>'+k+'>'+h+'> '+c)
            os.system('clear')
            os.system('cowsay -f elephant '+str(ep))
            time.sleep(3)
            ogol+=7
        elif num=='g' :
            hk=input(p+'Nickname Kamu '+m+'>'+k+'>'+h+'> '+c)
            os.system('clear')
            os.system('cowsay -f hellokitty '+str(hk))
            time.sleep(3)
            ogol+=8
        elif num=='h' :
            eye=input(p+'Nickname Kamu '+m+'>'+k+'>'+h+'> '+c)
            os.system('clear')
            os.system('cowsay -f eyes '+str(eye))
            time.sleep(3)
            ogol+=9
        elif num=='i' :
            st=input(p+'Nickname Kamu '+m+'>'+k+'>'+h+'> '+c)
            os.system('clear')
            os.system('cowsay -f skeleton '+str(st))
            time.sleep(3)
            ogol+=10
        elif num=='j' :
            ren=input(p+'Nickname Kamu '+m+'>'+k+'>'+h+'> '+c)
            os.system('clear')
            os.system('cowsay -f ren '+str(ren))
            time.sleep(3)
            ogol+=11
        elif num=='k' :
            tux=input(p+'Nickname Kamu '+m+'>'+k+'>'+h+'> '+c)
            os.system('clear')
            os.system('cowsay -f tux '+str(tux))
            time.sleep(3)
            ogol+=12
        elif num=='R' :
            intro()
        elif num=='X' :
            print(m+'Keluar ...'+z)
            time.sleep(1)
            sys.exit()
        else:
             print(m+'Wrong Input'+z)
             time.sleep(1)
def teks():
        fol=0
        while True:
             os.system('clear')
             def mengetik(s):
                for c in s + '\n':
                    sys.stdout.write(c)
                    sys.stdout.flush()
                    time.sleep(random.random() * 0.1)
             print(m+'('+p+'X'+m+')'+h+' Animasi Teks Berjalan '+m+'('+p+'X'+m+')'+z)
             print(p+' Masukkan Text Anda Dibawah '+z)
             tul=input(c+' > ')
             kom=input(p+' Lihat Hasilnya ? [y/t]'+c+' > ')
             if kom=='' :
               print(m+' Tidak Boleh Kosong !'+z)
               time.sleep(1)
               fol+=1
             elif kom=='y' :
                 os.system('clear')
                 print('')
                 mengetik(str(tul))
                 time.sleep(3)
             elif kom=='t' :
                 time.sleep(1)
             elif kom=='exit' :
                 sys.exit()

def intro():
         maning=0
         while True:
              os.system('clear')
              print(m+'['+c+'X'+m+']'+p+'=============='+m+'['+c+'+'+m+']'+p+'=============='+m+'['+c+'X'+m+']'+z)
              print(m+'['+p+'*'+m+']'+k+'    Author :'+c+' Mr.F124NZ         '+m+'['+p+'*'+m+']'+z)
              print(m+'['+p+'*'+m+']'+b+'   Facebook : Franz            '+m+'['+p+'*'+m+']'+z)
              print(m+'['+p+'*'+m+']'+h+'   WhatsApp : +6285211523414   '+m+'['+p+'*'+m+']'+z)
              print(m+'['+p+'*'+m+']'+p+'   Version : 0.1               '+m+'['+p+'*'+m+']'+z)
              print(m+'['+c+'X'+m+']'+p+'=============='+m+'['+c+'+'+m+']'+p+'=============='+m+'['+c+'X'+m+']'+z)
              print(p+' Menu '+m+':'+z)
              print(m+'     ['+c+'1'+m+']'+b+' Cmatrix'+z)
              time.sleep(0.01)
              print(m+'     ['+c+'2'+m+']'+b+' Cacafire'+z)
              time.sleep(0.01)
              print(m+'     ['+c+'3'+m+']'+b+' StarWars'+z)
              time.sleep(0.01)
              print(m+'     ['+c+'4'+m+']'+b+' cacademo'+z)
              time.sleep(0.01)
              print(m+'     ['+c+'5'+m+']'+b+' Lokomotif (sl)'+z)
              time.sleep(0.01)
              print(m+'     ['+c+'6'+m+']'+b+' Running Text'+z)
              time.sleep(0.01)
              print(m+'     ['+c+'7'+m+']'+b+' Jam Digital '+z)
              time.sleep(0.01)
              print(m+'     ['+c+'8'+m+']'+b+' Logo (cowsay)'+z)
              time.sleep(0.01)
              print(m+'     ['+c+'0'+m+']'+b+' Exit'+z)
              on=input(c+'     Pilih Nomor '+m+'>'+k+'>'+h+'> '+c)
              if on=='' :
                print(m+'     Tidak Boleh Kosong !'+z)
                time.sleep(1)
                maning+=1
              elif on=='1' :
                  time.sleep(1)
                  os.system('pkg install cmatrix')
                  os.system('clear')
                  os.system('cmatrix')
              elif on=='2' :
                  time.sleep(1)
                  os.system('pkg install libcaca -y')
                  os.system('clear')
                  os.system('cacafire')
              elif on=='3' :
                  os.system('apt install figlet -y')
                  os.system('clear')
                  print(c+' Aktifkan Mode Rotasi Layar (lanskap)'+z)
                  time.sleep(2)
                  print(c+' Menampilkan Animasi ...'+z)
                  time.sleep(1)
                  print(c+' Press ctrl + z To stop '+z)
                  time.sleep(3)
                  os.system('telnet towel.blinkenlights.nl')
              elif on=='4' :
                  time.sleep(1)
                  os.system('pkg install lilcaca -y')
                  os.system('clear')
                  os.system('cacademo')
              elif on=='5' :
                  time.sleep(1)
                  os.system('pkg install sl -y')
                  os.system('clear')
                  os.system('sl')
              elif on=='6' :
                  time.sleep(1)
                  str+teks()
              elif on=='7' :
                  os.system('pkg install tty-clock')
                  os.system('clear')
                  print(h+' Press ctrl + z To Quit'+z)
                  os.system('tty-clock')
              elif on=='8' :
                  os.system('pkg install cowsay -y')
                  logo()
              elif on=='0' :
                  print(m+'     Keluar ...'+z)
                  time.sleep(1)
                  sys.exit()
              else:
                  print(m+'     Masukkan Tidak Tersedia'+z)
                  time.sleep(1)

intro()

