import sqlite3
def KrediKartıBorçBilgi(kimsin,soru):
    KHB=sqlite3.connect('KisiHesapBilgileri.db')
    im=KHB.cursor()
    tablo_yap=("CREATE TABLE IF NOT EXISTS hesap_bilgisi(AdSoyad,KartNo,Şifre,İban,Bakiye,SimBloke,KKFatura,Tlf,Elek,Su,gaz,trafik)")
    im.execute(tablo_yap)
    im.execute("""SELECT * FROM hesap_bilgisi""")
    veriler=im.fetchall()
    final_result=[list(i)for i in veriler]
    while True:
        if kimsin == 0:
            Cemal=final_result[0]
            Bakiye=Cemal[4]
            KrediKFatura=Cemal[6]
            im=KHB.cursor()
            tablo_yap=("CREATE TABLE IF NOT EXISTS hesap_bilgisi(AdSoyad,KartNo,Şifre,İban,Bakiye,SimBloke,KKFatura,Tlf,Elek,Su,gaz,trafik)")
            im.execute(tablo_yap)
            im.execute("""SELECT * FROM hesap_bilgisi""")
            print("Faturanız",KrediKFatura,"TL dir")
            degis=("UPDATE hesap_bilgisi SET KKFatura =?")
            BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
            KrediFaturaOde=int(input("Lütfen ödemek istediğiniz miktarı giriniz:"))
            if KrediFaturaOde>Bakiye:
                print("Yetersiz Bakiye")
            else:
                KrediFaturaSonMiktar=KrediKFatura-KrediFaturaOde
                if KrediFaturaSonMiktar<0:
                    BakiyeSon=Bakiye-KrediKFatura
                    SonFatura=0
                    degis=("UPDATE hesap_bilgisi SET KKFatura = ?")
                    im.execute(degis,[SonFatura])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı 0 TL dir")
                else:
                    BakiyeSon=Bakiye-KrediFaturaOde
                    im.execute(degis,[KrediFaturaSonMiktar])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı",KrediFaturaSonMiktar,"TL dir")
                return KrediKFatura
            break
        elif kimsin == 1:
            Cemal=final_result[1]
            Bakiye=Cemal[4]
            KrediKFatura=Cemal[6]
            im=KHB.cursor()
            tablo_yap=("CREATE TABLE IF NOT EXISTS hesap_bilgisi(AdSoyad,KartNo,Şifre,İban,Bakiye,SimBloke,KKFatura,Tlf,Elek,Su,gaz,trafik)")
            im.execute(tablo_yap)
            im.execute("""SELECT * FROM hesap_bilgisi""")
            print("Faturanız",KrediKFatura,"TL dir")
            degis=("UPDATE hesap_bilgisi SET KKFatura =?")
            BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
            KrediFaturaOde=int(input("Lütfen ödemek istediğiniz miktarı giriniz:"))
            if KrediFaturaOde>Bakiye:
                print("Yetersiz Bakiye")
            else:
                KrediFaturaSonMiktar=KrediKFatura-KrediFaturaOde
                if KrediFaturaSonMiktar<0:
                    BakiyeSon=Bakiye-KrediKFatura
                    SonFatura=0
                    degis=("UPDATE hesap_bilgisi SET KKFatura = ?")
                    im.execute(degis,[SonFatura])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı 0 TL dir")
                else:
                    BakiyeSon=Bakiye-KrediFaturaOde
                    im.execute(degis,[KrediFaturaSonMiktar])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı",KrediFaturaSonMiktar,"TL dir")
                return KrediKFatura
            break
        elif kimsin == 2:
            Cemal=final_result[2]
            Cemal=final_result[1]
            Bakiye=Cemal[4]
            KrediKFatura=Cemal[6]
            im=KHB.cursor()
            tablo_yap=("CREATE TABLE IF NOT EXISTS hesap_bilgisi(AdSoyad,KartNo,Şifre,İban,Bakiye,SimBloke,KKFatura,Tlf,Elek,Su,gaz,trafik)")
            im.execute(tablo_yap)
            im.execute("""SELECT * FROM hesap_bilgisi""")
            print("Faturanız",KrediKFatura,"TL dir")
            degis=("UPDATE hesap_bilgisi SET KKFatura =?")
            BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
            KrediFaturaOde=int(input("Lütfen ödemek istediğiniz miktarı giriniz:"))
            if KrediFaturaOde>Bakiye:
                print("Yetersiz Bakiye")
            else:
                KrediFaturaSonMiktar=KrediKFatura-KrediFaturaOde
                if KrediFaturaSonMiktar<0:
                    BakiyeSon=Bakiye-KrediKFatura
                    SonFatura=0
                    degis=("UPDATE hesap_bilgisi SET KKFatura = ?")
                    im.execute(degis,[SonFatura])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı 0 TL dir")
                else:
                    BakiyeSon=Bakiye-KrediFaturaOde
                    im.execute(degis,[KrediFaturaSonMiktar])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()

                    print("Faturanızda Kalan Borç Miktarı",KrediFaturaSonMiktar,"TL dir")
                return KrediKFatura
            break
        if soru=="e":
            print ("Kalan Bakiyeniz",BakiyeSon,"TL dir")
        else:
            break
