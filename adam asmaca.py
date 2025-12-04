import random
import json

# Adam asmaca çizimleri
GORSELLER = [
    """
     +---+
     |   |
         |
         |
         |
        ===
    """,
    """
     +---+
     |   |
     O   |
         |
         |
        ===
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
        ===
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
        ===
    """,
    """
     +---+
     |   |
     O   |
    /|\  |
         |
        ===
    """,
    """
     +---+
     |   |   
     O   |
    /|\  |
    /    |
        ===
    """,
    """
     +---+
     |   | 
     O   |
    /|\  |
    / \  |
        ===
    """
]

# Oyun için kelimeler daha sonradan eklenilebilir
KELIMELER = {
    "meyve": ["kiraz", "karpuz", "üzüm", "mandalina", "elma"],
    "hayvan": ["zebra", "yunus", "tavşan", "ayı", "zürafa"],
    "teknoloji": ["klavye", "yazıcı", "hoparlör", "televizyon", "mikrofon"]
}

MAKS_HATA = len(GORSELLER) - 1  # 6 yanlışta kaybediliyor


# Skorları kaydet - en iyi 5'i tutulacak
def skor_kaydet(isim, puan):
    """Skorları dosyaya yazıyoruz, eskileri kaybetmeyelim"""
    try:
        # Önceki skorları oku
        with open("skorlar.json", "r", encoding="utf-8") as f:
            veriler = json.load(f)
    except:
        veriler = []  # Dosya yoksa boş liste

    # Yeni skoru ekle
    veriler.append({"isim": isim, "puan": puan})

    # Puanına göre sırala ve ilk 5'i al
    veriler.sort(key=lambda x: x["puan"], reverse=True)
    veriler = veriler[:5]

    # Kaydet
    with open("skorlar.json", "w", encoding="utf-8") as f:
        json.dump(veriler, f, indent=4, ensure_ascii=False)


# En iyi skorları göster
def skor_goster():
    """Skor tablosunu gösterelim"""
    try:
        with open("skorlar.json", "r", encoding="utf-8") as f:
            veriler = json.load(f)

        print("\n--- EN İYİ 5 SKOR ---")
        for v in veriler:
            print(f"{v['isim']}: {v['puan']} puan")
        print("----------------------")
    except:
        print("Henüz kimse oynamamış, ilk skoru sen kaydedeceksin!")


# Matematik işlemi çözme - bonus harf kazanmak için
def islem_coz(kullanilanlar):
    """Matematik işlemi çöz, doğruysa bonus harf kazan"""
    print("\nHangi işlemi yapalım? (+ - * /)")
    tur = input("İşlem seç (çıkmak için 'iptal' yaz): ").strip()

    if tur == "iptal":
        print("İşlem iptal edildi.")
        return 0, None

    if tur not in ["+", "-", "*", "/"]:
        print("O işlem yok ki...")
        return 0, None

    if tur in kullanilanlar:
        print("Bu işlemi zaten yaptın, başka bir şey dene!")
        return 0, None

    try:
        # Sayıları alalım
        a = input("Birinci sayı: ")
        if a == "iptal":
            print("İşlem iptal edildi.")
            return 0, None

        b = input("İkinci sayı: ")
        if b == "iptal":
            print("İşlem iptal edildi.")
            return 0, None

        a = float(a)
        b = float(b)

        # Sıfıra bölme kontrolü
        if tur == "/" and b == 0:
            print("Sıfıra bölme yapamazsın! Bu hata sayılacak...")
            return -10, False

        # İşlemi hesapla
        sonuc = eval(f"{a} {tur} {b}")  # Kolay yol :)

        # Kullanıcının tahminini al
        tahmin = float(input("Senin cevabın: "))

        # İşlemi kullanıldı olarak işaretle
        kullanilanlar.add(tur)

        # Kontrol et
        if abs(tahmin - sonuc) < 0.000001:  # Küçük farkları görmezden gel
            print("✔️ Aferin! Doğru cevap!")
            return 15, True
        else:
            print(f"✖️ Yanlış... Doğru cevap: {sonuc}")
            return -10, False

    except ValueError:
        print("Sayı girmen lazım...")
        return 0, None
    except:
        print("Bir şeyler ters gitti, tekrar dene.")
        return 0, None


# Rastgele kelime seç
def kelime_al():
    """Rastgele bir kategori ve kelime seç"""
    kategori = random.choice(list(KELIMELER.keys()))
    kelime = random.choice(KELIMELER[kategori])
    return kategori, kelime


