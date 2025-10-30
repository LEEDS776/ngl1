import requests
import json
import time
import random

def spam_ngl(ngl_link, message, num_spams, delay=1):
    """
    Melakukan spam pesan ke tautan NGL tertentu.

    Args:
        ngl_link (str): Tautan NGL yang ingin di-spam.
        message (str): Pesan yang akan dikirimkan.
        num_spams (int): Jumlah spam yang akan dikirim.
        delay (float): Delay antara setiap spam (dalam detik).
    """

    api_endpoint = "https://ngl.link/api/submit"
    
    # Ekstrak username dari tautan
    username = ngl_link.split("/")[-1]
    if not username:
        print("Error: Tautan NGL tidak valid!")
        return

    print(f"Memulai spam ke: {username}")
    print(f"Pesan: {message}")
    print(f"Jumlah: {num_spams} kali")
    print("-" * 50)

    success_count = 0
    failed_count = 0

    for i in range(num_spams):
        payload = {
            "question": message,
            "username": username
        }

        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded",
        }

        try:
            response = requests.post(api_endpoint, data=payload, headers=headers)
            
            if response.status_code == 200:
                success_count += 1
                print(f"✅ Spam ke-{i+1} berhasil dikirim.")
            else:
                failed_count += 1
                print(f"❌ Gagal mengirim spam ke-{i+1}. Status code: {response.status_code}")

        except requests.exceptions.RequestException as e:
            failed_count += 1
            print(f"❌ Error pada spam ke-{i+1}: {e}")

        # Delay antara spam
        if i < num_spams - 1:
            sleep_time = delay + random.uniform(0.1, 0.5)
            print(f"⏳ Menunggu {sleep_time:.1f} detik...")
            time.sleep(sleep_time)

    print("-" * 50)
    print(f"✅ Selesai! Berhasil: {success_count}, Gagal: {failed_count}")

def main():
    print("=" * 50)
    print("🛡️  NGL Spammer Tool")
    print("=" * 50)
    
    try:
        ngl_link = input("🔗 Masukkan tautan NGL: ").strip()
        if not ngl_link.startswith("https://ngl.link/"):
            print("❌ Error: Tautan harus dimulai dengan 'https://ngl.link/'")
            return

        message = input("💬 Masukkan pesan spam: ").strip()
        if not message:
            print("❌ Error: Pesan tidak boleh kosong!")
            return

        num_spams = int(input("🔢 Masukkan jumlah spam: "))
        if num_spams <= 0:
            print("❌ Error: Jumlah spam harus lebih dari 0!")
            return

        print("\n🚀 Memulai proses spam...")
        spam_ngl(ngl_link, message, num_spams)

    except ValueError:
        print("❌ Error: Jumlah spam harus berupa angka!")
    except KeyboardInterrupt:
        print("\n⏹️  Program dihentikan oleh pengguna.")
    except Exception as e:
        print(f"❌ Error tidak terduga: {e}")

if __name__ == "__main__":
    main()
