import hashlib

class AkunBank:
    def __init__(self, username, password):
        # Inisialisasi objek AkunBank dengan username dan password
        self.username = username
        # Menggunakan fungsi _hash_password untuk mengenkripsi password
        self.password = self._hash_password(password)

    def _hash_password(self, password):
        # Menggunakan SHA-256 untuk mengenkripsi password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

    def _encrypt_password(self, password):
        # Fungsi untuk menghasilkan enkripsi password
        # menggunakan SHA-256
        encrypted_password = hashlib.sha256(password.encode()).hexdigest()
        return encrypted_password

    def get_encrypted_password(self):
        # Mengembalikan hasil enkripsi password
        return self._encrypt_password(self.password)

    def check_password(self, input_password, input_username):
        # Memeriksa kecocokan username dan password
        return self.username == input_username and self.password == self._hash_password(input_password)

def read_data_rahasia_from_file():
    try:
        with open("data_rahasia.txt", 'r') as file:
            # Membaca baris-baris dari file
            lines = file.readlines()

            accounts = []
            i = 0
            while i < len(lines):
                # Mengambil username dan password dari baris-baris yang dibaca
                username = lines[i].strip()
                password = lines[i + 1].strip()
                # Membuat objek AkunBank dan menambahkannya ke list accounts
                account = AkunBank(username, password)
                accounts.append(account)
                i += 2

            return accounts
    except FileNotFoundError:
        # Menangani kasus jika file tidak ditemukan
        print("File data_rahasia.txt not found.")
        return None

def main():
    # Membaca data akun dari file
    accounts = read_data_rahasia_from_file()

    if accounts:
        for n in range(3):
            # Meminta input dari pengguna untuk username dan password
            login_attempt_username = str(input("Masukkan username untuk masuk: "))
            login_attempt_password = str(input("Masukkan kata sandi untuk masuk: "))

            for ak in accounts:
                # Memeriksa kecocokan input dengan data akun
                if ak.username == login_attempt_username and ak.check_password(login_attempt_password, login_attempt_username):
                    print("Masuk berhasil.")
                    # Mengambil dan mencetak hasil enkripsi password
                    encrypted_password = ak.get_encrypted_password()
                    print(f"Kode enkripsi dari password: {encrypted_password}")
                    return
                elif ak.username == login_attempt_username and not ak.check_password(login_attempt_password, login_attempt_username):
                    # Menangani kasus jika password salah
                    print("Kata sandi salah. Masuk gagal.")
                    if n == 2:
                        # Menangani kasus jika sudah 3 kali percobaan
                        print("Anda telah mencoba 3 kali.")
                        break

if __name__ == "__main__":
    main()
