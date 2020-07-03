import phonenumbers, time, ipinfo, pprint, os
from phonenumbers import carrier, timezone
from colorama import Fore

def PhoneNumber():
    numInput = input("Enter Phone Number - GB Only (Ex. = +447777123456) > ")
    ro_number = phonenumbers.parse(numInput, "RO")
    gb_number = phonenumbers.parse(numInput, "GB")
    timezone_gb = timezone.time_zones_for_number(gb_number)
    x = carrier.name_for_number(ro_number, "en")
    print("Carrier: "+(x))
    print("Timezone: "+str((timezone_gb)))

def IPAddress():
    ipInput = input("Enter IP Address (Ex. 1.1.1.1) > ")
    access_token = '48c250a21605e7'
    handler = ipinfo.getHandler(access_token)
    ip_address = ipInput
    details = handler.getDetails(ip_address)
    pprint.pprint(details.all)

print(Fore.RED)
print("                                                    ")
print("                   `/-`    `-/.                     ")
print("                `:ohs.        .sds:`                ")
print("            .+hNNs.            `sNNh+.              ")
print("           yMMMs`                `sMMMy             ")
print("           dMMM:                  :MMMd             ")
print("           mMMMo                  oMMMm             ")
print("           NMMMh      `:oo-`      hMMMN             ")
print("          `NMMMM  `.+ymMNNMmy+.`  MMMMN`            ")
print("          .MMMMM::smNmh+--+hmNms-:MMMMM.            ")
print("        .:yMMMMMNdyso-`    `:osydNMMMMMy:.          ")
print("   ./ymMMMMMMMMMMMMNdy--ydNMMMMMMMMMMMMmy/.         ")
print("  `-+hNMMMMMNmNMMMMMNhhhh//hhhhNMMMMMNmNMMMMMNh+-`  ")
print(" sdNMMMNmho:.:ssdNMMNo        oNMMNdsy-.:ohmNMMMNds ")
print(" MMNhs/-`    /MNs-odMMo      oMMdo-yNM-    `-/shNMM ")
print(" MMo         /MMh  `:+yy.  .yy+:`  dMM-         oMM ")
print(" Mm`         :MMh`   +MMm--mMM/   `dMM-         `mM ")
print(" M/          -dMMmy+--MMMNNMMM.-+hmMNd.          /M ")
print(" d            `-+hNMN:mMMMMMMm:NMmy+.`            d ")
print(" -                `:s/yMMMMMMy+o:`                - ")
print("                    :yNMMMMMMNy:                    ")
print("    `            -smMMMMMMMMMMMMmo-            `    ")
print("    ./+so/:.` .odMMMMMNho::odNMMMMMd+. `.:/os+/.    ")
print("     `:sdMNNMMMMMdo:`      `:odMMMMMNNMds:`         ")
print("         ./yNdo:`              `:sdNy/.             ")
time.sleep(5)
os.system('clear')

print(Fore.GREEN)
print(" ---   --      |  ---   --  |   |  ---     ")
print(" |  | |  | |\  |   |   |  | |   |  |  |    ")
print(" ---  |  | | \ |   |   |  | |   |  |--|    ")
print(" |  | |  | |  \|   |   |  | |   |  |   \   ")
print(" ---   --  |     --     --   ---   |    \ ")

print("                        ")
print("       Welcome to       ")
print("                        ")
print(" |-|-|   ----    |-|-|  ")
print("   |     |   |     |    ")
print("   |     |----     |    ")    
print(" |-|-|   |       |-|-|  ")
print("                        ")
print(" IP      Phone   Info   ")
print("                        ")
print(" Options:               ")
print("                        ")
print (" 1| Phone Number       ")
print (" 2| IP Address         ")
print (" 3| Exit               ")
print ("                       ")
Option = input("Option > ")

if Option == "1":
    PhoneNumber()

elif Option == "2":
    IPAddress()

else:
    print("")
    print("------------")
    print("            ")
    print(" Exiting... ")
    print("            ")
    print("------------")
    time.sleep(3)
    quit
