#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time

class DNDGame:
    def __init__(self):
        self.character_name = ""
        self.character_class = ""
        self.background = ""
        self.power = ""
        self.points = 0
        self.game_over = False
        self.victory = False
        
    def print_separator(self):
        print("\n" + "="*60 + "\n")
    
    def print_story(self, text):
        print(text)
        time.sleep(0.5)
    
    def add_points(self, amount, reason):
        """Menambah atau mengurangi poin"""
        self.points += amount
        if amount > 0:
            print(f"✓ {reason} | +{amount} poin (Total: {self.points} poin)")
        else:
            print(f"✗ {reason} | {amount} poin (Total: {self.points} poin)")
        time.sleep(0.3)
    
    def get_character_input(self):
        """Mengambil input tokoh dari pemain"""
        print("\n" + "="*60)
        print("SELAMAT DATANG DI DUNGEON & DRAGON: PETUALANGAN LEGENDA")
        print("="*60 + "\n")
        
        print("Mari kita ciptakan karakter Anda!\n")
        
        # Input nama tokoh
        self.character_name = input("Siapa nama tokoh Anda? ").strip()
        if not self.character_name:
            self.character_name = "Penjelajah Berani"
        
        # Input kelas karakter
        print("\nPilih kelas karakter Anda:")
        print("1. Prajurit (Warrior)")
        print("2. Penyihir (Mage)")
        print("3. Pemanah (Ranger)")
        print("4. Pencuri (Rogue)")
        
        class_choice = input("\nMasukkan pilihan (1-4): ").strip()
        classes = {
            "1": "Prajurit",
            "2": "Penyihir",
            "3": "Pemanah",
            "4": "Pencuri"
        }
        self.character_class = classes.get(class_choice, "Prajurit")
        
        # Input latar belakang
        print("\nPilih latar belakang tokoh Anda:")
        print("1. Dari Desa Kecil yang Damai")
        print("2. Dari Kerajaan yang Kaya")
        print("3. Dari Gua Gelap yang Misterius")
        print("4. Dari Pengasingan")
        
        background_choice = input("\nMasukkan pilihan (1-4): ").strip()
        backgrounds = {
            "1": "Desa Kecil yang Damai",
            "2": "Kerajaan yang Kaya",
            "3": "Gua Gelap yang Misterius",
            "4": "Pengasingan"
        }
        self.background = backgrounds.get(background_choice, "Desa Kecil yang Damai")
        
        # Input kekuatan/trait/magic
        print("\nPilih kekuatan/magic Anda:")
        print("1. Pedang Legendaris (Meningkatkan Serangan)")
        print("2. Mantra Penyembuhan (Bisa menyembuhkan diri)")
        print("3. Ketangkasan Tinggi (Bisa menghindari serangan)")
        print("4. Telepati (Bisa membaca pikiran musuh)")
        
        power_choice = input("\nMasukkan pilihan (1-4): ").strip()
        powers = {
            "1": "Pedang Legendaris",
            "2": "Mantra Penyembuhan",
            "3": "Ketangkasan Tinggi",
            "4": "Telepati"
        }
        self.power = powers.get(power_choice, "Pedang Legendaris")
        
        self.print_separator()
        print(f"Tokoh Anda: {self.character_name}")
        print(f"Kelas: {self.character_class}")
        print(f"Latar Belakang: {self.background}")
        print(f"Kekuatan: {self.power}")
        print(f"Poin Awal: {self.points}")
        self.print_separator()
    
    def get_yes_no_input(self, prompt):
        """Mengambil input yes/no dari pemain"""
        while True:
            choice = input(prompt).strip().lower()
            if choice in ['y', 'ya', 'yes', '1']:
                return True
            elif choice in ['n', 'tidak', 'no', '0']:
                return False
            else:
                print("Masukkan 'ya'/'y' atau 'tidak'/'n': ")
    
    def game_over(self, message, points_penalty=0):
        """Mengakhiri permainan dengan pesan"""
        if points_penalty != 0:
            self.add_points(points_penalty, message)
        self.print_separator()
        print("⚠️  GAME OVER ⚠️")
        self.print_separator()
        self.game_over = True
    
    def victory(self, message):
        """Kemenangan!"""
        self.print_separator()
        print("🎉 KEMENANGAN! 🎉")
        print(message)
        self.print_separator()
        self.victory = True
    
    def start_story(self):
        """Memulai cerita utama"""
        self.print_separator()
        self.print_story(f"Kisah dimulai...\n")
        
        self.print_story(f"{self.character_name}, seorang {self.character_class} dari {self.background}.")
        self.print_story(f"Anda memiliki kemampuan istimewa: {self.power}.\n")
        
        self.print_story("Suatu hari, Anda berjalan melewati hutan belantara.")
        self.print_story("Tiba-tiba, Anda mendengar suara tangisan yang menyedihkan...")
        
        self.print_separator()
        
        if self.get_yes_no_input("Apakah Anda akan membantu? (ya/tidak): "):
            self.add_points(3, "Memilih untuk membantu korban")
            self.story_help_victim()
        else:
            self.print_story("Anda memutuskan untuk terus berjalan...")
            self.story_ignore_victim()
    
    def story_help_victim(self):
        """Alur cerita: membantu korban"""
        self.print_separator()
        self.print_story("Anda menemukan seorang gadis muda yang terjebak dalam jaringan laba-laba raksasa!")
        self.print_story("Laba-laba berukuran besar keluar dari kegelapan dengan kedua mata berkilau merah.")
        
        self.print_separator()
        
        if self.power == "Pedang Legendaris":
            self.print_story("Berkat Pedang Legendaris Anda, Anda berhasil mengusir laba-laba tersebut!")
            self.add_points(10, "Membunuh laba-laba raksasa")
            self.story_save_girl()
        elif self.power == "Mantra Penyembuhan":
            self.print_story("Anda menggunakan Mantra Penyembuhan untuk melindungi gadis itu...")
            if self.get_yes_no_input("Bertarung langsung dengan laba-laba? (ya/tidak): "):
                self.add_points(-3, "Terluka dalam pertarungan")
                self.game_over("Laba-laba raksasa memukul Anda dengan tajam! Anda kalah...", -10)
            else:
                self.print_story("Anda dan gadis itu berhasil meloloskan diri!")
                self.add_points(5, "Menyelamatkan gadis dari laba-laba")
                self.story_save_girl()
        elif self.power == "Ketangkasan Tinggi":
            self.print_story("Dengan Ketangkasan Tinggi Anda, Anda dengan mudah menghindari serangan laba-laba!")
            self.print_story("Anda membebaskan gadis itu dari jaring pengganggu.")
            self.add_points(5, "Menyelamatkan gadis dengan kelincahan")
            self.story_save_girl()
        elif self.power == "Telepati":
            self.print_story("Menggunakan kemampuan Telepati, Anda membaca pikiran laba-laba...")
            self.print_story("Ternyata laba-laba itu sedang kelaparan dan hanya mencari makanan.")
            if self.get_yes_no_input("Menawarkan damai kepada laba-laba? (ya/tidak): "):
                self.print_story("Laba-laba itu menerima persembahan makanan Anda dan meninggalkan gadis itu!")
                self.add_points(3, "Membantu laba-laba dengan cara damai")
                self.story_save_girl()
            else:
                self.print_story("Anda mengecek jaringan untuk menemukan musuh lain di sana...")
                self.story_secret_dungeon()
    
    def story_ignore_victim(self):
        """Alur cerita: mengabaikan korban"""
        self.print_separator()
        self.print_story("Tiba-tiba, tanah di bawah kaki Anda amblas!")
        self.print_story("Anda jatuh ke dalam lubang gelap yang dalam...")
        
        self.print_separator()
        
        if self.get_yes_no_input("Apakah Anda akan mencoba memanjat keluar? (ya/tidak): "):
            if self.power == "Ketangkasan Tinggi" or self.power == "Pedang Legendaris":
                self.print_story("Dengan kemampuan Anda, berhasil memanjat keluar dari lubang!")
                self.story_treasure_found()
            else:
                self.add_points(-10, "Jatuh ke lubang dan terbunuh")
                self.game_over("Lubang terlalu dalam dan licin. Anda tidak bisa keluar dan mati di sana...")
        else:
            self.print_story("Anda menunggu di dalam lubang gelap...")
            self.print_story("Sebuah cahaya muncul! Seorang pedagang melihat Anda dan menolongnya!")
            self.add_points(3, "Ditolong oleh pedagang")
            self.story_meet_merchant()
    
    def story_save_girl(self):
        """Alur cerita: setelah menyelamatkan gadis"""
        self.print_separator()
        self.print_story("Gadis itu sangat berterima kasih!")
        self.print_story("Dia bernama Elara, seorang penyihir muda dari kerajaan.")
        self.print_story("Elara menawarkan untuk bergabung dengan Anda dalam petualangan lebih lanjut.")
        
        self.print_separator()
        
        if self.get_yes_no_input("Apakah Anda akan menerimanya? (ya/tidak): "):
            self.add_points(3, "Menerima misi dari Elara")
            self.print_story("Elara memberitahu Anda tentang kastil gelap di gunung yang dipimpin oleh seorang penyihir jahat.")
            self.print_story("Dia meminta bantuan Anda untuk mengalahkan penyihir itu dan membebaskan kerajaannya.")
            if self.get_yes_no_input("Apakah Anda setuju untuk membantu? (ya/tidak): "):
                self.add_points(3, "Berkomitmen membantu Elara")
                self.story_final_battle()
            else:
                self.add_points(5, "Menyelamatkan gadis tanpa meneruskan misi")
                self.victory("Anda memilih untuk beristirahat di desa aman. Hidup Anda sejahtera dengan Elara!")
        else:
            self.print_story("Elara pergi sendirian. Anda melanjutkan petualangan Anda...")
            self.story_treasure_found()
    
    def story_secret_dungeon(self):
        """Alur cerita: menemukan dungeon rahasia"""
        self.print_separator()
        self.print_story("Di balik jaringan, Anda menemukan sebuah gua gelap...")
        self.print_story("Di dalamnya terdapat harta karun legendaris yang bersinar!")
        
        self.print_separator()
        
        if self.get_yes_no_input("Apakah Anda akan mengambil harta karun itu? (ya/tidak): "):
            self.print_story("Saat Anda menyentuh harta karun, sebuah kutukan muncul!")
            self.print_story("Makhluk bersayap hitam terbang keluar dari bayangan...")
            self.add_points(-10, "Dikutuk dan terbunuh oleh makhluk gelap")
            self.game_over("Makhluk tersebut sangat kuat. Anda tidak bisa mengalahkannya...")
        else:
            self.print_story("Anda berhati-hati dan tidak menyentuh harta karun.")
            self.print_story("Anda meninggalkan gua dengan selamat dan kembali ke dunia di atas.")
            self.victory("Anda selamat dengan pengetahuan tentang harta karun! Petualangan Anda berakhir dengan aman.")
    
    def story_treasure_found(self):
        """Alur cerita: menemukan harta karun"""
        self.print_separator()
        self.print_story("Setelah berjalan jauh, Anda menemukan goa harta karun yang terkenal!")
        self.print_story("Di dalam goa, terdapat peti beremas merah yang gemilang...")
        
        self.print_separator()
        
        if self.get_yes_no_input("Apakah Anda akan membuka peti itu? (ya/tidak): "):
            self.print_story("Peti terbuka... dan emas berlimpah ruah!")
            self.add_points(10, "Menemukan harta karun")
            self.victory("Anda kaya raya dan menjadi petualang legendaris! Hidup Anda berubah selamanya!")
        else:
            self.print_story("Anda curiga dengan peti itu. Dengan hati-hati Anda tinggalkan goa.")
            self.victory("Keberuntungan ada di pihak Anda! Anda kembali ke desa dengan sehat walafiat.")
    
    def story_meet_merchant(self):
        """Alur cerita: bertemu pedagang"""
        self.print_separator()
        self.print_story("Pedagang itu memberitahu Anda tentang sebuah perjalanan berbahaya ke kastil hitam.")
        self.print_story("Dia menawarkan uang jika Anda mau membantu mengeluarkan barang bawaannya dari sana.")
        
        self.print_separator()
        
        if self.get_yes_no_input("Apakah Anda akan membantu pedagang itu? (ya/tidak): "):
            self.add_points(3, "Menerima bantuan dari pedagang")
            self.story_final_battle()
        else:
            self.add_points(3, "Selamat dari bahaya")
            self.victory("Anda memilih jalan yang aman dan hidup nyaman di desa kecil.")
    
    def story_final_battle(self):
        """Alur cerita: pertempuran akhir"""
        self.print_separator()
        self.print_story("Anda tiba di kastil hitam yang misterius...")
        self.print_story("Sebuah naga hitam dengan mata merah berkobar keluar dari gelapnya!")
        self.print_story("Inilah musuh terakhir Anda!")
        
        self.print_separator()
        
        if self.power == "Pedang Legendaris":
            self.print_story("Pedang Legendaris Anda bersinar dengan cahaya emas!")
            if self.get_yes_no_input("Menyerang naga secara frontal? (ya/tidak): "):
                self.add_points(10, "Membunuh naga dengan Pedang Legendaris")
                self.victory("Dengan sekali sabitan, Anda mengalahkan naga! Anda adalah pahlawan sejati!")
            else:
                self.add_points(-3, "Terluka akibat keraguan")
                self.game_over("Anda ragu-ragu terlalu lama. Naga menyerangmu dengan api yang membara...", -10)
        elif self.power == "Mantra Penyembuhan":
            self.print_story("Anda menggunakan Mantra Penyembuhan untuk melindungi diri...")
            if self.get_yes_no_input("Mencari kelemahan naga? (ya/tidak): "):
                self.print_story("Anda menemukan bahwa naga takut pada cahaya. Anda menciptakan cahaya terang!")
                self.add_points(10, "Mengusir naga dengan strategi cerdas")
                self.victory("Naga lari ketakutan! Anda menang tanpa perlu pertarungan berat!")
            else:
                self.add_points(-3, "Terluka oleh naga")
                self.game_over("Naga menemukan Anda dan menyerang dengan ganas...", -10)
        elif self.power == "Ketangkasan Tinggi":
            self.print_story("Dengan Ketangkasan Tinggi, Anda bisa menghindari setiap serangan naga!")
            if self.get_yes_no_input("Mencari cara untuk menghentikan naga? (ya/tidak): "):
                self.print_story("Anda menemukan kristal ajaib yang bisa menyegelnya!")
                self.add_points(10, "Menyegel naga dengan kristal ajaib")
                self.victory("Anda berhasil menyegel naga dengan kristal ajaib! Tanah dibebaskan dari teror!")
            else:
                self.add_points(-3, "Terjebak dalam api naga")
                self.game_over("Naga menciptakan jebakan api di mana-mana. Anda terperangah dalam api...", -10)
        elif self.power == "Telepati":
            self.print_story("Anda membaca pikiran naga yang gelap dan penuh kebencian...")
            if self.get_yes_no_input("Apakah Anda akan mencoba menebus naga itu? (ya/tidak): "):
                self.print_story("Dengan Telepati kuat, Anda berhasil mencapai bagian kemanusiaan dalam hati naga!")
                self.print_story("Naga berubah kembali menjadi manusia! Anda telah membebaskannya dari kutukan!")
                self.add_points(10, "Membebaskan naga dari kutukan")
                self.victory("Naga yang telah manusia mengucapkan terima kasih. Anda adalah pembebas yang sejati!")
            else:
                self.add_points(-3, "Diserang oleh naga")
                self.game_over("Naga membaca pikiran Anda juga dan menyerang dengan kekuatan penuh...", -10)
    
    def show_final_score(self):
        """Menampilkan skor akhir dan reward"""
        self.print_separator()
        print(f"POIN AKHIR: {self.points}")
        self.print_separator()
        
        if self.points > 50:
            print("🏆 SELAMAT! 🏆")
            print("Anda berhak atas 500 gulden emas ini!")
            print("Anda telah menunjukkan keberanian dan kebijaksanaan dalam perjalanan ini.")
        else:
            print("😌 PERJALANAN BERLANJUT 😌")
            print("Perjalanan masih panjang kawan, mungkin di kehidupan selanjutnya")
            print("kaulah pemenangnya...")
        
        self.print_separator()
    
    def play(self):
        """Menjalankan permainan"""
        self.get_character_input()
        self.start_story()
        self.show_final_score()
        
        self.print_separator()
        print("Terima kasih telah memainkan Dungeon & Dragon: Petualangan Legenda!")
        print("="*60 + "\n")


def main():
    while True:
        game = DNDGame()
        game.play()
        
        again = input("Apakah Anda ingin bermain lagi? (ya/tidak): ").strip().lower()
        if again not in ['y', 'ya', 'yes', '1']:
            print("\nTerima kasih telah bermain! Sampai jumpa lagi!\n")
            break


if __name__ == "__main__":
    main()