def TelefonFatura(kimsin,soru):
    KHB=sqlite3.connect('KisiHesapBilgileri.db')
    im=KHB.cursor()
    tablo_yap=("CREATE TABLE IF NOT EXISTS hesap_bilgisi(AdSoyad,KartNo,Şifre,İban,Bakiye,SimBloke,KKFatura,Tlf,Elek,Su,gaz,trafik)")
    im.execute(tablo_yap)
    im.execute("""SELECT * FROM hesap_bilgisi""")
    veriler=im.fetchall()
    final_result=[list(i)for i in veriler]
    while True:
        if kimsin == 0:
            Cemal=final_result[0]
            Bakiye=Cemal[4]
            KrediKFatura=Cemal[7]
            im=KHB.cursor()
            tablo_yap=("CREATE TABLE IF NOT EXISTS hesap_bilgisi(AdSoyad,KartNo,Şifre,İban,Bakiye,SimBloke,KKFatura,Tlf,Elek,Su,gaz,trafik)")
            im.execute(tablo_yap)
            im.execute("""SELECT * FROM hesap_bilgisi""")
            print("Faturanız",KrediKFatura,"TL dir")
            degis=("UPDATE hesap_bilgisi SET Tlf =?")
            BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
            KrediFaturaOde=int(input("Lütfen ödemek istediğiniz miktarı giriniz:"))
            if KrediFaturaOde>Bakiye:
                print("Yetersiz Bakiye")
            else:
                KrediFaturaSonMiktar=KrediKFatura-KrediFaturaOde
                if KrediFaturaSonMiktar<0:
                    BakiyeSon=Bakiye-KrediKFatura
                    SonFatura=0
                    degis=("UPDATE hesap_bilgisi SET Tlf = ?")
                    im.execute(degis,[SonFatura])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı 0 TL dir")
                else:
                    BakiyeSon=Bakiye-KrediFaturaOde
                    im.execute(degis,[KrediFaturaSonMiktar])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı",KrediFaturaSonMiktar,"TL dir")
                return KrediKFatura
            break
        elif kimsin == 1:
            Cemal=final_result[1]
            Bakiye=Cemal[4]
            KrediKFatura=Cemal[7]
            im=KHB.cursor()
            tablo_yap=("CREATE TABLE IF NOT EXISTS hesap_bilgisi(AdSoyad,KartNo,Şifre,İban,Bakiye,SimBloke,KKFatura,Tlf,Elek,Su,gaz,trafik)")
            im.execute(tablo_yap)
            im.execute("""SELECT * FROM hesap_bilgisi""")
            print("Faturanız",KrediKFatura,"TL dir")
            degis=("UPDATE hesap_bilgisi SET Tlf =?")
            BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
            KrediFaturaOde=int(input("Lütfen ödemek istediğiniz miktarı giriniz:"))
            if KrediFaturaOde>Bakiye:
                print("Yetersiz Bakiye")
            else:
                KrediFaturaSonMiktar=KrediKFatura-KrediFaturaOde
                if KrediFaturaSonMiktar<0:
                    BakiyeSon=Bakiye-KrediKFatura
                    SonFatura=0
                    degis=("UPDATE hesap_bilgisi SET Tlf = ?")
                    im.execute(degis,[SonFatura])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı 0 TL dir")
                else:
                    BakiyeSon=Bakiye-KrediFaturaOde
                    im.execute(degis,[KrediFaturaSonMiktar])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı",KrediFaturaSonMiktar,"TL dir")
                return KrediKFatura
            break
        elif kimsin == 2:
            Cemal=final_result[2]
            Bakiye=Cemal[4]
            KrediKFatura=Cemal[7]
            im=KHB.cursor()
            tablo_yap=("CREATE TABLE IF NOT EXISTS hesap_bilgisi(AdSoyad,KartNo,Şifre,İban,Bakiye,SimBloke,KKFatura,Tlf,Elek,Su,gaz,trafik)")
            im.execute(tablo_yap)
            im.execute("""SELECT * FROM hesap_bilgisi""")
            print("Faturanız",KrediKFatura,"TL dir")
            degis=("UPDATE hesap_bilgisi SET Tlf =?")
            BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
            KrediFaturaOde=int(input("Lütfen ödemek istediğiniz miktarı giriniz:"))
            if KrediFaturaOde>Bakiye:
                print("Yetersiz Bakiye")
            else:
                KrediFaturaSonMiktar=KrediKFatura-KrediFaturaOde
                if KrediFaturaSonMiktar<0:
                    BakiyeSon=Bakiye-KrediKFatura
                    SonFatura=0
                    degis=("UPDATE hesap_bilgisi SET Tlf = ?")
                    im.execute(degis,[SonFatura])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı 0 TL dir")
                else:
                    BakiyeSon=Bakiye-KrediFaturaOde
                    im.execute(degis,[KrediFaturaSonMiktar])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı",KrediFaturaSonMiktar,"TL dir")
                return KrediKFatura
            break
        if soru=="e":
            print ("Kalan Bakiyeniz",BakiyeSon,"TL dir")
        else:
            break
