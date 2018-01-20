"""
Yazar : Atakan Argın
Github : atakanargn

Amaç;
    NTV Haber sitesinden kategoriye ve sayfa sayısına göre haber çekme

Eksiklikler;
    # Galeri ve Video haberlerini çekmiyor.
    # Bazı haberlerde "datalayer.push{}" verisini dosya sonuna kaydediyor, düzeltilecek.
    # AttributeError hatası düzeltilecek.

"""

# Dosya oluşturma işlemi için kullanılacak kütüphane
from os import system

# Siteden veri çekmek için kullanılan kütüphaneler
import urllib.request
from bs4 import BeautifulSoup

"""
NTV Sitesindeki kategoriler;

Türkiye : turkiye
Dünya : dunya
Ekonomi : ekonomi
Spor : spor
Yaşam : yasam
Sağlık : saglik
Teknoloji : teknoloji
Emlak : emlak
Sanat : sanat
Otomobil : otomobil
Eğitim : egitim

"""
#Kategori seçiyoruz
haberKategori = "turkiye"
#Kaç sayfa çekilecek ?
sayfaSayi=1

#Istediğimiz sayfa sayısına kadar dönmesini istedik
for sayfa in range(1,sayfaSayi+1,1):
    #Haberleri çekeceğimiz url
    haberSitesi = "https://www.ntv.com.tr/"+haberKategori+"/?sayfa="+str(sayfa)
    haberSitesi = urllib.request.urlopen(haberSitesi)

    #BeatifulSoup'un HTML ayrıştırma özelliğini seçtik
    #Parse = Ayrıştırmak
    haberler = BeautifulSoup(haberSitesi, 'html.parser')

    #HTML içinden div'ler arasından sadece class'ı "addthis_toolbox" olan div'leri çektik
    haberler = haberler.find_all('div', attrs={'class': 'addthis_toolbox'})

    #haberler dizisinin elemanlarını haber değişkenine atadık ve işleme soktuk
    for haber in haberler:

        #AttributeError hatasına geçici çözüm getirdik. (DAHA SONRA DÜZELTİLECEK!)
        #Düzeltmeniz halinde benle paylaşırsanız sevinirim :)
        try:

            #Haber kodları içinden addthis:title'ı yani başlığı çektik
            haberBaslik = haber.get("addthis:title")
            #Haber kodları içinden addthis:url'i yani url'i çektik
            haberUrl = haber.get("addthis:url")

            #Haberin içeriğini almak için
            #Çektiğimiz haber url'ine giriş yaptık
            haberUrl = urllib.request.urlopen(haberUrl)

            #Haber sayfası için
            #BeatifulSoup'un HTML ayrıştırma özelliğini seçtik
            haberIcerikSayfasi = BeautifulSoup(haberUrl, 'html.parser')

            #Haber sayfası içindeki div'lerden sadece itemprop'u "articleBody" olanları çektik
            #.text ile string haline getirip
            #.strip() ile fazla olan boşlukları temizledik
            haberIcerik = haberIcerikSayfasi.find('div', attrs={'itemprop':'articleBody'}).text.strip()
            #Haber başlığı ve içeriğini yazdırdık
            print("\n"+haberBaslik+"\n\n"+haberIcerik)
            print("\n\n\n")

            #Linux için kategori ismine sahip dosya oluşturma işlemi yaptık
            system("mkdir "+haberKategori)

            #Windows için kategori ismine sahip dosya oluşturma işlemi yaptık
            # -----------------
            # system("md "+haberKategori)

            #Haberin başlığına sahip yeni bir dosya oluşturduk
            dosya=open(haberKategori+"/"+haberBaslik+".txt","w")
            #Haber içeriğini dosyaya yazdırdık
            dosya.write(haberIcerik)
            #Dosyayı kapattık
            dosya.close()
            print("HABER KAYDEDİLDİ!!!")
        except AttributeError:
            #Hata vermesi durumunda hiç birşey olmamış gibi devam etmesini sağladık
            #(DAHA SONRA HATALAR DÜZELTİLECEK)
            continue