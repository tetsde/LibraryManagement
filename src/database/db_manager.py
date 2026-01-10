import os
import sqlite3

class DBManager:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = sqlite3.connect(self.db_path,check_same_thread=False)
        self.connection.execute("PRAGMA foreign_keys = ON;")
        self.connection.row_factory = sqlite3.Row
        self.cursor = self.connection.cursor()
        os.makedirs(os.path.dirname(db_path), exist_ok=True)

    def close(self):
        self.connection.close()
        
    def execute_script(self, script_path):
        """Hàm thực thi file SQL"""
        if not os.path.exists(script_path):
            print(f" Không tìm thấy file script: {script_path}")
            return
        with open(script_path, 'r', encoding='utf-8') as f:
            sql_script = f.read()
        self.cursor.executescript(sql_script)
        self.connection.commit()
        print(f"Đã thực thi script từ {script_path}")

    def execute_query(self, query, params=()):
        """Hàm thực thi câu lệnh đơn (INSERT, UPDATE...)"""
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor

    def fetch_all(self, query, params=()):
        """Hàm lấy nhiều dòng"""
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor.fetchall()

    def fetch_one(self, query, params=()):
        """Hàm lấy 1 dòng"""
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor.fetchone()
    
if __name__ == "__main__":
    db_path = 'LibrarySystemV2/data/library.db'
    try:
        with DBManager(db_path) as db:
            db.execute_query("INSERT INTO doc_gia (ten_doc_gia, so_dien_thoai) VALUES (?, ?)", ("Nguyen Van A", '094579274'))
            db.execute_query("INSERT INTO sach (ten_sach, tac_gia) VALUES (?, ?)", ("Man's Search For Meaning", "Dale"))
            print("Đã thêm dữ liệu thành công")
            authors = db.fetch_all("SELECT * FROM doc_gia ")
            books = db.fetch_all("SELECT * FROM sach")
            print(f"\n Danh sách độc giả {len(authors)}")
            print(f"\n Danh sách sách  {len(books)}")
            for auth in authors:
                    #row_factor dùng user['name']
                    print(f"- Tên độc giả {auth['ten_doc_gia']} - Số điện thoại {auth['so_dien_thoai']}")
            for book in books:
                     print(f"- Tên sách {book['ten_sach']},{book['tac_gia']},{book['so_luong_tong']}")
    except Exception as e:
        print(f"Có lỗi xảy ra: {e}")

    print("\n--- KẾT THÚC TEST (Connection đã đóng an toàn) ---")
                