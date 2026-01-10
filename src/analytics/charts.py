import pandas as pd
import matplotlib.pyplot as plt

class ChartModel:
    def __init__(self,db_manager):
        self.db = db_manager

    def get_book_by_categories(self):
        #Thống kê số lượng sách theo từng thể loại.
        query = """SELECT t.ten_loai, COUNT(s.id) as so_luong
        FROM sach s
        JOIN the_loai t ON s.the_loai_id = t.id
        GROUP BY t.ten_loai"""
        df = pd.read_sql_query(query, self.db.connection)
        return df
    
    def get_loan_status_distribution(self):
        #Tỉ lệ trạng thái mượn trả (Đang mượn vs Đã trả vs Quá hạn).
        query ="""SELECT trang_thai,COUNT(id) as so_luong 
        FROM muon_tra GROUP BY trang_thai"""
        df = pd.read_sql_query(query,self.db.connection)
        fig, ax = plt.subplots()
        ax.pie(df['so_luong'],labels=df['trang_thai'],autopct='%1.1f%%',startangle=90)
        ax.axis('equal')
        return fig
    
    def top_borrow(self,limit= 5):
        query = f"""SELECT  s.ten_sach, COUNT (m.id) as luot_muon
        FROM muon_tra m 
        JOIN sach s ON m.sach_id = s.id
        GROUP BY s.ten_sach
        ORDER BY luot_muon DESC
        LIMIT {limit}"""
        return pd.read_sql_query(query,self.db.connection)
    
    def get_monthly_trend(self):
        #Xu hướng mượn sách theo tháng (Line Chart)
        query = """SELECT strftime('%Y - %m',ngay_muon) as thang, COUNT(id) as luot_muon
        FROM muon_tra
        GROUP BY thang
        ORDER BY thang ASC """
        return pd.read_sql_query(query,self.db.connection)
    
    def get_category_distribution(self):
        #Phân bố thể loại được yêu thích nhất (Bar Chart)
        query = """SELECT t.ten_loai ,COUNT (m.id) as so_luong
        FROM muon_tra m 
        JOIN sach s ON m.sach_id = s.id
        JOIN the_loai t ON s.the_loai_id = t.id
        GROUP BY ten_loai
        ORDER BY so_luong DESC
        """
        return pd.read_sql_query(query,self.db.connection)
    
    def top_user(self,limit = 10):
        query = """SELECT d.ten_doc_gia, d.so_dien_thoai, COUNT (m.id) as tong_luot_muon
        FROM muon_tra m 
        JOIN doc_gia d ON m.doc_gia_id = d.id
        GROUP BY d.id
        ORDER BY tong_luot_muon DESC"""
        return pd.read_sql_query(query,self.db.connection)