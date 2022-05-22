import sqlite3
def kacıncıHesap (kimsin):
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
            break
        elif kimsin == 1:
            Cemal=final_result[1]
            break
        elif kimsin == 2:
            Cemal=final_result[2]
            
            break
        else:
            print("Lütfen Seçili Kişilerden Birini Seçiniz")
            break