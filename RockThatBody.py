import sys
import time

def printLyrics():
    lirik = [
        ("Karena semua yang kau cinta akan pergi", 0.06),
        ("Maka tunjukkan cintamu sebelum terlambat", 0.06),
        ("Kita selalu pikir kita punya waktu", 0.06),
        ("Lalu kita pilih untuk nanti dulu", 0.06),
        ("Tapi semua yang kau cinta akan pergi", 0.06),
        ("Maka tunjukkan cintamu sebelum terlambat", 0.06),
        ("Kita selalu pikir kita punya waktu", 0.06),
        ("Lalu kita pilih untuk nanti dulu", 0.06),
    ]

    delay = [0.3, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5,]
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu:
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])
        print('')
    print("//code-by-vall?")
printLyrics()