class Okul:
    def __init__(self, sinifSayisi, ogrenciSayisi, personelSayisi, okulduzeyi):
        self.sinifsayi = sinifSayisi
        self.ogrencisayi = ogrenciSayisi
        self.personelsayi = personelSayisi
        self.okulduzeyi = okulduzeyi


class Sinif(Okul):
    def __init__(self, ogrenciSayisi, dersSayisi, sinifOgretmeni):
        self.ogrencis = ogrenciSayisi
        self.derssayisi = dersSayisi
        self.sinifogretmeni = sinifOgretmeni



kartalImamhatip = Okul(16, 483, 47, "lise")
kartalImamhatip9A = Sinif(34, 12, "Yüksel DURMAZ")
kartalImamhatip10B = Sinif(32, 13, "İsmail BATMAZ")

izmirAtaturk = Okul(24, 501, 53, "ortaokul")
izmirAtaturk6C = Sinif(23, 9, "Abdullah KALIN")
izmirAtaturk7F = Sinif(21, 10, "Mustafa KORKMAZ")

istanbulBeykoz = Okul(30, 923, 53, "ilkokul")
istanbulBeykoz1A = Sinif(30, 7, "Fatma KURTULUŞ")
istanbulBeykoz3C = Sinif(31, 8, "Bilge DEMİRCİ")
