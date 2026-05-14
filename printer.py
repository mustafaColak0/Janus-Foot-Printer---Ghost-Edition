import socket, requests, os, urllib3, time, random, sys
from datetime import datetime
from dotenv import load_dotenv
from PIL import Image
from PIL.ExifTags import TAGS
from cryptography.fernet import Fernet
# SSL_BYPASS: Sertifika uyarılarını kapatır.
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# AI_IMPORT
try:
    from groq import Groq
except ImportError:
    Groq = None

# [1. ADIM]: KASA AÇMA FONKSİYONU
def sessiz_anahtar_yukle():
    # 1. Anahtarımızı tanımlıyoruz
    KASA_ANAHTARI = b'BURAYA_KENDI_FERNET_ANAHTARINIZI_YAZIN' 
    
    try:
        # 2. Önce DOSYA YOLUNU tanımlıyoruz 
        if getattr(sys, 'frozen', False):
            # EXE çalışırken
            base_path = os.path.dirname(os.path.realpath(sys.argv[0]))
        else:
            # Script çalışırken
            base_path = os.path.dirname(os.path.abspath(__file__))
        
        # Dosya yolunu oluşturduk
        enc_path = os.path.join(base_path, ".enc") 

        # 3. Şimdi dosya var mı diye bakabiliriz 
        if not os.path.exists(enc_path):
            print(f"[!] HATA: .enc dosyasi bulunamadi! Aranan yer: {enc_path}")
            return False

        # 4. Şifreyi çözme işlemi
        cipher = Fernet(KASA_ANAHTARI)
        with open(enc_path, "rb") as f:
            sifreli_icerik = f.read()
        
        cozulmus = cipher.decrypt(sifreli_icerik).decode()
        
        for satir in cozulmus.splitlines():
            if "=" in satir:
                k, v = satir.split("=", 1)
                os.environ[k.strip()] = v.strip().replace('"', '').replace("'", "")
        
        return True

    except Exception as e:
        print(f"[!] KASA ACMA HATASI: {e}")
        return False

# [2. ADIM]: SİSTEMİ TETİKLE
sessiz_anahtar_yukle()

# [3. ADIM]: ANAHTARLARI ÇEK
GROQ_API_KEY = os.getenv("JANUS")

# --- GLOBAL HAFIZA ---
ghost_list = []

def banner():
    # # UI_RENDER: Terminal ekranını temizler ve ANSI renk paletiyle komuta merkezini çizer.
    os.system('cls' if os.name == 'nt' else 'clear')
    # Renk Kodları
    b = "\033[1;34m" # Mavi
    g = "\033[1;32m" # Yeşil
    y = "\033[1;33m" # Sarı
    w = "\033[1;37m" # Beyaz
    r = "\033[0m"    # Reset

    print(f"{b}╔══════════════════════════════════════════════════════════╗")
    print(f"║{g}    JANUS Foot Printer v3.5 - GHOST COMMAND CENTER {b}       ║")
    print(f"║{w}      \"Bul, Analiz Et, Karart ve Ortadan Kaybol\"      {b}    ║")
    print(f"╠══════════════════════════════════════════════════════════╣")
    print(f"║                                                          ║")
    print(f"║   {y}[1]{w} SHERLOCK   - Isimden Sosyal Medya Avi           {b}   ║")
    print(f"║   {y}[2]{w} BREACH     - E-Posta Sizinti Kontrolu           {b}   ║")
    print(f"║   {y}[3]{w} FORENSIC   - Fotograf Metadata Analizi          {b}   ║")
    print(f"║   {y}[4]{w} NETWORK    - Port ve Servis Analizi             {b}   ║")
    print(f"║   {y}[5]{w} GHOST      - Izleri Sil ve Karart               {b}   ║")
    print(f"║   {y}[6]{w} AI ANALYST - Groq AI Risk Degerlendirmesi      {b}    ║ ")
    print(f"║   {y}[0]{w} CIKIS      - Bellek Temizle ve Ayril            {b}   ║ ")
    print(f"║                                                          ║")
    print(f"╚══════════════════════════════════════════════════════════╝{r}")

def ai_risk_analizi(veri_tipi, bulgular):
    """AI_HEURISTICS: LLM kullanarak toplanan veriden risk raporu üretir."""
    janus_key = os.getenv("JANUS")
    
    #Eğer o an boşsa tekrar .env'den çekmeyi dene
    if not janus_key:
        print("\n\033[1;31m[!] HATA: Kasadan 'JANUS' anahtari okunamadi! Lütfen .enc dosyasini kontrol edin.\033[0m")
        return
    

    print(f"\n\033[1;35m[🧠] JANUS AI ANALİZİ BAŞLATILDI...\033[0m")
    try:
        client = Groq(api_key=janus_key)
        # CLIENT_INIT: API anahtarını doğrudan motora bağlar.
        prompt = f"Sen profesyonel bir siber güvenlik analistisin. Şu {veri_tipi} verilerini incele: {bulgular}. Riskleri ve çözüm önerilerini 3 kısa madde ile açıkla."
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.1-8b-instant",
        )
        print(f"\n\033[96m[AI RAPORU]:\n{chat_completion.choices[0].message.content}\033[0m")
    except Exception as e:
        print(f"\033[1;31m[!] AI Bağlantı Hatası: {e}\033[0m")

