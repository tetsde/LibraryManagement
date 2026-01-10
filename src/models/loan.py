from datetime import datetime, timedelta

class LoanModel:
    def __init__(self,db_manager):
        self.db = db_manager
        
    def get_loan_status(self, status=None):
        query = '''SELECT 
                m.id AS muontra_id,           
                s.ten_sach AS sach_ten,       
                d.ten_doc_gia AS docgia_ten,  
                m.ngay_muon AS ngay_muon,    
                m.ngay_tra_du_kien AS ngay_tra_du_kien, 
                m.ngay_tra_thuc_te AS ngay_tra_thuc_te, 
                m.trang_thai AS trang_thai, 
                m.ghi_chu AS ghi_chu           
            FROM muon_tra m
            JOIN sach s ON m.sach_id = s.id
            JOIN doc_gia d ON m.doc_gia_id = d.id
            '''
        params = ()
        if status:
            query += " WHERE m.trang_thai = ?"
            params = (status,)
        query += " ORDER BY m.id DESC"
        return self.db.fetch_all(query, params)
    
    def get_currently_borrowed(self):
        query = "SELECT COUNT(*) FROM muon_tra WHERE trang_thai = 'DangMuon'"
        result = self.db.fetch_one(query)
        return result[0] if result else 0


    def borrow_book(self, sach_id, doc_gia_id):
        hien_tai = datetime.now()
        ngay_muon_str = hien_tai.strftime('%Y-%m-%d')
        ngay_tra_obj = hien_tai + timedelta(days=7)
        ngay_tra_str = ngay_tra_obj.strftime('%Y-%m-%d')

        book = self.db.fetch_one("SELECT so_luong_tong FROM sach WHERE id = ?", (sach_id,))
        if not book:
            raise ValueError("Sách không tồn tại!")
        if book['so_luong_tong'] < 1:
            raise ValueError("Sách này đã hết hàng, không thể mượn!")
        
        update_query = "UPDATE sach SET so_luong_tong = so_luong_tong - 1 WHERE id = ? AND so_luong_tong > 0"
        self.db.execute_query(update_query, (sach_id,))
        query_loan = """
        INSERT INTO muon_tra (sach_id, doc_gia_id, ngay_muon, ngay_tra_du_kien, trang_thai)
        VALUES (?, ?, ?, ?, 'DangMuon')
        """
        self.db.execute_query(query_loan, (sach_id, doc_gia_id, ngay_muon_str, ngay_tra_str))
        print(f"Đã tạo phiếu mượn thành công ngày {ngay_muon_str}")
        return True
    
    def return_book(self,loan_id):
        loan = self.db.fetch_one("SELECT sach_id, trang_thai FROM muon_tra WHERE id = ?", (loan_id,))
        if not loan:
            raise ValueError ("Phiếu mượn không tồn tại")
        if loan['trang_thai'] == 'DaTra':
            raise ValueError("Sách này đã được trả rồi!")
        sach_id = loan['sach_id']
        query_update =  """ UPDATE muon_tra 
            SET ngay_tra_thuc_te = DATE('now'), 
                trang_thai = 'DaTra'
            WHERE id = ?"""
        self.db.execute_query(query_update, (loan_id,))
        self.db.execute_query("UPDATE sach SET so_luong_tong = so_luong_tong + 1 WHERE id = ?", (sach_id,))
        print("Trả sách thành công")
        return True



