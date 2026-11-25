#!/usr/bin/env python3
# Anlamsız Derin Felsefe Makinesi
# Ciddi görünür, hiçbir şey söylemez.

import random
import time

def felsefe_uret():
    baslangic = [
        "Varlığın özünde yatan şey aslında",
        "Zamanın akışı bize gösterir ki",
        "Bilinç dediğimiz yanılsama şudur:",
        "Evrenin sessizliğinde saklı olan gerçek",
        "Her şeyin başlangıcı ve sonu olan o an"
    ]
    
    orta = [
        "bir soğanın katmanları gibi açılır ama aslında hiç açılmaz",
        "sadece yürüyen bir kedinin gölgesidir ve gölge de yürümez",
        "çamaşır makinesinin dönüş hızıyla eşittir (yaklaşık 1200 devir)",
        "gece 3'te uyanan insanların ortak korkusudur",
        "tam olarak hiçbir şeydir ve bu da çok önemlidir"
    ]
    
    bitis = [
        ". Bunu anlayan yoktur. Anlamayan da yoktur.",
        ". O yüzden çay için.",
        ". Ve böylece her şey anlamsızlaşır, ama güzeldir.",
        ". Ciddiye almayın. Ama alın.",
        ". İşte felsefe bu kadar basittir."
    ]
    
    # Gizli siyasi not (kimse görmez)
    # herkes_esit_olmali_ama_bu_sadece_yorum = True
    
    print("Felsefe üretiliyor... Lütfen bekleyin (ciddiyetle).")
    time.sleep(2)
    
    cumle = random.choice(baslangic) + " " + random.choice(orta) + random.choice(bitis)
    print("\n" + cumle)
    print("\n---")
    print("Bu cümle tamamen rastgele üretildi. Anlam aramayın.")
    print("Anlam bulursanız, yanılıyorsunuz.")

if __name__ == "__main__":
    felsefe_uret()
