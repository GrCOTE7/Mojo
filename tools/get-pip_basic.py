import os
import urllib.request

def download_get_pip():
    url = "https://bootstrap.pypa.io/get-pip.py"
    file_name = "get-pip.py"
    
    print("Téléchargement de get-pip.py...")
    urllib.request.urlretrieve(url, file_name)
    print("Téléchargement terminé.")

def install_pip():
    print("Installation de pip...")
    os.system("python3 get-pip.py")
    print("Installation terminée.")

def main():
    download_get_pip()
    install_pip()

if __name__ == "__main__":
    main()
