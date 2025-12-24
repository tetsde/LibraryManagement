import sqlite3
import os


class DataManager:
    
    def __init__(self, db_name):
        self.db_name = db_name
        self._tao_database_neu_chua_ton_tai()
    
    def _tao_database_neu_chua_ton_tai(self):
        db_dir = os.path.dirname(self.db_name)
        if db_dir and not os.path.exists(db_dir):
            os.makedirs(db_dir)
        
        query = """
        CREATE TABLE IF NOT EXISTS sach (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ten TEXT NOT NULL,
            so_luong INTEGER DEFAULT 0,
            loai_sach TEXT NOT NULL,
            link_tai TEXT
        )
        """
        self.thuc_thi(query)
    
    def thuc_thi(self, sql, params=()):
        conn = None
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute(sql, params)
            conn.commit()
            return True
        except sqlite3.Error as e:
            print(f"Lỗi database: {e}")
            return False
        finally:
            if conn:
                conn.close()
    
    def lay_tat_ca_sach(self):
        conn = None
        try:
            conn = sqlite3.connect(self.db_name)
            conn.row_factory = sqlite3.Row
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM sach")
            rows = cursor.fetchall()
            
            danh_sach_sach = [dict(row) for row in rows]
            return danh_sach_sach
        except sqlite3.Error as e:
            print(f"Lỗi khi lấy dữ liệu: {e}")
            return []
        finally:
            if conn:
                conn.close()


