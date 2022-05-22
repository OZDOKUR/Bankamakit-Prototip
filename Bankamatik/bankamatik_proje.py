import kisibilgi
import HesapGiris
Hosgeldiniz=int(input("""Hoşgeldiz Hangi Hesaptan İşlem Yapmak İstersiniz
[1]Yasemin Dönmez(9262)               [2]Baran Yılmaz(9390)
[3]Çağla Teke(2990)\n"""))
kimsin=Hosgeldiniz-1
HesapGiris.kacıncıHesap(kimsin)
if kimsin == 0 or kimsin == 1 or kimsin == 2:
    for i in range (3):
        sifre=input("Lütfen şifrenizi giriniz\n")
        if kimsin==0 and sifre=='9262' or kimsin==1 and sifre=='9390' or kimsin==2 and sifre=='2990':
            giriş="Başarılı"
            soru=input("Makbuz ister misiniz? (e/h)")
            break
        else:
            print("Şifre Hatalı Lütfen Tekrar Deneyiniz")
            giriş="Başarısız"
    while giriş=="Başarılı": 
        secim=input("""[1]Para Çekme                               [2]Para Yatırma
    [3]Ödeme İşlemleri                          [4]Kredi Kartı Borç Ödeme
    [5]Bakiye-Bilgi Şifre                       [6]Kart İade\n""")
        if secim =="1":
            kisibilgi.ParaCekme(kimsin,soru)
            devam=input("Başka işlem yapmak ister misiniz(e/h):")
            if devam == "e":
                continue
            elif devam =="h":
                break
        elif secim =="2":
            kisibilgi.ParaYatırma(kimsin,soru)
            devam=input("Başka işlem yapmak ister misiniz(e/h):")
            if devam == "e":
                continue
            elif devam =="h":
                break
        elif secim == "3":
            odeme_islemleri_secim=input("""[1]Fatura Ödemeleri                  [2]Trafik Cezası Ödemesi
    [3]Ana Menü\n""")

            if odeme_islemleri_secim == '1':
                FaturaOdemeSecim=input("""[1]Telefon faturası                   [2]Elektrik faturası
    [3]Su faturası                        [4]Doğalgaz faturası
    [5]Ana menü\n""")
                if FaturaOdemeSecim == '1':
                    kisibilgi.TelefonFatura(kimsin,soru)
                    devam=input("Başka işlem yapmak ister misiniz(e/h):")
                    if devam == "e":
                        continue
                    elif devam =="h":
                        break
                elif FaturaOdemeSecim == '2':
                    kisibilgi.ElektrikFatura(kimsin,soru)
                    devam=input("Başka işlem yapmak ister misiniz(e/h):")
                    if devam == "e":
                        continue
                    elif devam =="h":
                        break
                elif FaturaOdemeSecim == '3':
                    kisibilgi.SuFatura(kimsin,soru)
                    devam=input("Başka işlem yapmak ister misiniz(e/h):")
                    if devam == "e":
                        continue
                    elif devam =="h":
                        break
                elif FaturaOdemeSecim == '4':
                    kisibilgi.DogalgazFatura(kimsin,soru)
                    devam=input("Başka işlem yapmak ister misiniz(e/h):")
                    if devam == "e":
                        continue
                    elif devam =="h":
                        break
            elif odeme_islemleri_secim == '2':
                input("Lütfen Plakayı Giriniz:")
                kisibilgi.TrafikFatura(kimsin,soru)
                devam=input("Başka işlem yapmak ister misiniz(e/h):")
                if devam == "e":
                    continue
                elif devam =="h":
                    break
        elif secim == "4":
            kisibilgi.KrediKartıBorçBilgi(kimsin,soru)
            devam=input("Başka işlem yapmak ister misiniz(e/h):")
            if devam == "e":
                continue
            elif devam =="h":
                break
        elif secim == "5":
            bakiye_sifre_islemleri_secim=input("""[1]Bakiye Bilgileri                [2]IBAN Sorgulama              
    [3]Sim Kart Bloke Kaldırma         [4]Kart İade\n""")
            if bakiye_sifre_islemleri_secim =="1":
                kisibilgi.BakiyeBilgi(kimsin)
                Islemsoru=input("Başka bir işlem yapmak ister misiniz?(e/h):")
                if Islemsoru=="e":
                    continue
                else:
                    break
            elif bakiye_sifre_islemleri_secim =="2":
                kisibilgi.IbanOgren(kimsin)
                Islemsoru=input("Başka bir işlem yapmak ister misiniz?(e/h):")
                if Islemsoru=="e":
                    continue
                else:
                    break
            elif bakiye_sifre_islemleri_secim =="3":
                kisibilgi.SimKartıBloke(kimsin)
                Islemsoru=input("Başka bir işlem yapmak ister misiniz?(e/h):")
                if Islemsoru=="e":
                    continue
                else:
                    break
            elif bakiye_sifre_islemleri_secim =="4":
                break
        elif secim == "6":
            break
