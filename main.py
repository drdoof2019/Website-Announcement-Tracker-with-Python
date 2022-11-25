# Importing libraries
import time
import hashlib
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup

# setting the URL you want to monitor
url = Request('http://eee.gantep.edu.tr/duyurular.php',
              headers={'User-Agent': 'Mozilla/5.0'})

print("İlk kayıt için hazırlanılıyor")
time.sleep(5)
# to perform a GET request and load the
# content of the website and store it in a var
response = urlopen(url).read()
# print(response)

# To remove all html tags
cleantext = BeautifulSoup(response, "lxml").text
# To remove all whitespaces
cleantext = ''.join(cleantext.split())

# gonna be used for save hash
# with open("ilkkayitclean.txt","w") as file:
#     file.write(str(cleantext))

# to create the initial hash
currentHash = hashlib.sha224(cleantext.encode('utf-8')).hexdigest()
print("ilk kayıt başarılı")
print(currentHash)
# wait for 30 seconds
time.sleep(5)
while True:
    try:
        # perform the get request
        response = urlopen(url).read()
        time.sleep(5)

        # To remove all html tags
        cleantext = BeautifulSoup(response, "lxml").text
        # To remove all whitespaces
        cleantext = ''.join(cleantext.split())

        # create a new hash
        newHash = hashlib.sha224(cleantext.encode('utf-8')).hexdigest()
        print(f"newHash:{newHash}")
        # check if new hash is same as the previous hash
        if newHash == currentHash:
            continue

        # if something changed in the hashes
        else:
            # notify
            print("something changed")

            currentHash = newHash

            # wait for 30 seconds
            time.sleep(5)
            continue

    # To handle exceptions
    except Exception as e:
        print("error")
