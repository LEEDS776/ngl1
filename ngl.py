import requests
import json
import time
import random
from urllib.parse import urlparse

def spam_ngl(ngl_link, message, num_spams, delay=2):
    """
    Melakukan spam pesan ke tautan NGL tertentu.

    Args:
        ngl_link (str): Tautan NGL yang ingin di-spam.
        message (str): Pesan yang akan dikirimkan.
        num_spams (int): Jumlah spam yang akan dikirim.
        delay (float): Delay antara setiap spam (dalam detik).
    """

    # Endpoint API yang diperbarui
    api_endpoint = "https://ngl.link/api/submit"
    
    # Ekstrak username dari tautan
    parsed_url = urlparse(ngl_link)
    username = parsed_url.path.strip('/')
    
    if not username:
        print("❌ Error: Tidak bisa mengekstrak username dari tautan!")
        return

    print(f"🎯 Target: {username}")
    print(f"💬 Pesan: {message}")
    print(f"🔢 Jumlah: {num_spams} kali")
    print("=" * 50)

    # Headers yang lebih lengkap
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Origin": "https://ngl.link",
        "Referer": f"https://ngl.link/{username}",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
    }

    success_count = 0
    failed_count = 0

    for i in range(num_spams):
        # Payload dengan format yang mungkin berubah
        payload = {
            "username": username,
            "question": message,
            "deviceId": f"device_{random.randint(100000, 999999)}",
            "gameSlug": "",
            "referrer": ""
        }

        try:
            print(f"🔄 Mengirim spam ke-{i+1}...")
            response = requests.post(
                api_endpoint, 
                data=payload, 
                headers=headers,
                timeout=10
            )
            
            print(f"📊 Response: {response.status_code}")
            
            # Debug info
            if response.status_code != 200:
                print(f"📝 Response text: {response.text[:100]}...")
            
            if response.status_code == 200:
                success_count += 1
                print(f"✅ Spam ke-{i+1} berhasil dikirim!")
            else:
                failed_count += 1
                print(f"❌ Gagal mengirim spam ke-{i+1}. Status: {response.status_code}")

        except requests.exceptions.RequestException as e:
            failed_count += 1
            print(f"🚫 Error pada spam ke-{i+1}: {e}")

        # Delay yang lebih lama antara spam
        if i < num_spams - 1:
            sleep_time = delay + random.uniform(0.5, 1.5)
            print(f"⏳ Menunggu {sleep_time:.1f} detik...")
            time.sleep(sleep_time)

    print("=" * 50)
    print(f"📊 Hasil Akhir: Berhasil: {success_count}, Gagal: {failed_count}")

def test_connection():
    """Test koneksi ke server NGL"""
    print("🧪 Testing koneksi ke NGL...")
    try:
        response = requests.get("https://ngl.link", timeout=10)
        if response.status_code == 200:
            print("✅ Koneksi ke NGL berhasil!")
            return True
        else:
            print(f"❌ Koneksi gagal: Status {response.status_code}")
            return False
    except Exception as e:
        print(f"❌ Koneksi gagal: {e}")
        return False

def main():
    print("=" * 60)
    print("🛡️  NGL Spammer Tool (Fixed Version)")
    print("=" * 60)
    
    # Test koneksi dulu
    if not test_connection():
        print("❌ Tidak bisa melanjutkan karena koneksi gagal")
        return
    
    print()
    
    try:
        ngl_link = input("🔗 Masukkan tautan NGL (contoh: https://ngl.link/username): ").strip()
        
        # Validasi tautan
        if not ngl_link.startswith("https://ngl.link/"):
            print("❌ Error: Format tautan harus 'https://ngl.link/username'")
            return

        message = input("💬 Masukkan pesan spam: ").strip()
        if not message:
            print("❌ Error: Pesan tidak boleh kosong!")
            return

        if len(message) > 100:
            print("⚠️  Peringatan: Pesan terlalu panjang, mungkin akan dipotong oleh NGL")

        num_spams = int(input("🔢 Masukkan jumlah spam: "))
        if num_spams <= 0:
            print("❌ Error: Jumlah spam harus lebih dari 0!")
            return

        if num_spams > 50:
            print("⚠️  Peringatan: Jumlah spam besar mungkin terdeteksi sebagai spam!")
            
        delay = float(input("⏱️  Masukkan delay antara spam (detik, rekomendasi 2): ") or "2")

        print("\n🚀 Memulai proses spam...")
        print("=" * 50)
        spam_ngl(ngl_link, message, num_spams, delay)

    except ValueError as e:
        print(f"❌ Error input: {e}")
    except KeyboardInterrupt:
        print("\n⏹️  Program dihentikan oleh pengguna.")
    except Exception as e:
        print(f"❌ Error tidak terduga: {e}")

if __name__ == "__main__":
    main()