def ElektrikFatura(kimsin,soru):
    KHB=sqlite3.connect('KisiHesapBilgileri.db')
    im=KHB.cursor()
    tablo_yap=("CREATE TABLE IF NOT EXISTS hesap_bilgisi(AdSoyad,KartNo,Şifre,İban,Bakiye,SimBloke,KKFatura,Tlf,Elek,Su,gaz,trafik)")
    im.execute(tablo_yap)
    im.execute("""SELECT * FROM hesap_bilgisi""")
    veriler=im.fetchall()
    final_result=[list(i)for i in veriler]
    while True:
        if kimsin == 0:
            Cemal=final_result[0]
            Bakiye=Cemal[4]
            KrediKFatura=Cemal[8]
            im=KHB.cursor()
            tablo_yap=("CREATE TABLE IF NOT EXISTS hesap_bilgisi(AdSoyad,KartNo,Şifre,İban,Bakiye,SimBloke,KKFatura,Tlf,Elek,Su,gaz,trafik)")
            im.execute(tablo_yap)
            im.execute("""SELECT * FROM hesap_bilgisi""")
            print("Faturanız",KrediKFatura,"TL dir")
            degis=("UPDATE hesap_bilgisi SET Elek =?")
            BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
            KrediFaturaOde=int(input("Lütfen ödemek istediğiniz miktarı giriniz:"))
            if KrediFaturaOde>Bakiye:
                print("Yetersiz Bakiye")
            else:
                KrediFaturaSonMiktar=KrediKFatura-KrediFaturaOde
                if KrediFaturaSonMiktar<0:
                    BakiyeSon=Bakiye-KrediKFatura
                    SonFatura=0
                    degis=("UPDATE hesap_bilgisi SET Elek = ?")
                    im.execute(degis,[SonFatura])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı 0 TL dir")
                else:
                    BakiyeSon=Bakiye-KrediFaturaOde
                    im.execute(degis,[KrediFaturaSonMiktar])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı",KrediFaturaSonMiktar,"TL dir")
                return KrediKFatura
            break
        elif kimsin == 1:
            Cemal=final_result[1]
            Bakiye=Cemal[4]
            KrediKFatura=Cemal[8]
            im=KHB.cursor()
            tablo_yap=("CREATE TABLE IF NOT EXISTS hesap_bilgisi(AdSoyad,KartNo,Şifre,İban,Bakiye,SimBloke,KKFatura,Tlf,Elek,Su,gaz,trafik)")
            im.execute(tablo_yap)
            im.execute("""SELECT * FROM hesap_bilgisi""")
            print("Faturanız",KrediKFatura,"TL dir")
            degis=("UPDATE hesap_bilgisi SET Elek =?")
            BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
            KrediFaturaOde=int(input("Lütfen ödemek istediğiniz miktarı giriniz:"))
            if KrediFaturaOde>Bakiye:
                print("Yetersiz Bakiye")
            else:
                KrediFaturaSonMiktar=KrediKFatura-KrediFaturaOde
                if KrediFaturaSonMiktar<0:
                    BakiyeSon=Bakiye-KrediKFatura
                    SonFatura=0
                    degis=("UPDATE hesap_bilgisi SET Elek = ?")
                    im.execute(degis,[SonFatura])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı 0 TL dir")
                else:
                    BakiyeSon=Bakiye-KrediFaturaOde
                    im.execute(degis,[KrediFaturaSonMiktar])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı",KrediFaturaSonMiktar,"TL dir")
                return KrediKFatura
            break
        elif kimsin == 2:
            Cemal=final_result[2]
            Bakiye=Cemal[4]
            KrediKFatura=Cemal[8]
            im=KHB.cursor()
            tablo_yap=("CREATE TABLE IF NOT EXISTS hesap_bilgisi(AdSoyad,KartNo,Şifre,İban,Bakiye,SimBloke,KKFatura,Tlf,Elek,Su,gaz,trafik)")
            im.execute(tablo_yap)
            im.execute("""SELECT * FROM hesap_bilgisi""")
            print("Faturanız",KrediKFatura,"TL dir")
            degis=("UPDATE hesap_bilgisi SET Elek =?")
            BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
            KrediFaturaOde=int(input("Lütfen ödemek istediğiniz miktarı giriniz:"))
            if KrediFaturaOde>Bakiye:
                print("Yetersiz Bakiye")
            else:
                KrediFaturaSonMiktar=KrediKFatura-KrediFaturaOde
                if KrediFaturaSonMiktar<0:
                    BakiyeSon=Bakiye-KrediKFatura
                    SonFatura=0
                    degis=("UPDATE hesap_bilgisi SET Elek = ?")
                    im.execute(degis,[SonFatura])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı 0 TL dir")
                else:
                    BakiyeSon=Bakiye-KrediFaturaOde
                    im.execute(degis,[KrediFaturaSonMiktar])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı",KrediFaturaSonMiktar,"TL dir")
                return KrediKFatura
            break
        if soru=="e":
            print ("Kalan Bakiyeniz",BakiyeSon,"TL dir")
        else:
            break
