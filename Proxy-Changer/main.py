from selenium import webdriver
import requests
from sys import argv

def main():
    # Proxyyi siteden çektik, ip ve portu aldık
    # 1 https://gimmeproxy.com/api/getProxy
    # 2 https://api.getproxylist.com/proxy
    proxyCek = requests.get("https://gimmeproxy.com/api/getProxy")
    proxy,port = proxyCek.json()['ip'], proxyCek.json()['port']

    # Firefox proxy ayarlarını değiştirdik
    profile = webdriver.FirefoxProfile()
    profile.set_preference("network.proxy.type", 1) 
    profile.set_preference("network.proxy.http", proxy) 
    profile.set_preference("network.proxy.http_port", int(port))
    profile.set_preference("network.proxy.ssl", proxy) 
    profile.set_preference("network.proxy.ssl_port", int(port))
    profile.set_preference("javascript.enabled", True)
    profile.update_preferences() 

    # GeckoDriver konumuna göre siteye girdik
    driver = webdriver.Firefox(executable_path="/home/atakan/DESKTOP/Python Projeler/Proxy-CHAnger/geckodriver", firefox_profile=profile) 
    #system("x-terminal-emulator -c -e python mouse.py")
    driver.get(argv[1])

if __name__ == "__main__":
    main()