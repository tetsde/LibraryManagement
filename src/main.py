import sys
import os
import pandas as pd
import streamlit as st

current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, 'src')
if src_path not in sys.path:
    sys.path.append(src_path)

from database.db_manager import DBManager
from models.book import BookModel
from models.member import MemberModel
from models.loan import LoanModel
from analytics.charts import ChartModel
from analytics.report_generator import ReportGenerator

class LibrarySystem:
   def __init__(self, db_path):
       self.db = DBManager(db_path)
       print("Kết nối đến cơ sở dữ liệu thành công")
       self.book_model = BookModel(self.db)
       self.member_model = MemberModel(self.db)
       self.loan_model = LoanModel(self.db)
       self.chart_model = ChartModel(self.db)
       self.report_model = ReportGenerator(self.db)
       print("Kết nối đến các bảng thành công")

       
    #BookManager
   def get_all_book(self):
       return self.book_model.get_all_book()
   
   def get_all_categories(self):
       return self.book_model.get_categories()
   
   def add_book(self,ten_sach,tac_gia,so_luong,the_loai_id,link_tai =""):
       return  self.book_model.add_book(ten_sach,tac_gia,so_luong,the_loai_id,link_tai='')
    
   def search_book(self,keyword):
       return self.book_model.search_book(keyword)
    
   def get_total_book(self):
       return self.book_model.get_total_books()
    
   def delete_book(self,book_id):
       self.book_model.delete_book(book_id)
       return True
    
   def upload_book(self,book_id,ten_sach,so_luong,tac_gia,the_loai_id):
       self.book_model.upload_book(ten_sach,so_luong,tac_gia,the_loai_id)
       return True

    #MemberManager
    
   def get_all_member(self):
       return self.member_model.get_all_member()
    
   def add_member(self,ten,sdt):
       self.member_model.add_member(ten,sdt)
       return True

   def delete_member(self,id_member):
       self.member_model.delete_member(id_member)
       return True
    
   def get_total_member(self):
       return self.member_model.get_total_readers()

   def search_member(self,keyword):
       return self.member_model.search_member(keyword)

    #LoanManger
   def get_loan_status(self,status=None):
       return self.loan_model.get_loan_status(status)
    
   def borrow_book(self,sach_id,doc_gia_id):
       self.loan_model.borrow_book(sach_id,doc_gia_id)
       return True
    
   def return_book(self, loan_id):
       self.loan_model.return_book(loan_id)
       return True
   def get_currently_borowed(self):
       return self.loan_model.get_currently_borrowed()

    #Chart
   def get_book_by_categories(self):
       return self.chart_model.get_book_by_categories()

   def get_loan_status_distribution(self):
       return self.chart_model.get_loan_status_distribution()

   def top_borrow(self,limit= 5):
       return self.chart_model.top_borrow(limit)
    
   def get_monthly_trend(self):
       return self.chart_model.get_monthly_trend()

   def get_category_distribution(self):
       return self.chart_model.get_category_distribution()

   def top_user(self,limit = 10):
       return self.chart_model.top_user()
    
    #ReportGenerator
   def get_overdue_report(self):
       return self.report_model.get_overdue_report()
    
   def get_full_activity_log(self):
       return self.report_model.get_full_activity_log()


if __name__ == "__main__":
    DB_FILE = os.path.join(current_dir,'data','library.db')
    system  = LibrarySystem(DB_FILE) 


 
  



