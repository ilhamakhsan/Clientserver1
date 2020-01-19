import MySQLdb
import os

db = MySQLdb.connect(
    host="localhost",
    user="root",
    passwd="",
    database="kampus"
)


def tambah_data(db):
    nim = input("Masukan nim: ")
    nama = input("Masukan nama: ")
    alamat = input("Masukan alamat: ")
    isi = (nim, nama,alamat)
    cursor = db.cursor()
    perintahDB = "INSERT INTO mahasiswa (nim, nama, alamat) VALUES (%s, %s, %s)"
    cursor.execute(perintahDB, isi)
    db.commit()
    print("{} data mahasiswa berhasil disimpan".format(cursor.rowcount))


def ubah_data(db):
    cursor = db.cursor()
    tampilkan_data(db)
    id_mahasiswa = input("pilih id mahasiswa> ")
    nim = input("Nim baru: ")
    nama = input("Nama baru: ")
    alamat = input("Alamat baru: ")

    perintahDB = "UPDATE mahasiswa SET nim=%s,nama=%s, alamat=%s WHERE id=%s"
    isi = (nim, nama, alamat, id_mahasiswa)
    cursor.execute(perintahDB, isi)
    db.commit()
    print("{} data mahasiswa berhasil diubah".format(cursor.rowcount))




def hapus_data(db):
    cursor = db.cursor()
    tampilkan_data(db)
    id_mahasiswa = input("pilih id mahasiswa> ")
    perintahDB = "DELETE FROM mahasiswa WHERE id=%s"
    isi = (id_mahasiswa,)
    cursor.execute(perintahDB, isi)
    db.commit()
    print("{} data mahasiswa berhasil dihapus".format(cursor.rowcount))



def tampilkan_data(db):
    cursor = db.cursor()
    perintahDB = "SELECT * FROM `mahasiswa` "
    cursor.execute(perintahDB)
    results = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Tidak ada data")
    else:
        for data in results:
            print(data)


def tampilkan_menu(db):
    print()
    print("--- APLIKASI DATA MAHASISWA ---")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Lihat Data")
    print("5. keluar")
    print("-----------------------")
    menu = input("Pilih menu> ")

    #
    os.system("")

    if menu == "1":
        tambah_data(db)
    elif menu == "2":
        ubah_data(db)
    elif menu == "3":
        hapus_data(db)
    elif menu == "4":
        tampilkan_data(db)
    elif menu == "5":
        exit()
    else:
        print("Menu tidak ada!")


if __name__ == "__main__":
    while (True):
        tampilkan_menu(db)