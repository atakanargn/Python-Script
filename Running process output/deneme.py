import subprocess

def islem(cmd):    
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    while(True):
        # returns None while subprocess is running
        retcode = p.poll()
        line = p.stdout.readline()
        yield line
        if retcode is not None:
            break

def baslat(mlist):
    for line in islem(mlist):
        gelenDeger = line.decode("utf8")
        print(gelenDeger)

while 1:
    baslat(["bash" ,"yaz.sh"])