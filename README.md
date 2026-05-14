# 🚩 Janus Foot Printer v3.5 🚩
### *AI-Powered OSINT, Forensic & Privacy Enforcement Suite*

<img width="800" height="421" alt="janusFootPrinter-ezgif com-video-to-gif-converter" src="https://github.com/user-attachments/assets/4151a88f-c23c-49fd-b47e-413b0d124014" />


Janus, dijital ayak izlerini takip etmek, siber riskleri analiz etmek ve gerektiğinde bu izleri "karartmak" için tasarlanmış hibrit bir güvenlik aracıdır. LLM (Llama 3.1) entegrasyonu ile ham veriyi siber güvenlik raporuna dönüştürür.

---

## 🛠️ Temel Modüller

| Modül | Fonksiyon | Açıklama |
| :--- | :--- | :--- |
| 🔍 **SHERLOCK** | Sosyal Medya Avı | Kullanıcı adından dijital profil haritalama yapar. |
| 🔓 **BREACH** | Sızıntı Kontrolü | E-posta adreslerinin dark web sızıntılarını sorgular. |
| 📷 **FORENSIC** | Metadata Analizi | Görsellerdeki gizli EXIF verilerini ayıklar. |
| 🌐 **NETWORK** | Servis Keşfi | Hedef sistemlerde port taraması ve zafiyet analizi yapar. |
| 💀 **GHOST PROTOCOL** | İz Silme & Karartma | KVKK dilekçesi üretir veya firewall kuralları simüle eder. |
| 🧠 **AI ANALYST** | Groq Llama 3.1 | Toplanan tüm bulguları profesyonel risk raporuna dönüştürür. |

---

## 🔐 Güvenlik: Ghost Vault (Şifreli Kasa)
Janus, API anahtarlarınızı kod içinde saklamaz. **Fernet (AES-128)** simetrik şifreleme kullanarak `.enc` dosyası içinde mühürler.

### **Kendi Kasanızı Oluşturun:**
1. `sifrele.py` dosyasındaki `icerik` kısmına API anahtarlarınızı yazın.
2. Scripti çalıştırarak `.enc` dosyasını üretin.
3. `printer.py` içindeki `KASA_ANAHTARI` değişkenine kendi anahtarınızı tanımlayın.

---

## 🚀 Kurulum

1. **Depoyu Klonlayın:**
```bash
git clone [https://github.com/mustafaColak0/Janus-Foot-Printer.git](https://github.com/mustafaColak0/Janus-Foot-Printer.git)
cd Janus-Foot-Printer
```
2. Gerekli Kütüphaneleri Yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

4. Çalıştırma
   ```bash
   python printer.py
   ```
   
⚠️ Yasal Uyarı (Disclaimer)
Bu araç sadece eğitim ve yasal siber güvenlik testleri (Pentest) için geliştirilmiştir. Yetkisiz sistemlere karşı kullanımı yasal sorumluluk doğurabilir. Geliştirici, kötüye kullanım durumunda sorumluluk kabul etmez.

Developed by mustafaColak0