def SuFatura(kimsin,soru):
    KHB=sqlite3.connect('KisiHesapBilgileri.db')
    im=KHB.cursor()
    tablo_yap=("CREATE TABLE IF NOT EXISTS hesap_bilgisi(AdSoyad,KartNo,Şifre,İban,Bakiye,SimBloke,KKFatura,Tlf,Elek,Su,gaz,trafik)")
    im.execute(tablo_yap)
    im.execute("""SELECT * FROM hesap_bilgisi""")
    veriler=im.fetchall()
    final_result=[list(i)for i in veriler]
    while True:
        if kimsin == 0:
            Cemal=final_result[0]
            Bakiye=Cemal[4]
            KrediKFatura=Cemal[9]
            im=KHB.cursor()
            tablo_yap=("CREATE TABLE IF NOT EXISTS hesap_bilgisi(AdSoyad,KartNo,Şifre,İban,Bakiye,SimBloke,KKFatura,Tlf,Elek,Su,gaz,trafik)")
            im.execute(tablo_yap)
            im.execute("""SELECT * FROM hesap_bilgisi""")
            print("Faturanız",KrediKFatura,"TL dir")
            degis=("UPDATE hesap_bilgisi SET SU =?")
            BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
            KrediFaturaOde=int(input("Lütfen ödemek istediğiniz miktarı giriniz:"))
            if KrediFaturaOde>Bakiye:
                print("Yetersiz Bakiye")
            else:
                KrediFaturaSonMiktar=KrediKFatura-KrediFaturaOde
                if KrediFaturaSonMiktar<0:
                    BakiyeSon=Bakiye-KrediKFatura
                    SonFatura=0
                    degis=("UPDATE hesap_bilgisi SET SU = ?")
                    im.execute(degis,[SonFatura])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı 0 TL dir")
                else:
                    BakiyeSon=Bakiye-KrediFaturaOde
                    im.execute(degis,[KrediFaturaSonMiktar])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı",KrediFaturaSonMiktar,"TL dir")
                return KrediKFatura
            break
        elif kimsin == 1:
            Cemal=final_result[1]
            Bakiye=Cemal[4]
            KrediKFatura=Cemal[9]
            im=KHB.cursor()
            tablo_yap=("CREATE TABLE IF NOT EXISTS hesap_bilgisi(AdSoyad,KartNo,Şifre,İban,Bakiye,SimBloke,KKFatura,Tlf,Elek,Su,gaz,trafik)")
            im.execute(tablo_yap)
            im.execute("""SELECT * FROM hesap_bilgisi""")
            print("Faturanız",KrediKFatura,"TL dir")
            degis=("UPDATE hesap_bilgisi SET SU =?")
            BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
            KrediFaturaOde=int(input("Lütfen ödemek istediğiniz miktarı giriniz:"))
            if KrediFaturaOde>Bakiye:
                print("Yetersiz Bakiye")
            else:
                KrediFaturaSonMiktar=KrediKFatura-KrediFaturaOde
                if KrediFaturaSonMiktar<0:
                    BakiyeSon=Bakiye-KrediKFatura
                    SonFatura=0
                    degis=("UPDATE hesap_bilgisi SET SU = ?")
                    im.execute(degis,[SonFatura])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı 0 TL dir")
                else:
                    BakiyeSon=Bakiye-KrediFaturaOde
                    im.execute(degis,[KrediFaturaSonMiktar])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı",KrediFaturaSonMiktar,"TL dir")
                return KrediKFatura
            break
        elif kimsin == 2:
            Cemal=final_result[2]
            Bakiye=Cemal[4]
            KrediKFatura=Cemal[9]
            im=KHB.cursor()
            tablo_yap=("CREATE TABLE IF NOT EXISTS hesap_bilgisi(AdSoyad,KartNo,Şifre,İban,Bakiye,SimBloke,KKFatura,Tlf,Elek,Su,gaz,trafik)")
            im.execute(tablo_yap)
            im.execute("""SELECT * FROM hesap_bilgisi""")
            print("Faturanız",KrediKFatura,"TL dir")
            degis=("UPDATE hesap_bilgisi SET SU =?")
            BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
            KrediFaturaOde=int(input("Lütfen ödemek istediğiniz miktarı giriniz:"))
            if KrediFaturaOde>Bakiye:
                print("Yetersiz Bakiye")
            else:
                KrediFaturaSonMiktar=KrediKFatura-KrediFaturaOde
                if KrediFaturaSonMiktar<0:
                    BakiyeSon=Bakiye-KrediKFatura
                    SonFatura=0
                    degis=("UPDATE hesap_bilgisi SET SU = ?")
                    im.execute(degis,[SonFatura])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı 0 TL dir")
                else:
                    BakiyeSon=Bakiye-KrediFaturaOde
                    im.execute(degis,[KrediFaturaSonMiktar])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı",KrediFaturaSonMiktar,"TL dir")
                return KrediKFatura
            break
        if soru=="e":
            print ("Kalan Bakiyeniz",BakiyeSon,"TL dir")
        else:
            break
