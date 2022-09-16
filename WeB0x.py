import os
import webbrowser
from colorama import Fore

#اول اداة ب اسم whois تحتاج محرر برمجي مثل باي شارم او فيجوال ستيديو كود او كومنتي للتشغيل

#The first tool with a name whois You need a software editor like Pychram, Visual Studio Code, or Community to run 

bs = Fore.CYAN+"""
 ___       __   _______   ________  ________     ___    ___ 
|\  \     |\  \|\  ___ \ |\   __  \|\   __  \   |\  \  /  /|
\ \  \    \ \  \ \   __/|\ \  \|\ /\ \  \|\  \  \ \  \/  / /
 \ \  \  __\ \  \ \  \_|/_\ \   __  \ \  \\\  \  \ \    / / 
  \ \  \|\__\_\  \ \  \_|\ \ \  \|\  \ \  \\\  \  /     \/  
   \ \____________\ \_______\ \_______\ \_______\/  /\   \  
    \|____________|\|_______|\|_______|\|_______/__/ /\ __\ 
                                                |__|/ \|__| 
                                                
"""
bn = Fore.RED+"""
                        ,--,                                                       ,--,                    ,--. 
           .---.      ,--.'|                             .--.--.                 ,--.'|                  ,--.'| 
          /. ./|   ,--,  | :                    ,--,    /  /    '.            ,--,  | :              ,--,:  : | 
      .--'.  ' ;,---.'|  : '   ,---.          ,--.'|   |  :  /`. /         ,---.'|  : '           ,`--.'`|  ' : 
     /__./ \ : ||   | : _' |  '   ,'\         |  |,    ;  |  |--`          |   | : _' |,--,  ,--, |   :  :  | | 
 .--'.  '   \' .:   : |.'  | /   /   |        `--'_    |  :  ;_            :   : |.'  ||'. \/ .`| :   |   \ | : 
/___/ \ |    ' '|   ' '  ; :.   ; ,. :        ,' ,'|    \  \    `.         |   ' '  ; :'  \/  / ; |   : '  '; | 
;   \  \;      :'   |  .'. |'   | |: :        '  | |     `----.   \        '   |  .'. | \  \.' /  '   ' ;.    ; 
 \   ;  `      ||   | :  | ''   | .; :        |  | :     __ \  \  |        |   | :  | '  \  ;  ;  |   | | \   | 
  .   \    .\  ;'   : |  : ;|   :    |        '  : |__  /  /`--'  /        '   : |  : ; / \  \  \ '   : |  ; .' 
   \   \   ' \ ||   | '  ,/  \   \  /         |  | '.'|'--'.     /         |   | '  ,/./__;   ;  \|   | '`--'   
    :   '  |--" ;   : ;--'    `----'          ;  :    ;  `--'---'          ;   : ;--' |   :/\  \ ;'   : |       
     \   \ ;    |   ,/                        |  ,   /                     |   ,/     `---'  `--` ;   |.'       
      '---"     '---'                          ---`-'                      '---'                  '---'  
"""
bn1 = Fore.BLUE+"""
                                ,----,                                                        
                              ,/   .`|       ,--,                ,--,                    ,--. 
    ,---,.                  ,`   .'  :     ,--.'|              ,--.'|                  ,--.'| 
  ,'  .'  \         ,--,  ;    ;     /  ,--,  | :           ,--,  | :              ,--,:  : | 
,---.' .' |       ,'_ /|.'___,/    ,',---.'|  : '        ,---.'|  : '           ,`--.'`|  ' : 
|   |  |: |  .--. |  | :|    :     | |   | : _' |        |   | : _' |,--,  ,--, |   :  :  | | 
:   :  :  /,'_ /| :  . |;    |.';  ; :   : |.'  |        :   : |.'  ||'. \/ .`| :   |   \ | : 
:   |    ; |  ' | |  . .`----'  |  | |   ' '  ; :        |   ' '  ; :'  \/  / ; |   : '  '; | 
|   :     \|  | ' |  | |    '   :  ; '   |  .'. |        '   |  .'. | \  \.' /  '   ' ;.    ; 
|   |   . |:  | | :  ' ;    |   |  ' |   | :  | '        |   | :  | '  \  ;  ;  |   | | \   | 
'   :  '; ||  ; ' |  | '    '   :  | '   : |  : ;        '   : |  : ; / \  \  \ '   : |  ; .' 
|   |  | ; :  | : ;  ; |    ;   |.'  |   | '  ,/         |   | '  ,/./__;   ;  \|   | '`--'   
|   :   /  '  :  `--'   \   '---'    ;   : ;--'          ;   : ;--' |   :/\  \ ;'   : |       
|   | ,'   :  ,      .-./            |   ,/              |   ,/     `---'  `--` ;   |.'       
`----'      `--`----'                '---'               '---'                  '---'         
"""
bn2 = Fore.CYAN+"""
                      ,--,                                                                                                       
                   ,---.'|                                                                          ,--,                    ,--. 
    ,---,.         |   | :       ,---,.                   .---.    ,---,.    ,---,.               ,--.'|                  ,--.'| 
  ,'  .' |  ,--,   :   : |     ,'  .' |                  /. ./|  ,'  .' |  ,'  .'  \           ,--,  | :              ,--,:  : | 
,---.'   |,--.'|   |   ' :   ,---.'   |              .--'.  ' ;,---.'   |,---.' .' |        ,---.'|  : '           ,`--.'`|  ' : 
|   |   .'|  |,    ;   ; '   |   |   .'             /__./ \ : ||   |   .'|   |  |: |        |   | : _' |,--,  ,--, |   :  :  | | 
:   :  :  `--'_    '   | |__ :   :  |-,         .--'.  '   \' .:   :  |-,:   :  :  /        :   : |.'  ||'. \/ .`| :   |   \ | : 
:   |  |-,,' ,'|   |   | :.'|:   |  ;/|        /___/ \ |    ' ':   |  ;/|:   |    ;         |   ' '  ; :'  \/  / ; |   : '  '; | 
|   :  ;/|'  | |   '   :    ;|   :   .'        ;   \  \;      :|   :   .'|   :     \        '   |  .'. | \  \.' /  '   ' ;.    ; 
|   |   .'|  | :   |   |  ./ |   |  |-,         \   ;  `      ||   |  |-,|   |   . |        |   | :  | '  \  ;  ;  |   | | \   | 
'   :  '  '  : |__ ;   : ;   '   :  ;/|          .   \    .\  ;'   :  ;/|'   :  '; |        '   : |  : ; / \  \  \ '   : |  ; .' 
|   |  |  |  | '.'||   ,/    |   |    \           \   \   ' \ ||   |    \|   |  | ;         |   | '  ,/./__;   ;  \|   | '`--'   
|   :  \  ;  :    ;'---'     |   :   .'            :   '  |--" |   :   .'|   :   /          ;   : ;--' |   :/\  \ ;'   : |       
|   | ,'  |  ,   /           |   | ,'               \   \ ;    |   | ,'  |   | ,'           |   ,/     `---'  `--` ;   |.'       
`----'     ---`-'            `----'                  '---"     `----'    `----'             '---'                  '---'         
"""
ls = (Fore.CYAN+"""
 [1] Pc ~ WinDows / LinUx ( iDE only)

 [2] Phone ~ UniX (Android) / ioS
""")
print(bs)
#اول اداة ب اسم whois تحتاج محرر برمجي مثل باي شارم او فيجوال ستيديو كود او كومنتي للتشغيل

