import requests
from bs4 import BeautifulSoup
print("""
**********************
T�rk�e - �ngilizce
�ngilizce - T�rk�e 
    v.1 S�zl�k
    
created by Omer Akkoyun
*********************


""")
while True:
    sozluk=input("\n�evirmek istedi�iniz kelime = ")
    url="https://tr.bab.la/sozluk/turkce-ingilizce/"+sozluk
    response= requests.get(url)
    html_icerigi=response.content
    soup=BeautifulSoup(html_icerigi,"html.parser")

    listem =[]

    for i in soup.find_all("div",{"class":"quick-result-overview"}):

        i=i.text
        i=i.split()
        listem.append(i)
        break


    for i in listem:
        if "Ekibimiz" not in i:
            print("�evirisi ba�ar�l�yla yap�ld�\n","  ",sozluk,"�evirisi ")
            print("--------------------")

        else:
            print("\n�zg�n�z,B�yle bir kelime bulunamad�!")
            break

        for i in (listem[0][1:]):
            print(i)
        print("--------------------")






