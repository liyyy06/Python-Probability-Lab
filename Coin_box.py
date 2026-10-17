# Sebuah kotak berisi koin emas dan koin perak. 
# Dua koin diambil secara acak, satu per satu, tanpa dikembalikan.
# Probabilitas bahwa kedua koin yang terambil adalah emas adalah 1/3.
# (a) Berapakah jumlah minimum koin yang mungkin ada di dalam kotak? 
# (b) Berapa banyak koin emas serta koin peraknya?

for total in range (3, 10):
    for gold in range (2, total):
        silver = total - gold

        if 3 * gold * (gold - 1) == total * (total - 1):
            print("Jumlah minimum koin di dalam kotak:", total)
            print("Gold:", gold)
            print("Silver:", silver)