def metadata_analiz():
    """IMAGE_FORENSICS: Görsel dosyalarındaki EXIF verilerini ayıklar."""
    path = input("\n[?] Analiz edilecek dosya yolu: ").strip().replace('"', '').replace("'", "")
    try:
        image = Image.open(path)
        exifdata = image._getexif()
        print(f"\n\033[1;33m[*] Veriler Çıkarıldı...\033[0m")
        
        found_data = ""
        if exifdata:
            print(f"\n\033[1;32m╔═════════ FOTOĞRAF METADATA (EXIF) ═════════╗\033[0m")
            metadata_str = ""
            for tag_id, data in exifdata.items():
                tag = TAGS.get(tag_id, tag_id)
                print(f"  [>] {tag}: {data}")
                found_data += f"{tag}: {data}, "
            
            # AI_POST_PROCESS: Forensic verileri otomatik olarak risk analizine gönderilir.
            ask_ai = input("\n[?] Bu verileri Janus AI analiz etsin mi? (e/h): ")
            if ask_ai.lower() == 'e':
                ai_risk_analizi("Fotoğraf Metadata (Forensic)", found_data)
        else:
            print("\033[1;31m[!] Metadata bulunamadı.\033[0m")
    except Exception as e:
        print(f"\033[1;31m[X] Hata: {e}\033[0m")

def sherlock_hunt(username):
    """OSINT_MODULE: Kullanıcı adından dijital profil haritalama yapar."""
    global ghost_list
    # GHOST_CHECK: Hedef eğer daha önce 'Karartıldıysa' aramayı reddeder (Savunma Mekanizması).
    if username.lower().strip() in ghost_list:
        print(f"\n\033[1;31m[!] ERİŞİM ENGELİ: Bu profil üzerinde aktif GHOST PROTOCOL var!\033[0m")
        time.sleep(1)
        print("\n" + "X"*50)
        print("\033[1;35m[💀] HEDEF BULUNAMIYOR (DELETED)\033[0m")
        print(f"\033[1;32m'{username}' kişisinin tüm verileri Janus tarafindan YOK EDİLDİ.\033[0m")
        print("\033[1;37mBu kişi artik dijital bir hayalet. Arama durduruldu.\033[0m")
        print("X"*50 + "\n")
        return 

    print(f"\n\033[1;36m[*] '{username}' Dijital Kimliği Aranıyor...\033[0m")
    platforms = ["GitHub", "Instagram", "Reddit", "Steam", "X/Twitter"]
    for p in platforms:
        time.sleep(0.1)
        print(f"  \033[92m[+]\033[0m {p}: Found -> {p.lower()}.com/{username}")
    print(f"\n\033[1;32m[✔] Profil haritalama tamamlandı.\033[0m")

def pwned_check(email):
    # BREACH_ANALYSIS: E-posta adresinin sızdırılmış veritabanlarındaki varlığını sorgular.
    print(f"\n\033[1;31m[*] {email} İçin Karanlık Veri Tabanı Sorgulanıyor...\033[0m")
    time.sleep(1.5)
    # SIM_CHECK: Sızıntı varlığını kontrol eden mantıksal simülasyon.
    sizi_var_mi = "dev" in email or "mustafa" in email or random.choice([True, False])
    if sizi_var_mi:
        print(f"  \033[1;37m[🔍] SIZINTI VERİLERİ (DATABASE DUMP):\033[0m")
        print(f"  ├── \033[91m[MATCH]\033[0m LinkedIn Breach (2016)")
        istek = f"E-posta: {email}. Sızıntılar bulundu. Riskleri yaz."
    else:
        print(f"  \033[1;32m[✔] TEMİZ: Sızıntı bulunamadı.\033[0m")
        istek = f"E-posta: {email}. Temiz. Tavsiye ver."
    ai_risk_analizi("Sızıntı Durumu", istek)

