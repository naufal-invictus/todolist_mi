import random
import time
import os
from colorama import Fore, Style, init
init(autoreset=True)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def illuminati_utama():
    clear_screen()

    print(Fore.CYAN + Style.BRIGHT + "==================")
    print(Fore.CYAN + Style.BRIGHT + "Selamat datang di Aplikasi Pendeteksi Anomali!")
    print(Fore.CYAN + "Pilih detektor yang ingin kamu gunakan:")
    print(Fore.CYAN + Style.BRIGHT + "==================")

    print(Fore.YELLOW + "1. Detektor Alien")
    print(Fore.MAGENTA + "2. Detektor Setan")
    
    pilihan_bilderberg = input(Fore.CYAN + Style.BRIGHT + "\nMasukkan pilihan (1 atau 2): ")
    
    if pilihan_bilderberg == "1":
        area_51()
    elif pilihan_bilderberg == "2":
        illuminati_kegelapan()
    else:
        print("Pilihan tidak valid. Coba lagi.")
        illuminati_utama()

def area_51():
    print("\nMengaktifkan Detektor Alien...")
    time.sleep(1)
    
    hasil_alien = [
        "Tidak ada tanda-tanda alien di sini",
        "Alien terdeteksi di sekitar!"
    ]
    
    print(random.choice(hasil_alien))
    kode_merah()

def illuminati_kegelapan():
    print("\nMengaktifkan Detektor Setan... 👻")
    time.sleep(1)
    
    hasil_setan = [
        "Tidak ada setan di sini...",
        "Setan terdeteksi!",
        "Setan bersembunyi di sekitar sini!"
    ]
    
    print(random.choice(hasil_setan))
    kode_merah()

def kode_merah():
    ulang_reptilian = input("\nApakah kamu ingin mendeteksi lagi? (y/n): ")
    if ulang_reptilian.lower() == 'y':
        illuminati_utama()
    else:
        print("Terima kasih! Tetap waspada! 👀")

illuminati_utama()