def DogalgazFatura(kimsin,soru):
    KHB=sqlite3.connect('KisiHesapBilgileri.db')
    im=KHB.cursor()
    tablo_yap=("CREATE TABLE IF NOT EXISTS hesap_bilgisi(AdSoyad,KartNo,Şifre,İban,Bakiye,SimBloke,KKFatura,Tlf,Elek,Su,gaz,trafik)")
    im.execute(tablo_yap)
    im.execute("""SELECT * FROM hesap_bilgisi""")
    veriler=im.fetchall()
    final_result=[list(i)for i in veriler]
    while True:
        if kimsin == 0:
            Cemal=final_result[0]
            Bakiye=Cemal[4]
            KrediKFatura=Cemal[10]
            im=KHB.cursor()
            tablo_yap=("CREATE TABLE IF NOT EXISTS hesap_bilgisi(AdSoyad,KartNo,Şifre,İban,Bakiye,SimBloke,KKFatura,Tlf,Elek,Su,gaz,trafik)")
            im.execute(tablo_yap)
            im.execute("""SELECT * FROM hesap_bilgisi""")
            print("Faturanız",KrediKFatura,"TL dir")
            degis=("UPDATE hesap_bilgisi SET gaz =?")
            BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
            KrediFaturaOde=int(input("Lütfen ödemek istediğiniz miktarı giriniz:"))
            if KrediFaturaOde>Bakiye:
                print("Yetersiz Bakiye")
            else:
                KrediFaturaSonMiktar=KrediKFatura-KrediFaturaOde
                if KrediFaturaSonMiktar<0:
                    BakiyeSon=Bakiye-KrediKFatura
                    SonFatura=0
                    degis=("UPDATE hesap_bilgisi SET gaz = ?")
                    im.execute(degis,[SonFatura])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı 0 TL dir")
                else:
                    BakiyeSon=Bakiye-KrediFaturaOde
                    im.execute(degis,[KrediFaturaSonMiktar])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı",KrediFaturaSonMiktar,"TL dir")
                return KrediKFatura
            break
        elif kimsin == 1:
            Cemal=final_result[1]
            Bakiye=Cemal[4]
            KrediKFatura=Cemal[10]
            im=KHB.cursor()
            tablo_yap=("CREATE TABLE IF NOT EXISTS hesap_bilgisi(AdSoyad,KartNo,Şifre,İban,Bakiye,SimBloke,KKFatura,Tlf,Elek,Su,gaz,trafik)")
            im.execute(tablo_yap)
            im.execute("""SELECT * FROM hesap_bilgisi""")
            print("Faturanız",KrediKFatura,"TL dir")
            degis=("UPDATE hesap_bilgisi SET gaz =?")
            BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
            KrediFaturaOde=int(input("Lütfen ödemek istediğiniz miktarı giriniz:"))
            if KrediFaturaOde>Bakiye:
                print("Yetersiz Bakiye")
            else:
                KrediFaturaSonMiktar=KrediKFatura-KrediFaturaOde
                if KrediFaturaSonMiktar<0:
                    BakiyeSon=Bakiye-KrediKFatura
                    SonFatura=0
                    degis=("UPDATE hesap_bilgisi SET gaz = ?")
                    im.execute(degis,[SonFatura])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı 0 TL dir")
                else:
                    BakiyeSon=Bakiye-KrediFaturaOde
                    im.execute(degis,[KrediFaturaSonMiktar])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı",KrediFaturaSonMiktar,"TL dir")
                return KrediKFatura
            break
        elif kimsin == 2:
            Cemal=final_result[2]
            Bakiye=Cemal[4]
            KrediKFatura=Cemal[10]
            im=KHB.cursor()
            tablo_yap=("CREATE TABLE IF NOT EXISTS hesap_bilgisi(AdSoyad,KartNo,Şifre,İban,Bakiye,SimBloke,KKFatura,Tlf,Elek,Su,gaz,trafik)")
            im.execute(tablo_yap)
            im.execute("""SELECT * FROM hesap_bilgisi""")
            print("Faturanız",KrediKFatura,"TL dir")
            degis=("UPDATE hesap_bilgisi SET gaz =?")
            BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
            KrediFaturaOde=int(input("Lütfen ödemek istediğiniz miktarı giriniz:"))
            if KrediFaturaOde>Bakiye:
                print("Yetersiz Bakiye")
            else:
                KrediFaturaSonMiktar=KrediKFatura-KrediFaturaOde
                if KrediFaturaSonMiktar<0:
                    BakiyeSon=Bakiye-KrediKFatura
                    SonFatura=0
                    degis=("UPDATE hesap_bilgisi SET gaz = ?")
                    im.execute(degis,[SonFatura])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı 0 TL dir")
                else:
                    BakiyeSon=Bakiye-KrediFaturaOde
                    im.execute(degis,[KrediFaturaSonMiktar])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı",KrediFaturaSonMiktar,"TL dir")
                return KrediKFatura
            break
        if soru=="e":
            print ("Kalan Bakiyeniz",BakiyeSon,"TL dir")
        else:
            break
