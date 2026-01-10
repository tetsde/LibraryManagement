import pandas as pd
class MemberModel:
    def __init__(self,db_manager):
        self.db = db_manager

    def get_all_member(self):
        query = '''SELECT 
            id AS docgia_id,
            ten_doc_gia AS docgia_ten,
            so_dien_thoai AS docgia_sdt,
            ngay_tham_gia AS docgia_ngaytao
        FROM doc_gia
        ORDER BY id DESC;'''
        rows = self.db.fetch_all(query)
        columns = ["docgia_id", "docgia_ten", "docgia_sdt", "docgia_ngaytao"]
        return pd.DataFrame(rows, columns=columns)

    def search_member(self,keyword):
        query = ''' SELECT * FROM doc_gia WHERE ten_doc_gia LIKE ? 
                   OR so_dien_thoai LIKE ?
                   ORDER BY id DESC '''
        search_temp = f"%{keyword}%"
        return self.db.fetch_all(query, (search_temp,search_temp))
    
    def get_total_readers(self):
        query = "SELECT COUNT(*) FROM doc_gia"
        result = self.db.fetch_one(query)
        return result[0] if result else 0
    
    def add_member(self,ten,sdt):
        if not ten:
            raise ValueError("Tên độc giả không được để trống")
        query = '''INSERT OR IGNORE INTO doc_gia (ten_doc_gia, so_dien_thoai) VALUES (?, ?)'''
        self.db.execute_query(query, (ten, sdt))
        return True
    
    def delete_member(self,id_member):
        if not id_member:
            raise ValueError("Tên không được để trống")
        query = '''DELETE FROM doc_gia WHERE id = ?'''
        self.db.execute_query(query,(id_member,))
        return True
         