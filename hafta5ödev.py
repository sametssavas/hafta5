t1 = '01.01.2005'
t2 = '30.12.2010'

tarih1 = t1.split('.')
tarih2 = t2.split('.')

yıl1 = int(tarih1[-1])
yıl2 = int(tarih2[-1])
ay1 = int(tarih1[-2])
ay2 = int(tarih2[-2])
gun1 = int(tarih1[-3])
gun2 = int(tarih2[-3])

print("Başlangıç tarihi:", yıl1, ay1, gun1)
print("Bitiş tarihi:", yıl2, ay2, gun2)

kategoriler = ['saglik', 'dunya', 'teknoloji']
gazeteler = ['sabah', 'hurriyet', 'milliyet']

ay_gunleri = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def artik_yil(yil):
    return (yil % 4 == 0 and yil % 100 != 0) or (yil % 400 == 0)

with open("haber_linkleri.txt", "w") as f:
    for gazete in gazeteler:
        gaste_url = f"https://www.{gazete}.com.tr"

        for kategori in kategoriler:
            for yil in range(yıl1, yıl2 + 1):
                for ay in range(1, 13):
                    if ay == 2 and artik_yil(yil):
                        max_gun = 29
                    else:
                        max_gun = ay_gunleri[ay - 1]

                    for gun in range(1, max_gun + 1):
                        tarih = f"{yil}-{ay:02}-{gun:02}"
                        url = f"{gaste_url}/{kategori}/{tarih}"
                        print(url)
                        f.write(url + "\n")

print("Tüm URL'ler haber_linkleri.txt dosyasına kaydedildi.")