def TrafikFatura(kimsin,soru):
    KHB=sqlite3.connect('KisiHesapBilgileri.db')
    im=KHB.cursor()
    tablo_yap=("CREATE TABLE IF NOT EXISTS hesap_bilgisi(AdSoyad,KartNo,Şifre,İban,Bakiye,SimBloke,KKFatura,Tlf,Elek,Su,gaz,trafik)")
    im.execute(tablo_yap)
    im.execute("""SELECT * FROM hesap_bilgisi""")
    veriler=im.fetchall()
    final_result=[list(i)for i in veriler]
    while True:
        if kimsin == 0:
            Cemal=final_result[0]
            Bakiye=Cemal[4]
            KrediKFatura=Cemal[11]
            im=KHB.cursor()
            tablo_yap=("CREATE TABLE IF NOT EXISTS hesap_bilgisi(AdSoyad,KartNo,Şifre,İban,Bakiye,SimBloke,KKFatura,Tlf,Elek,Su,gaz,trafik)")
            im.execute(tablo_yap)
            im.execute("""SELECT * FROM hesap_bilgisi""")
            print("Faturanız",KrediKFatura,"TL dir")
            degis=("UPDATE hesap_bilgisi SET trafik =?")
            BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
            KrediFaturaOde=int(input("Lütfen ödemek istediğiniz miktarı giriniz:"))
            if KrediFaturaOde>Bakiye:
                print("Yetersiz Bakiye")
            else:
                KrediFaturaSonMiktar=KrediKFatura-KrediFaturaOde
                if KrediFaturaSonMiktar<0:
                    BakiyeSon=Bakiye-KrediKFatura
                    SonFatura=0
                    degis=("UPDATE hesap_bilgisi SET trafik = ?")
                    im.execute(degis,[SonFatura])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı 0 TL dir")
                else:
                    BakiyeSon=Bakiye-KrediFaturaOde
                    im.execute(degis,[KrediFaturaSonMiktar])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı",KrediFaturaSonMiktar,"TL dir")
                return KrediKFatura
            break
        elif kimsin == 1:
            Cemal=final_result[1]
            Bakiye=Cemal[4]
            KrediKFatura=Cemal[11]
            im=KHB.cursor()
            tablo_yap=("CREATE TABLE IF NOT EXISTS hesap_bilgisi(AdSoyad,KartNo,Şifre,İban,Bakiye,SimBloke,KKFatura,Tlf,Elek,Su,gaz,trafik)")
            im.execute(tablo_yap)
            im.execute("""SELECT * FROM hesap_bilgisi""")
            print("Faturanız",KrediKFatura,"TL dir")
            degis=("UPDATE hesap_bilgisi SET trafik =?")
            BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
            KrediFaturaOde=int(input("Lütfen ödemek istediğiniz miktarı giriniz:"))
            if KrediFaturaOde>Bakiye:
                print("Yetersiz Bakiye")
            else:
                KrediFaturaSonMiktar=KrediKFatura-KrediFaturaOde
                if KrediFaturaSonMiktar<0:
                    BakiyeSon=Bakiye-KrediKFatura
                    SonFatura=0
                    degis=("UPDATE hesap_bilgisi SET trafik = ?")
                    im.execute(degis,[SonFatura])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı 0 TL dir")
                else:
                    BakiyeSon=Bakiye-KrediFaturaOde
                    im.execute(degis,[KrediFaturaSonMiktar])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı",KrediFaturaSonMiktar,"TL dir")
                return KrediKFatura
            break
        elif kimsin == 2:
            Cemal=final_result[2]
            Bakiye=Cemal[4]
            KrediKFatura=Cemal[11]
            im=KHB.cursor()
            tablo_yap=("CREATE TABLE IF NOT EXISTS hesap_bilgisi(AdSoyad,KartNo,Şifre,İban,Bakiye,SimBloke,KKFatura,Tlf,Elek,Su,gaz,trafik)")
            im.execute(tablo_yap)
            im.execute("""SELECT * FROM hesap_bilgisi""")
            print("Faturanız",KrediFaturaSonMiktar,"TL dir")
            degis=("UPDATE hesap_bilgisi SET trafik =?")
            BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
            KrediFaturaOde=int(input("Lütfen ödemek istediğiniz miktarı giriniz:"))
            if KrediFaturaOde>Bakiye:
                print("Yetersiz Bakiye")
            else:
                KrediFaturaSonMiktar=KrediKFatura-KrediFaturaOde
                if KrediFaturaSonMiktar<0:
                    BakiyeSon=Bakiye-KrediKFatura
                    SonFatura=0
                    degis=("UPDATE hesap_bilgisi SET trafik = ?")
                    im.execute(degis,[SonFatura])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı 0 TL dir")
                else:
                    BakiyeSon=Bakiye-KrediFaturaOde
                    im.execute(degis,[KrediFaturaSonMiktar])
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    print("Faturanızda Kalan Borç Miktarı",KrediFaturaSonMiktar,"TL dir")
                return KrediKFatura
            break
        if soru=="e":
            print ("Kalan Bakiyeniz",BakiyeSon,"TL dir")
        else:
            break
def ParaYatırma(kimsin,soru):
    KHB=sqlite3.connect('KisiHesapBilgileri.db')
    im=KHB.cursor()
    tablo_yap=("CREATE TABLE IF NOT EXISTS hesap_bilgisi(AdSoyad,KartNo,Şifre,İban,Bakiye,SimBloke,KKFatura,Tlf,Elek,Su,gaz,trafik)")
    im.execute(tablo_yap)
    im.execute("""SELECT * FROM hesap_bilgisi""")
    veriler=im.fetchall()
    final_result=[list(i)for i in veriler]
    while True:
        if kimsin == 0:
            Cemal=final_result[0]
            Bakiye=Cemal[4]
            Parasecim=int(input("Yatırılacak Miktarı Giriniz:"))
            BakiyeSon=Bakiye+Parasecim
            BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
            im.execute(BakiyeDegis,[BakiyeSon])
            KHB.commit()
            KHB.close()
        elif kimsin == 1:
            Cemal=final_result[1]
            Bakiye=Cemal[4]
            Parasecim=int(input("Yatırılacak Miktarı Giriniz:"))
            BakiyeSon=Bakiye+Parasecim
            BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
            im.execute(BakiyeDegis,[BakiyeSon])
            KHB.commit()
            KHB.close()
        elif kimsin == 2:
            Cemal=final_result[2]
            Bakiye=Cemal[4]
            Parasecim=int(input("Yatırılacak Miktarı Giriniz:"))
            BakiyeSon=Bakiye+Parasecim
            BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
            im.execute(BakiyeDegis,[BakiyeSon])
            KHB.commit()
            KHB.close()
        break
    if soru=="e":
        print ("Kalan Bakiyeniz",BakiyeSon,"TL dir")
