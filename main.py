import os, sys
try:
    import fade
except IndexError:
    os.system("pip install fade")
    import fade
try:
    from colorama import Fore
except IndexError:
    os.system("pip install Fore")
    os.system("pip install colorama")
    from colorama import Fore
try:
    from pystyle import *
except IndexError:
    os.system("pip install pystyle")
    from pystyle import *
gui="""
    ╔═══════════════════════════╗ ╔═════════════════════╗
    ║    ╔╗╔╔═╗═╗ ╦╦╦ ╦╔═╗      ║ ║ [discord.gg/noxius] ║
    ║    ║║║║ ║╔╩╦╝║║ ║╚═╗      ║ ║                     ║
    ║    ╝╚╝╚═╝╩ ╚═╩╚═╝╚═╝      ║ ║  [Project Noxius]   ║
    ╚═══════════════════════════╝ ╚═════════════════════╝
    ╔═══════════════════════════════════════════════════╗
    ║           [Noxius Serial Checker]                 ║
    ║       [!] https://discord.gg/noxius [!]           ║
    ╚═══════════════════════════════════════════════════╝
"""
os.system("@mode con cols=90 lines=56")
os.system("title Project Noxius Serial Checker ^| Press any key to refresh")
faded_gui=fade.pinkred(gui)
while(True):
    os.system("cls")
    print(faded_gui)
    Write.Print("[</>] Baseboard\n", Colors.red_to_purple, interval=0.001)
    os.system("wmic baseboard get serialnumber")
    Write.Print("[</>] Mac\n", Colors.red_to_purple, interval=0.001)
    os.system("""wmic path Win32_NetworkAdapter where "PNPDeviceID like '%%PCI%%' AND NetConnectionStatus=2 AND AdapterTypeID='0'" get MacAddress""")
    Write.Print("[</>] CPU\n", Colors.red_to_purple, interval=0.001)
    os.system("wmic cpu get processorid")
    Write.Print("[</>] GPU\n", Colors.red_to_purple, interval=0.001)
    os.system("wmic PATH Win32_VideoController GET Description,PNPDeviceID")
    Write.Print("[</>] DISK DRIVE\n", Colors.red_to_purple, interval=0.001)
    os.system("wmic diskdrive get serialnumber")
    Write.Print("[</>] MotherBoard\n", Colors.red_to_purple, interval=0.001)
    os.system("wmic baseboard get serialnumber")
    Write.Print("[</>] RAM\n", Colors.red_to_purple, interval=0.001)
    os.system("wmic memorychip get serialnumber")
    Write.Print("[</>] Bios\n", Colors.red_to_purple, interval=0.001)
    os.system("wmic bios get serialnumber")
    Write.Print("[</>] smBios\n", Colors.red_to_purple, interval=0.001)
    os.system("wmic csproduct get uuid")





    os.system("pause >nul")
