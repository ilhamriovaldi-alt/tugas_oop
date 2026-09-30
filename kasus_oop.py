# ==========================================
# KASUS 01: CLASS & OBJECT
# Sistem Pendataan Dosen
# ==========================================
print("=" * 40)
print("KASUS 01: SISTEM PENDATAAN DOSEN")
print("=" * 40)

class Dosen:
    def __init__(self, nidn, nama, prodi, fakultas, status_kelulusan):
        self.nidn = nidn
        self.nama = nama
        self.prodi = prodi
        self.fakultas = fakultas

        if status_kelulusan.lower() == "lulus":
            self.status_kelulusan = "Aktif / Memenuhi Syarat"
        else:
            self.status_kelulusan = "Tidak Aktif / Belum Memenuhi Syarat"

    def cek_profil(self):
        print(f"Profil Dosen : {self.nama} (NIDN: {self.nidn})")
        print(f"Fakultas     : {self.fakultas}")
        print(f"Status       : {self.status_kelulusan}")

    def cek_prodi(self):
        print(f"Program Studi: Mengajar di Prodi {self.prodi}")


dosen1 = Dosen(
    "00112233",
    "Budi Santoso, M.Kom",
    "Informatika",
    "Ilmu Komputer",
    "Lulus"
)

dosen2 = Dosen(
    "00445566",
    "Siti Aminah, M.T.",
    "Sistem Informasi",
    "Ilmu Komputer",
    "Belum Lulus"
)

dosen3 = Dosen(
    "00778899",
    "Andi Wijaya, Ph.D",
    "Teknik Elektro",
    "Teknik",
    "Lulus"
)

daftar_dosen = [dosen1, dosen2, dosen3]

for d in daftar_dosen:
    d.cek_profil()
    d.cek_prodi()
    print("-" * 30)


# ==========================================
# KASUS 02: PEWARISAN SIFAT
# Sistem Rental Kendaraan
# ==========================================
print("\n" + "=" * 40)
print("KASUS 02: SISTEM RENTAL KENDARAAN")
print("=" * 40)


class Kendaraan:
    def __init__(self, nama, merk, tahun, kecepatan):
        self.nama = nama
        self.merk = merk
        self.tahun = tahun
        self.kecepatan = kecepatan

    def info_kendaraan(self):
        print(f"Kendaraan    : {self.nama} ({self.merk})")
        print(f"Tahun/Max Spd: {self.tahun} | {self.kecepatan} km/jam")


class Mobil(Kendaraan):
    def __init__(self, nama, merk, tahun, kecepatan, jumlah_kursi):
        super().__init__(nama, merk, tahun, kecepatan)
        self.jumlah_kursi = jumlah_kursi

    def info_mobil(self):
        print("[ INFO MOBIL ]")
        self.info_kendaraan()
        print(f"Jumlah Kursi : {self.jumlah_kursi} Kursi")


class Motor(Kendaraan):
    def __init__(self, nama, merk, tahun, kecepatan, tipe_motor):
        super().__init__(nama, merk, tahun, kecepatan)
        self.tipe_motor = tipe_motor

    def info_motor(self):
        print("[ INFO MOTOR ]")
        self.info_kendaraan()
        print(f"Tipe Motor   : {self.tipe_motor}")


mobil_rental = Mobil("Innova Zenix", "Toyota", 2023, 180, 7)
motor_rental = Motor("Ninja 250", "Kawasaki", 2022, 200, "Sport")

mobil_rental.info_mobil()
print("-" * 30)
motor_rental.info_motor()


# ==========================================
# KASUS 03: MULTIPLE INHERITANCE
# Sistem Manajemen Pegawai
# ==========================================
print("\n" + "=" * 40)
print("KASUS 03: SISTEM MANAJEMEN PEGAWAI")
print("=" * 40)


class Pegawai:
    def __init__(self, id_pegawai, nama):
        self.id_pegawai = id_pegawai
        self.nama = nama


class Gaji:
    def __init__(self, gaji):
        self.gaji = gaji


class PegawaiProyek:
    def __init__(self, nama_proyek):
        self.nama_proyek = nama_proyek


class ProjectManager(Pegawai, Gaji, PegawaiProyek):
    def __init__(self, id_pegawai, nama, gaji, nama_proyek):
        Pegawai.__init__(self, id_pegawai, nama)
        Gaji.__init__(self, gaji)
        PegawaiProyek.__init__(self, nama_proyek)

    def info_project_manager(self):
        print("[ PROFIL PROJECT MANAGER ]")
        print(f"ID Pegawai   : {self.id_pegawai}")
        print(f"Nama Lengkap : {self.nama}")
        print(f"Gaji/Bulan   : Rp {self.gaji:,}")
        print(f"Nama Proyek  : {self.nama_proyek}")


pm = ProjectManager(
    id_pegawai="PM-001",
    nama="Rina Amelia",
    gaji=15000000,
    nama_proyek="Migrasi Sistem ERP Perusahaan"
)

pm.info_project_manager()