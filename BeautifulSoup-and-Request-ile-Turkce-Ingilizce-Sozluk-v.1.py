import requests
from bs4 import BeautifulSoup
print("""
**********************
Türkçe - Ýngilizce
Ýngilizce - Türkçe 
    v.1 Sözlük
    
created by Omer Akkoyun
*********************


""")
while True:
    sozluk=input("\nÇevirmek istediðiniz kelime = ")
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
            print("Çevirisi baþarýlýyla yapýldý\n","  ",sozluk,"çevirisi ")
            print("--------------------")

        else:
            print("\nÜzgünüz,Böyle bir kelime bulunamadý!")
            break

        for i in (listem[0][1:]):
            print(i)
        print("--------------------")