#The first tool with a name whois You need a software editor like Pychram, Visual Studio Code, or Community to run
print("""
\t      Click Url To Login HxN Store
\n
\t   My Store : # https://hxn.sellix.io
\n
\t\t instagram : @hxn.ops
\t\t  TeleGram : @HEXiN1K
\t\t    GiTHuB : @HXN2
\n
\t\t      Version 1.0
\n
\t      To Check Update Visit GiTHuB 
""")
print(ls)
import os
ls = int(input (" [=] Please Choose your number =>> : "))
if ls ==1:
   def whois():
    import whois
    print(bn)
    url = input(Fore.CYAN+" [=] Enter WeBSitE To CheCk : ")
    info = whois.whois(url)
    print(info)
    whois()

def buth():
    import builtwith
    print(bn1)
    url1 = input(Fore.CYAN+" [=] Enter WeBsItE TO Stauts : ")
    info1 = builtwith.parse(url1)
    print(info1)
buth()

def fwb():
    import webbrowser
    print(bn2)
    url2 = input(Fore.CYAN+" [=] Enter WeBsiTe To FiLeS : ")
    webbrowser.open(url2+"/sitemap.xml")
fwb()

#اول اداة ب اسم whois تحتاج محرر برمجي مثل باي شارم او فيجوال ستيديو كود او كومنتي للتشغيل

