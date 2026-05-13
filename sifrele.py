from cryptography.fernet import Fernet

# 1. Sabit Kilidimiz
KASA_ANAHTARI = b'BURAYA_KENDI_FERNET_ANAHTARINIZI_YAZIN'
cipher = Fernet(KASA_ANAHTARI)

# 2. Şifrelenecek Gerçek Bilgilerin (Burayı kendine göre doldur)
icerik = "JANUS=BURAYA_KENDI_FERNET_ANAHTARINIZI_YAZIN"

# 3. Şifreleme İşlemi
sifreli_veri = cipher.encrypt(icerik.encode())

# 4. .enc Dosyasına Yazma
with open(".enc", "wb") as f:
    f.write(sifreli_veri)

print("-" * 30)
print("[✔] .enc DOSYASI OLUŞTURULDU!")
print("[!] Dosyanın içi artık karmaşık kodlarla dolu.")
print("[!] Bu dosyayı EXE'nin yanına koyman yeterli.")
print("-" * 30)