def ParaCekme(kimsin,soru):
    KHB=sqlite3.connect('KisiHesapBilgileri.db')
    im=KHB.cursor()
    tablo_yap=("CREATE TABLE IF NOT EXISTS hesap_bilgisi(AdSoyad,KartNo,Şifre,İban,Bakiye,SimBloke,KKFatura,Tlf,Elek,Su,gaz,trafik)")
    im.execute(tablo_yap)
    im.execute("""SELECT * FROM hesap_bilgisi""")
    veriler=im.fetchall()
    final_result=[list(i)for i in veriler]
    while True:
        if kimsin == 0:
            Cemal=final_result[0]
            Bakiye=Cemal[4]
            ParaYatırmaSecim=input("""[1]20TL           [2]300TL
[3]50TL           [4]400TL
[5]100TL          [6]500TL
[7]200TL          [8]Diğer\n""")
            if ParaYatırmaSecim == "1":
                BakiyeSon=Bakiye-20
                if BakiyeSon<0:
                    print("Yetersiz Bakiye")
                else:
                    BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    break
            elif ParaYatırmaSecim =="2":
                BakiyeSon=Bakiye-300
                if BakiyeSon<0:
                    print("Yetersiz Bakiye")
                else:
                    BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    break
            elif ParaYatırmaSecim =="3":
                BakiyeSon=Bakiye-50
                if BakiyeSon<0:
                    print("Yetersiz Bakiye")
                else:
                    BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    break
            elif ParaYatırmaSecim =="4":
                BakiyeSon=Bakiye-400
                if BakiyeSon<0:
                    print("Yetersiz Bakiye")
                else:
                    BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    break
            elif ParaYatırmaSecim =="5":
                BakiyeSon=Bakiye-100
                if BakiyeSon<0:
                    print("Yetersiz Bakiye")
                else:
                    BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    break
            elif ParaYatırmaSecim =="6":
                BakiyeSon=Bakiye-500
                if BakiyeSon<0:
                    print("Yetersiz Bakiye")
                else:
                    BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    break
            elif ParaYatırmaSecim =="7":
                BakiyeSon=Bakiye-200
                if BakiyeSon<0:
                    print("Yetersiz Bakiye")
                else:
                    BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    break
            elif ParaYatırmaSecim =="8":
                Parasecim=int(input("Lütfen Çekmek İstediğiniz Miktarı Giriniz:"))
                BakiyeSon=Bakiye-Parasecim
                if BakiyeSon<0:
                    print("Yetersiz Bakiye")
                else:
                    BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
            break
        elif kimsin == 1:
            Cemal=final_result[1]
            Bakiye=Cemal[4]
            ParaYatırmaSecim=input("""[1]20TL           [2]300TL
[3]50TL           [4]400TL
[5]100TL          [6]500TL
[7]200TL          [8]Diğer\n""")
            if ParaYatırmaSecim == "1":
                BakiyeSon=Bakiye-20
                if BakiyeSon<0:
                    print("Yetersiz Bakiye")
                else:
                    BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    break
            elif ParaYatırmaSecim =="2":
                BakiyeSon=Bakiye-300
                if BakiyeSon<0:
                    print("Yetersiz Bakiye")
                else:
                    BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    break
            elif ParaYatırmaSecim =="3":
                BakiyeSon=Bakiye-50
                if BakiyeSon<0:
                    print("Yetersiz Bakiye")
                else:
                    BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    break
            elif ParaYatırmaSecim =="4":
                BakiyeSon=Bakiye-400
                if BakiyeSon<0:
                    print("Yetersiz Bakiye")
                else:
                    BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    break
            elif ParaYatırmaSecim =="5":
                BakiyeSon=Bakiye-100
                if BakiyeSon<0:
                    print("Yetersiz Bakiye")
                else:
                    BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    break
            elif ParaYatırmaSecim =="6":
                BakiyeSon=Bakiye-500
                if BakiyeSon<0:
                    print("Yetersiz Bakiye")
                else:
                    BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    break
            elif ParaYatırmaSecim =="7":
                BakiyeSon=Bakiye-200
                if BakiyeSon<0:
                    print("Yetersiz Bakiye")
                else:
                    BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    break
            elif ParaYatırmaSecim =="8":
                Parasecim=int(input("Lütfen Çekmek İstediğiniz Miktarı Giriniz:"))
                BakiyeSon=Bakiye-Parasecim
                if BakiyeSon<0:
                    print("Yetersiz Bakiye")
                else:
                    BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
            break
        elif kimsin == 2:
            Cemal=final_result[2]
            Bakiye=Cemal[4]
            ParaYatırmaSecim=input("""[1]20TL           [2]300TL
[3]50TL           [4]400TL
[5]100TL          [6]500TL
[7]200TL          [8]Diğer\n""")
            if ParaYatırmaSecim == "1":
                BakiyeSon=Bakiye-20
                if BakiyeSon<0:
                    print("Yetersiz Bakiye")
                else:
                    BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    break
            elif ParaYatırmaSecim =="2":
                BakiyeSon=Bakiye-300
                if BakiyeSon<0:
                    print("Yetersiz Bakiye")
                else:
                    BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    break
            elif ParaYatırmaSecim =="3":
                BakiyeSon=Bakiye-50
                if BakiyeSon<0:
                    print("Yetersiz Bakiye")
                else:
                    BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    break
            elif ParaYatırmaSecim =="4":
                BakiyeSon=Bakiye-400
                if BakiyeSon<0:
                    print("Yetersiz Bakiye")
                else:
                    BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    break
            elif ParaYatırmaSecim =="5":
                BakiyeSon=Bakiye-100
                if BakiyeSon<0:
                    print("Yetersiz Bakiye")
                else:
                    BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    break
            elif ParaYatırmaSecim =="6":
                BakiyeSon=Bakiye-500
                if BakiyeSon<0:
                    print("Yetersiz Bakiye")
                else:
                    BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    break
            elif ParaYatırmaSecim =="7":
                BakiyeSon=Bakiye-200
                if BakiyeSon<0:
                    print("Yetersiz Bakiye")
                else:
                    BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
                    break
            elif ParaYatırmaSecim =="8":
                Parasecim=int(input("Lütfen Çekmek İstediğiniz Miktarı Giriniz:"))
                BakiyeSon=Bakiye-Parasecim
                if BakiyeSon<0:
                    print("Yetersiz Bakiye")
                else:
                    BakiyeDegis=("UPDATE hesap_bilgisi SET Bakiye =?")
                    im.execute(BakiyeDegis,[BakiyeSon])
                    KHB.commit()
                    KHB.close()
            break
    if soru=="e":
        print ("Kalan Bakiyeniz",BakiyeSon,"TL dir")
