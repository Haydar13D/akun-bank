import hashlib

class akun_bank:
    def __init__(self, username, password):
        self.username = username
        self.password = self._hash_password(password)

    def _hash_password(self, password):
        # Menggunakan hashlib untuk membuat hash SHA-256 dari kata sandi
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

    def check_password(self, input_password):
        # Memeriksa apakah kata sandi yang dimasukkan cocok dengan yang disimpan
        return self.password == self._hash_password(input_password)

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
        user_account = akun_bank(username, password)
        print("Akun berhasil dibuat.")

        # Menggunakan akun
        for n in range(3):
            login_attempt = str(input("Masukkan kata sandi untuk masuk: "))

            if user_account.check_password(login_attempt):
                print("Masuk berhasil.")
                break
            else:
                print("Kata sandi salah. Masuk gagal.")
                if n == 2:
                    print("anda telah mencoba 3 kali")
                    break
                

if __name__ == "__main__":
    main()
