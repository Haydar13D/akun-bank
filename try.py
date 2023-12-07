import hashlib

class AkunBank:
    def __init__(self, username, password):
        self.username = username
        self.password = self._hash_password(password)

    def _hash_password(self, password):
        # Menggunakan hashlib untuk membuat hash SHA-256 dari kata sandi
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

    def check_password(self, input_password, input_username):
        # Memeriksa apakah kata sandi yang dimasukkan cocok dengan yang disimpan
        return self.username == input_username and self.password == self._hash_password(input_password)

def read_data_rahasia_from_file(data_rahasia):
    try:
        with open("data_rahasia.txt", 'r') as file:
            lines = file.readlines()

            if len(lines) >= 2:
                username = lines[0].strip()
                password = lines[1].strip()
                return username, password 
            else:
                print("File tidak memenuhi struktur yang diharapkan.")
                return None, None
    except FileNotFoundError:
        print(f"File {data_rahasia} not found.")
        return None, None

# Contoh penggunaan program
def main():
    # Mengambil data dari berkas
    filename = 'data_rahasia.txt'
    username, password = read_data_rahasia_from_file('data_rahasia.txt')

    if username and password:
        # Membuat akun
        user_account = AkunBank(username, password)
        print("Akun berhasil dibuat.")

        # Menggunakan akun
        for n in range(3):
            login_attempt = str(input("Masukan username untuk masuk: "))
            login_attempt1 =  str(input("Masukkan kata sandi untuk masuk: "))
            if user_account.username == login_attempt and user_account.check_password(login_attempt1,login_attempt):
                print("Masuk berhasil.")
                break
            else:
                print("Kombinasi username dan kata sandi salah. Masuk gagal.")
                if n == 2:
                    print("Anda telah mencoba 3 kali.")
                    break

if __name__ == "__main__":
    main()

#Buka berkas "data_rahasia.txt"
# Jika berhasil:
#     Baca username dan password dari berkas
#     Jika struktur berkas sesuai:
#         Buat objek AkunBank dengan username dan password
#         Tampilkan pesan bahwa akun berhasil dibuat
#         Untuk setiap percobaan login (sebanyak 3 kali):
#             Minta pengguna memasukkan username
#             Minta pengguna memasukkan kata sandi
#             Jika username dan kata sandi cocok dengan data yang disimpan:
#                 Tampilkan pesan bahwa login berhasil
#                 Keluar dari loop
#             Jika username dan kata sandi tidak cocok:
#                 Tampilkan pesan kesalahan
#                 Jika sudah mencoba 3 kali:
#                     Tampilkan pesan bahwa pengguna telah mencoba sebanyak 3 kali
#                     Keluar dari loop
#     Jika struktur berkas tidak sesuai:
#         Tampilkan pesan kesalahan
# Jika berkas tidak ditemukan:
#     Tampilkan pesan bahwa berkas tidak ditemukan