# Adam asmayı göster
def asmaca_goster(hata):
    """Adamın durumunu çiz"""
    print(GORSELLER[hata])


# Ana oyun fonksiyonu
def baslat():
    """Oyunu başlat - burası asıl işlerin dönüceği yer"""

    # Oyunu hazırla
    kategori, kelime = kelime_al()
    tahmin = ["_"] * len(kelime)  # Başlangıçta tüm harfler gizli
    harfler = set()  # Tüm denenen harfler
    yanlislar = set()  # Sadece yanlış harfler
    hata = 0  # Yanlış sayısı
    puan = 0  # Toplam puan
    bonus = 0  # Bonus hakları
    islemler = set()  # Kullanılan işlem türleri

    print("\n" + "=" * 40)
    print("             OYUN BAŞLIYOR!")
    print("=" * 40)
    print(f"{len(kelime)} harfli bir kelime seçildi, hadi bulalım!")

    # Oyun döngüsü
    while hata < MAKS_HATA and "_" in tahmin:
        # Mevcut durumu göster
        asmaca_goster(hata)
        print(f"\n📖 Kelime: {' '.join(tahmin)}")
        print(f"❌ Yanlış sayısı: {hata}/{MAKS_HATA}")
        print(f"⭐ Puan: {puan} | Bonus: {bonus}")

        if harfler:
            print(f"🔠 Denediğin harfler: {', '.join(sorted(harfler))}")

        # Menü
        print("\nNe yapmak istersin?")
        print("1) Harf tahmin et")
        print("2) Matematik sorusu çöz (bonus kazan)")
        print("3) İpucu al (1 bonus harcar)")
        print("4) Oyundan çık")

        secim = input("Seçimin (1-4): ").strip()

        if secim == "1":
            # Harf tahmini
            h = input("Tahmin ettiğin harfi yaz: ").lower().strip()

            if len(h) != 1 or not h.isalpha():
                print("Tek bir harf yazmalısın...")
                continue

            if h in harfler:
                print("Bu harfi zaten denedin!")
                continue

            harfler.add(h)

            if h in kelime:
                print("🎯 Doğru harf! Bravo!")
                # Doğru harfi kelimede aç
                for i, k in enumerate(kelime):
                    if k == h:
                        tahmin[i] = h
                puan += 10
            else:
                print("😕 Yanlış harf...")
                yanlislar.add(h)
                hata += 1
                puan -= 5

        elif secim == "2":
            # Matematik işlemi
            p, d = islem_coz(islemler)
            puan += p

            if d is True:
                bonus += 1
                # Rastgele bir kapalı harfi aç
                acilmamis = [i for i, h in enumerate(tahmin) if h == "_"]
                if acilmamis:
                    i = random.choice(acilmamis)
                    tahmin[i] = kelime[i]
                    harfler.add(kelime[i])
                    print(f"🎁 Bonus kazandın! '{kelime[i]}' harfi açıldı!")
                else:
                    print("Zaten tüm harfler açık!")

            elif d is False:
                hata += 1

        elif secim == "3":
            # İpucu al
            if bonus >= 1:
                print(f"💡 İpucu: Bu kelime '{kategori}' kategorisinde")
                bonus -= 1
            else:
                print("Bonus hakkın yok! Matematik çözüp bonus kazanmalısın.")

        elif secim == "4":
            print("Tamam, çıkıyorum...")
            break

        else:
            print("Geçersiz sayı, 1 ile 4 arası bir sayı yaz...")

    # Oyun sonu
    print("\n" + "=" * 50)

    if "_" not in tahmin:
        print(f"🎉 TEBRİKLER! Kelimeyi buldun: {kelime}")
        puan += 50
    elif hata >= MAKS_HATA:
        asmaca_goster(hata)
        print(f"💀 Maalesef kaybettin... Kelime: {kelime}")
        print("Üzülme, bir daha dene!")
        puan -= 20

    print(f"\n🏆 Toplam puanın: {puan}")

    # Skor kaydetme
    isim = input("Skor tablosu için adını yaz (boş bırakabilirsin): ").strip()
    if isim:
        skor_kaydet(isim, puan)
        print("Skorun kaydedildi!")

    # Skorları göster
    skor_goster()


# Program buradan başlıyor
if __name__ == "__main__":
    print("Adam Asmaca Oyununa Hoş Geldin!")
    baslat()