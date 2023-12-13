import hashlib

class AkunBank:
    def __init__(self, username, password):
        self.username = username
        self.password = self._hash_password(password)

    def _hash_password(self, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

    def _encrypt_password(self, password):
        encrypted_password = hashlib.sha256(password.encode()).hexdigest()
        return encrypted_password

    def get_encrypted_password(self):
        return self._encrypt_password(self.password)

    def check_password(self, input_password, input_username):
        return self.username == input_username and self.password == self._hash_password(input_password)

def read_data_rahasia_from_file():
    try:
        with open("data_rahasia.txt", 'r') as file:
            lines = file.readlines()

            accounts = []
            i = 0
            while i < len(lines):
                username = lines[i].strip()
                password = lines[i + 1].strip()
                account = AkunBank(username, password)
                accounts.append(account)
                i += 2

            return accounts
    except FileNotFoundError:
        print("File data_rahasia.txt not found.")
        return None

def main():
    accounts = read_data_rahasia_from_file()

    if accounts:
        for user_account in accounts:
            print(f"Akun berhasil dibuat untuk {user_account.username}.")
            encrypted_password = user_account.get_encrypted_password()
            print(f"Kode enkripsi dari password: {encrypted_password}")

            for n in range(3):
                login_attempt = str(input("Masukkan username untuk masuk: "))
                login_attempt1 = str(input("Masukkan kata sandi untuk masuk: "))

                if user_account.username == login_attempt and user_account.check_password(login_attempt1, login_attempt):
                    print("Masuk berhasil.")
                    return
                else:
                    print("Kata sandi salah. Masuk gagal.")
                    if n == 2:
                        print("Anda telah mencoba 3 kali.")
                        break

if __name__ == "__main__":
    main()