#The first tool with a name whois You need a software editor like Pychram, Visual Studio Code, or Community to run

while True:
    os.system("clear")
    os.system("cls")
    v = ("""
    [1] ReLoaD T0oL whois [ Pc ~ WinDows / LinUx ( iDE only) Only ?
    
    [2] ReLoaD T0oL ButH ?
    
    [3] ReLoaD T0oL FiLe HxN ?
    
    [4] instagram HxN
    
    [5] TeleGram HxN

    [6] HxN Store To Buy Private TooLs
    
    [99] ExiT ?
    """)
    print(v)
    v = input(" [-] Type Your Choose : ")
    if v == '1':
        whois()

    if v == '2':
        buth()

    if v == '3':
        fwb()

    if v == '4':
        os.system("clear")
        os.system("cls")
        url5 = "https://instagram.com/hxn.ops"
        webbrowser.open(url5)
        os.system("clear")
        os.system("cls")

    if v == '5':
        os.system("clear")
        os.system("cls")
        url6 = "https://t.me/HEXiN1K"
        webbrowser.open(url6)
        os.system("clear")
        os.system("cls")
        
    if v == '6':
       os.system("clear")
       os.system("cls")
       url7 = "https://hxn.sellix.io"
       webbrowser.open(url7)
       os.system("clear")
       os.system("cls")

    if v == '99':
        exit(0)

        
if ls == 2:
   def buth():
    import builtwith
    print(bn1)
    url1 = input(Fore.CYAN+" [=] Enter WeBsItE TO Stauts : ")
    info1 = builtwith.parse(url1)
    print(info1)
buth()

def fwb():
    import webbrowser
    print(bn2)
    url2 = input(Fore.CYAN+" [=] Enter WeBsiTe To FiLeS : ")
    webbrowser.open(url2+"/sitemap.xml")
fwb()

#اول اداة ب اسم whois تحتاج محرر برمجي مثل باي شارم او فيجوال ستيديو كود او كومنتي للتشغيل

#The first tool with a name whois You need a software editor like Pychram, Visual Studio Code, or Community to run

while True:
    os.sytem("clear")
    os.system("cls")
    v = ("""
    [1] ReLoaD T0oL whois [ Pc ~ WinDows / LinUx ( iDE only) Only ?
    
    [2] ReLoaD T0oL ButH ?
    
    [3] ReLoaD T0oL FiLe HxN ?
    
    [4] instagram HxN
    
    [5] TeleGram HxN

    [6] HxN Store To Buy Private TooLs
    
    [99] ExiT ?
    """)
    print(v)
    v = input(" [-] Type Your Choose : ")
    if v == '1':
        whois()

    if v == '2':
        buth()

    if v == '3':
        fwb()

    if v == '4':
        os.system("clear")
        os.system("cls")
        url5 = "https://instagram.com/hxn.ops"
        webbrowser.open(url5)
        os.system("clear")
        os.system("cls")

    if v == '5':
        os.system("clear")
        os.system("cls")
        url6 = "https://t.me/HEXiN1K"
        webbrowser.open(url6)
        os.system("clear")
        os.system("cls")
        
    if v == '6':
       os.system("clear")
       os.system("cls")
       url7 = "https://hxn.sellix.io"
       webbrowser.open(url7)
       os.system("clear")
       os.system("cls")

    if v == '99':
        exit(0)

#اول اداة ب اسم whois تحتاج محرر برمجي مثل باي شارم او فيجوال ستيديو كود او كومنتي للتشغيل

#The first tool with a name whois You need a software editor like Pychram, Visual Studio Code, or Community to run
