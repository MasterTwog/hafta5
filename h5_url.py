def url_olustur(gazete,kategori,yil,ay,gun):
    site=f"www.{gazete}.com.tr"
    return f"{site}/{kategori}/{yil}-{ay}-{gun}"

t11='01.01.2005'
t12='30.12.2010'

tarih1=t11.split('.')
tarih2=t12.split('.')

yıl1=int(tarih1[-1])
yıl2=int(tarih2[-1])+ 1
ay1=int(tarih1[-2])
ay2=int(tarih2[-2])
gun1=int(tarih1[-3])
gun2=int(tarih2[-3])

kategori=['saglık','dunya','bilim','teknoloji']
gazeteler=['Sabah','Hurriyet','Sozcu']

for m in gazeteler:
    for k in kategori:
        for i in range(yıl1,yıl2):
            for j in range(1,13):
                for gun in range(1,32):
                    ay_str=f"{j:02d}"
                    gun_str=f"{gun:02d}"
                    url=url_olustur(m,k,i,ay_str,gun_str)
                    print(url)