def BakiyeBilgi(kimsin):
    KHB=sqlite3.connect('KisiHesapBilgileri.db')
    im=KHB.cursor()
    tablo_yap=("CREATE TABLE IF NOT EXISTS hesap_bilgisi(AdSoyad,KartNo,Şifre,İban,Bakiye,SimBloke,KKFatura,Tlf,Elek,Su,gaz,trafik)")
    im.execute(tablo_yap)
    im.execute("""SELECT * FROM hesap_bilgisi""")
    veriler=im.fetchall()
    final_result=[list(i)for i in veriler]
    while True:
        if kimsin == 0:
            Cemal=final_result[0]
            Isım=Cemal[0]
            KartNo=Cemal[1]
            Bakiye=Cemal[4]
            print("Merhaba",Isım,"\n Kart Numaranız:",KartNo,"olup\n Bakiyeniz:",Bakiye,"TL dir")
            break
        elif kimsin == 1:
            Cemal=final_result[1]
            Isım=Cemal[0]
            KartNo=Cemal[1]
            Bakiye=Cemal[4]
            print("Merhaba",Isım,"\n Kart Numaranız:",KartNo,"olup\n Bakiyeniz:",Bakiye,"TL dir")
            break
        elif kimsin == 2:
            Cemal=final_result[2]
            Isım=Cemal[0]
            KartNo=Cemal[1]
            Bakiye=Cemal[4]
            print("Merhaba",Isım,"\n Kart Numaranız:",KartNo,"olup\n Bakiyeniz:",Bakiye,"TL dir")
            break
def IbanOgren(kimsin):
    KHB=sqlite3.connect('KisiHesapBilgileri.db')
    im=KHB.cursor()
    tablo_yap=("CREATE TABLE IF NOT EXISTS hesap_bilgisi(AdSoyad,KartNo,Şifre,İban,Bakiye,SimBloke,KKFatura,Tlf,Elek,Su,gaz,trafik)")
    im.execute(tablo_yap)
    im.execute("""SELECT * FROM hesap_bilgisi""")
    veriler=im.fetchall()
    final_result=[list(i)for i in veriler]
    if kimsin==0:
        Cemal=final_result[0]
        Iban=Cemal[3]
        print("İban No:",Iban)
    elif kimsin==1:
        Cemal=final_result[1]
        Iban=Cemal[3]
        print("İban No:",Iban)       
    elif kimsin==2:
        Cemal=final_result[2]
        Iban=Cemal[3]
        print("İban No:",Iban)
def SimKartıBloke(kimsin):
    KHB=sqlite3.connect('KisiHesapBilgileri.db')
    im=KHB.cursor()
    tablo_yap=("CREATE TABLE IF NOT EXISTS hesap_bilgisi(AdSoyad,KartNo,Şifre,İban,Bakiye,SimBloke,KKFatura,Tlf,Elek,Su,gaz,trafik)")
    im.execute(tablo_yap)
    im.execute("""SELECT * FROM hesap_bilgisi""")
    veriler=im.fetchall()
    final_result=[list(i)for i in veriler]
    if kimsin == 0:
        Cemal=final_result[0]
        Bloke=Cemal[5]
        if Bloke==0:
            print("Sim Blokeniz Yoktur")
        else:
            deger=0
            degis=("UPDATE hesap_bilgisi SET SimBloke = ?")
            im.execute(degis,[deger])
            print("Sim Kartınız Başarı ile Aktifleştirilmiştir")
            KHB.commit()
            KHB.close()
    elif kimsin == 1:
        Cemal=final_result[1]
        Bloke=Cemal[5]
        if Bloke==0:
            print("Sim Blokeniz Yoktur")
        else:
            deger=0
            degis=("UPDATE hesap_bilgisi SET SimBloke = ?")
            im.execute(degis,[deger])
            print("Sim Kartınız Başarı ile Aktifleştirilmiştir")
            KHB.commit()
            KHB.close()
    elif kimsin == 2:
        Cemal=final_result[2]
        Bloke=Cemal[5]
        if Bloke==0:
            print("Sim Blokeniz Yoktur")
        else:
            deger=0
            degis=("UPDATE hesap_bilgisi SET SimBloke = ?")
            im.execute(degis,[deger])
            print("Sim Kartınız Başarı ile Aktifleştirilmiştir")
            KHB.commit()
            KHB.close()