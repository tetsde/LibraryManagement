import pandas as pd
class ReportGenerator:
    def __init__(self,db_manager):
        self.db = db_manager

    def get_overdue_report(self):
        #Lọc ra danh sách những người đang mượn quá hạn.
        query = """SELECT d.ten_doc_gia, d.so_dien_thoai, s.ten_sach, m.ngay_tra_du_kien
        FROM muon_tra m 
        JOIN doc_gia d ON m.doc_gia_id = d.id
        JOIN sach s ON m.sach_id = s.id
        WHERE m.trang_thai = 'DangMuon'
        AND DATE ('now') >= m.ngay_tra_du_kien
        """
        return pd.read_sql_query(query,self.db.connection)
    
    def get_full_activity_log(self):
        #Xuất toàn bộ lịch sử hoạt động để làm báo cáo tổng kết.
        query = """SELECT m.id, d.ten_doc_gia,s.ten_sach,m.ngay_muon,m.ngay_tra_du_kien,m.ngay_tra_thuc_te,m.trang_thai
        FROM muon_tra m
        JOIN sach s ON m.sach_id = s.id
        ORDER BY m.ngay_muon DESC """
        return pd.read_sql_query(query,self.db.connection)
