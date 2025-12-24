class Kitap:
    """Kitap bilgilerini tutan sınıf"""
    def __init__(self, isim, yazar, yil):
        self.name = isim
        self.author = yazar
        self.year = yil

    def __str__(self):
        return f"Kitap Adı: {self.name}, Yazar: {self.author}, Yayın Yılı: {self.year}"


class Library:
    """Kütüphane işlemlerini yöneten sınıf"""
    def __init__(self):
        self.books = []

    def add_book(self, yeni_kitap):
        self.books.append(yeni_kitap)
        print(f"\n>>> {yeni_kitap.name} başarıyla eklendi.")

    def remove_book(self, silinecek_ad):
        for kitap in self.books:
            if kitap.name.lower() == silinecek_ad.lower():
                self.books.remove(kitap)
                print(f"\n>>> {silinecek_ad} başarıyla silindi.")
                return
        print("\n>>> Kitap bulunamadı, silme işlemi başarısız.")

    def search_by_name(self, aranan_ad):
        print("\n--- Arama Sonuçları ---")
        bulundu = False
        for kitap in self.books:
            if aranan_ad.lower() in kitap.name.lower():
                print(kitap)
                bulundu = True
        if not bulundu:
            print("Eşleşen kitap bulunamadı.")

    def search_by_author(self, aranan_yazar):
        print("\n--- Arama Sonuçları ---")
        bulundu = False
        for kitap in self.books:
            if aranan_yazar.lower() in kitap.author.lower():
                print(kitap)
                bulundu = True
        if not bulundu:
            print("Bu yazara ait kitap bulunamadı.")

    def list_books(self):
        if not self.books:
            print("\nKütüphane şu an boş.")
        else:
            print("\n--- Kütüphanedeki Tüm Kitaplar ---")
            for kitap in self.books:
                print(kitap)


def main():
    kutuphane = Library()

    while True:
        print("\nKütüphane Kitap Arama Sistemi")
        print("1. Kitap Ekle")
        print("2. Kitap Sil")
        print("3. Kitap Ara (İsme Göre)")
        print("4. Kitap Ara (Yazara Göre)")
        print("5. Tüm Kitapları Listele")
        print("6. Çıkış")

        secim = input("\nSeçiminizi yapın (1-6): ")

        if secim == '1':
            ad = input("Kitap Adı: ")
            yazar = input("Yazar: ")
            yil = input("Yayın Yılı: ")
            yeni_kitap = Kitap(ad, yazar, yil)
            kutuphane.add_book(yeni_kitap)

        elif secim == '2':
            silinecek = input("Silmek istediğiniz kitabın adını girin: ")
            kutuphane.remove_book(silinecek)

        elif secim == '3':
            aranan = input("Aramak istediğiniz kitabın adını girin: ")
            kutuphane.search_by_name(aranan)

        elif secim == '4':
            yazar_adi = input("Yazar adını girin: ")
            kutuphane.search_by_author(yazar_adi)

        elif secim == '5':
            kutuphane.list_books()

        elif secim == '6':
            print("Uygulamadan çıkılıyor...")
            break

        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")


if __name__ == "__main__":
    main()
