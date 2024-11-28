class AkunBank:
    def __init__(self, nama, saldo):
        self.nama = nama           # Public
        self._jenis_akun = "Tabungan"  # Protected
        self.__saldo = saldo       # Private

    def cek_saldo(self):           # Method Public untuk akses private
        return f"Saldo {self.nama}: Rp{self.__saldo}"

    def tambah_saldo(self, jumlah):  # Method Public untuk memodifikasi saldo
        if jumlah > 0:
            self.__saldo += jumlah
            return f"Saldo berhasil ditambahkan. {self.cek_saldo()}"
        return "Jumlah harus lebih besar dari 0."

    def _ubah_jenis_akun(self, jenis):  # Method Protected
        self._jenis_akun = jenis
        return f"Jenis akun diubah menjadi: {self._jenis_akun}"


# Kelas Turunan
class AkunPremium(AkunBank):
    def upgrade_akun(self):
        return self._ubah_jenis_akun("Premium")  # Bisa akses protected


# Contoh Penggunaan
akun = AkunPremium("Alice", 500000)

# Akses Public
print(akun.cek_saldo())              # Output: Saldo Alice: Rp500000
print(akun.tambah_saldo(200000))     # Output: Saldo berhasil ditambahkan. Saldo Alice: Rp700000

# Akses Protected (dalam turunan)
print(akun.upgrade_akun())           # Output: Jenis akun diubah menjadi: Premium

# Akses langsung terhadap Private akan error
# print(akun.__saldo)                # Error
# print(akun._jenis_akun)            # Bisa, tapi tidak disarankan
