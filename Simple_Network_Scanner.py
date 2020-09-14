import subprocess

Network = "192.168.0."

for i in range(1, 255):
    IP = Network + str(i)
    p = subprocess.Popen(' ping -c 1 -W 1 ' + IP, stdout=subprocess.PIPE, shell=True)
    p.wait()

    if IP == "192.168.0.2":
        print("\033[1;32;1m [+] \033[1;31;2mCRISTIAN :)\033[1;32;1m IS IN THE NETWORK\033[1;32;0m\n")

    if p.poll() == 0:
        print("\033[1;32;1m [+] %s IS IN THE NETWORK\033[1;32;0m\n" % IP)

