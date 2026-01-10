import pandas as pd
class BookModel:
    def __init__(self,db_manager):
        self.db = db_manager
        
    def get_all_book(self):
        query = """SELECT 
                s.id AS sach_id,          
                s.ten_sach AS sach_ten,    
                s.tac_gia AS sach_tacgia, 
                s.so_luong_tong AS sach_soluong, 
                t.ten_loai AS loai_ten,   
                s.ngay_nhap AS sach_ngay_nhap    
            FROM sach s
            LEFT JOIN the_loai t ON s.the_loai_id = t.id
            ORDER BY s.id DESC;
            """
        rows = self.db.fetch_all(query)
        columns = ['sach_id','sach_ten','sach_tacgia','sach_soluong','loai_ten','sach_ngay_nhap']
        return pd.DataFrame(rows, columns = columns)
    
    def get_total_books(self):
        query = "SELECT COUNT(*) FROM sach"
        result = self.db.fetch_one(query) 
        return result[0] if result else 0
    
    def search_book(self,keyword):
        query = """SELECT s.id, s.ten_sach, s.tac_gia, s.so_luong_tong, t.ten_loai, s.ngay_nhap
        FROM sach s
        LEFT JOIN the_loai t ON s.the_loai_id = t.id
        WHERE s.ten_sach LIKE ? OR s.tac_gia LIKE ?"""
        search_term = f"%{keyword}%"
        return self.db.fetch_all(query,(search_term,search_term))
    
    def get_categories(self):
        return self.db.fetch_all("SELECT * FROM the_loai")
    
    def add_book(self, ten_sach, tac_gia, so_luong, the_loai_id, link_tai=""):
    
        if so_luong < 0:
            raise ValueError("Số lượng không được dưới 0")
        if not ten_sach:
            raise ValueError("Tên sách không được để trống")
        
        query = "SELECT id, so_luong_tong FROM sach WHERE ten_sach = ? AND tac_gia = ?"
        existing = self.db.fetch_one(query, (ten_sach, tac_gia))
        
        if existing:
            new_qty = existing['so_luong_tong'] + so_luong
            update_query = "UPDATE sach SET so_luong_tong = ? WHERE id = ?"
            self.db.execute_query(update_query, (new_qty, existing['id']))
        else:
            insert_query = "INSERT INTO sach(ten_sach, tac_gia, so_luong_tong, the_loai_id, link_tai) VALUES (?,?,?,?,?)"
            self.db.execute_query(insert_query, (ten_sach, tac_gia, so_luong, the_loai_id, link_tai))
        
        return True

        
    def delete_book(self,book_id):
        query = """DELETE FROM sach WHERE id = ?"""
        self.db.execute_query(query,(book_id,))
        return True
    
    def upload_book(self,book_id,ten_sach,so_luong,tac_gia,the_loai_id):
        query ="""UPDATE sach SET ten_sach = ?, tac_gia = ?, so_luong_tong = ?,the_loai_id = ?
        WHERE id = ?"""
        self.db.execute_query(query,(ten_sach,tac_gia,so_luong,the_loai_id))
        return True