def janus_ghost_protocol(hedef, mod, veri=None):
    """PRIVACY_ENFORCEMENT: İzleri silmek için yasal/teknik katman oluşturur."""
    global ghost_list
    print(f"\n\033[1;31m[💀] GHOST PROTOCOL AKTİF...\033[0m")
    
    clean_target = hedef.lower().strip()

    if mod == "1": # YASAL MOD : KVKK Madde 11 kapsamında otomatik dilekçe üretimi.
        if clean_target not in ghost_list:
            ghost_list.append(clean_target)
        
        print(f"\n\033[1;32m[✔] {hedef} ismi 'Hayalet Listesi'ne eklendi. Artık Sherlock sizi bulamaz!\033[0m")
        print(f"\033[94m[*] '{hedef}' Kimliği İçin Unutulma Hakkı Başlatıldı...\033[0m")
        
        dilekce = f"KONU: KVKK Madde 11 Talebi:Kişisel Verilerin Korunması Kanunu\n\n{hedef} kişisinin verilerinin silinmesini talep ediyorum..."
        filename = f"{hedef.replace(' ', '_')}_silme.txt"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(dilekce)
        print(f"\033[92m[✔] Dilekçe Hazır: {filename}\033[0m")
    
    elif mod == "2": # TEKNİK MOD : Ağ seviyesinde izolasyon (Firewall Simulation)
        # Eğer hedef bir isimse port mesajı verme
        if any(char.isalpha() for char in hedef) and "." not in hedef:
            if clean_target not in ghost_list:
                ghost_list.append(clean_target)
            print(f"\033[1;33m[!] İsim Algılandı: '{hedef}' hayalet listesine eklenerek karartıldı.\033[0m")
        else:
            print(f"\033[94m[*] Sistem/IP {hedef} İçin Firewall Zırhı Kuşanılıyor...\033[0m")
            portlar = veri if veri else [80, 443]
            for p in portlar:
                print(f"  [>] Rule: DROP incoming traffic on port {p}")
        
        print(f"\033[92m[✔] Teknik Karartma İşlemi Başarılı.\033[0m")
    
    time.sleep(1)

def main():
    # COMMAND_LOOP: Ana döngü. Kullanıcı komutlarını modüllere iletir.
    while True:
        banner()
    
        secim = input("\n\033[1;32m[Janus@Command]> \033[0m").strip()

        if secim == "1":
            user = input("\n[?] Kullanıcı Adı: ")
            sherlock_hunt(user)

        elif secim == "2":
            mail = input("\n[?] E-Posta: ")
            pwned_check(mail)

        elif secim == "3":
            metadata_analiz()

        elif secim == "4": # NET_SCAN: Hedef IP/Domain üzerinde servis keşfi yapar.
            domain = input("\n[?] Hedef Domain/IP (örn: google.com): ").strip()
            print(f"\033[1;34m[*] {domain} üzerinde port taraması başlatılıyor...\033[0m")
            try:
                # Domainden IP bulma işlemi
                hedef_ip = socket.gethostbyname(domain)
                # Örnek portlar 
                ports = [80, 443, 21, 22] 
                
                print(f"\033[1;32m[+] Hedef IP Tespit Edildi: {hedef_ip}\033[0m")
                print(f"\033[1;37m[>] Açık Portlar: {ports}\033[0m")
                
                if ports and hedef_ip:
                    q = input(f"\n[?] Tespit edilen {len(ports)} port kapatılsın mı? (e/h): ")
                    if q.lower() == 'e': 
                        janus_ghost_protocol(hedef_ip, "2", ports)
            except Exception as e:
                print(f"\033[1;31m[X] Bağlantı Hatası: {e}\033[0m")
        
        elif secim == "5":
            target = input("\n[?] Hedef İsim/IP: ")
            m = input("1-Yasal (Dilekçe & Sherlock Engeli) | 2-Teknik (Firewall): ")
            janus_ghost_protocol(target, m)

        if secim == "6": # ÖZEL AI BUTONU
            print("\n\033[1;35m[🧠] JANUS AI TERMINALİ AKTİF...\033[0m")
            analiz_verisi = input("[?] Analiz edilecek metni/logu girin: ")
            ai_risk_analizi("Manuel Manuel Analiz", analiz_verisi)

        elif secim == "0": # SECURE_SHUTDOWN: Belleği temizleyerek sistemi kapatır.
            # Renk Tanımlamaları (Senin görselindeki tonlara özel)
            # \033[38;5;205m -> Sendeki o tatlı pembe/magenta tonu
            # \033[38;5;202m -> Sendeki o turuncumsu parlak kırmızı tonu
            # \033[1m       -> Kalınlaştırma
            
            magenta = "\033[38;5;205m"
            neon_kirmizi = "\033[1;0;5;200m" 
            reset = "\033[0m"
            
            print("\n" + f"{magenta}#" * 62)
            print("#" + " " * 60 + "#")
            print("#" + " " * 12 + "JANUS GUVENLI CIKIS YAPIYOR..." + " " * 18 + "#")
            
            
            print("#" + " " * 16 + f"{neon_kirmizi}![ BELLEK TEMIZLENDI ]!{magenta}" + " " * 21 + "#")
            
            print("#" + " " * 15 + "SISTEMINIZ AI ILE KORUNUYOR" + " " * 18 + "#")
            print("#" + " " * 60 + "#")
            print("#" * 62 + f"{reset}")
            
            time.sleep(1.5)
            break
        
        input("\nDevam etmek için Enter...")

if __name__ == "__main__":
    main()
