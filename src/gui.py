import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.append(current_dir)

from main import LibrarySystem

# Khởi tạo hệ thống
def init_system():
    """Khởi tạo hệ thống hoặc lấy từ session state"""
    if 'system' not in st.session_state:
        db_path = os.path.join(os.path.dirname(current_dir), 'data', 'library.db')
        st.session_state.system = LibrarySystem(db_path)
    return st.session_state.system

# Cấu hình trang
st.set_page_config(
    page_title="Hệ Thống Quản Lý Thư Viện",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS tùy chỉnh
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stButton>button {
        width: 100%;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

def show_dashboard(system):
    """Dashboard với các biểu đồ và thống kê"""
    st.title("📊 Dashboard")
    total_books = system.get_total_book()
    total_readers = system.get_total_member()
    currently_borrowed = system.get_currently_borowed()
    # Row 1: Các chỉ số tổng quan
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Tổng số sách", total_books)
    with col2:
        st.metric("Tổng độc giả", total_readers)
    with col3:
        st.metric("Đang mượn", currently_borrowed)
    
    st.divider()
    
    # Row 2: Biểu đồ
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📚 Phân bổ sách theo thể loại")
        try:
            df_categories = system.get_book_by_categories()
            if df_categories is not None and not df_categories.empty:
                fig = px.pie(df_categories, values='so_luong', names='ten_loai',
                           title='Phân bổ sách theo thể loại')
                st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("Chưa có dữ liệu sách")
        except Exception as e:
            st.error(f"Lỗi: {str(e)}")
    
    with col2:
        st.subheader("📊 Trạng thái mượn sách")
        try:
            fig = system.get_loan_status_distribution()
            st.pyplot(fig)
        except Exception as e:
            st.error(f"Lỗi: {str(e)}")
    
    # Row 3: Top sách được mượn nhiều nhất
    st.subheader("Top sách được mượn nhiều nhất")
    try:
        df_top_books = system.top_borrow(limit=5)
        if df_top_books is not None and not df_top_books.empty:
            fig = px.bar(df_top_books, x='ten_sach', y='luot_muon',
                       title='Top 5 sách được mượn nhiều nhất',
                       labels={'ten_sach': 'Tên sách', 'so_lan_muon': 'Số lần mượn'})
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Chưa có dữ liệu")
    except Exception as e:
        st.error(f"Lỗi: {str(e)}")
    
    # Row 4: Xu hướng mượn sách theo tháng
    st.subheader("📈 Xu hướng mượn sách theo tháng")
    try:
        df_monthly = system.get_monthly_trend()
        if df_monthly is not None and not df_monthly.empty:
            fig = px.line(df_monthly, x='thang', y='luot_muon',
                        title='Xu hướng mượn sách theo tháng',
                        labels={'thang': 'Tháng', 'so_luong': 'Số lượng'})
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Chưa có dữ liệu")
    except Exception as e:
        st.error(f"Lỗi: {str(e)}")

def show_book_management(system):
    """Quản lý sách"""
    st.title("📚 Quản Lý Sách")
    
    # Tabs cho các chức năng
    tab1, tab2, tab3, tab4 = st.tabs([" Thêm sách", " Tìm kiếm", "Danh sách", "Xóa sách"])
    with tab1:
        st.subheader("Thêm sách mới")
        with st.form("add_book_form"):
            ten_sach = st.text_input("Tên sách")
            tac_gia = st.text_input("Tác giả")
            so_luong = st.number_input("Số lượng", min_value=1, value=1)
            the_loai_id = st.number_input("Nhập ID thể loại \n | Công Nghệ Thông Tin: 1, Tiểu Thuyết: 2, Ngôn Tình: 3" ,min_value=1, value=1)
            link_tai = st.text_input("Link tải (tùy chọn)")
            
            submitted = st.form_submit_button("Thêm sách")
            if submitted:
                try:
                    system.add_book(ten_sach, tac_gia, so_luong, the_loai_id, link_tai)
                    st.success(f"Đã thêm sách: {ten_sach}")
                except Exception as e:
                    st.error(f"Lỗi: {str(e)}")
    
    with tab2:
        st.subheader("Tìm kiếm sách")
        keyword = st.text_input("Nhập từ khóa tìm kiếm")
        if st.button("🔍 Tìm kiếm"):
            try:
                results = system.search_book(keyword)
                if results is not None:
                    st.dataframe(results, use_container_width=True)
                else:
                    st.warning("Không tìm thấy sách nào")
            except Exception as e:
                st.error(f"Lỗi: {str(e)}")
    
    with tab3:
        st.subheader("Danh sách tất cả sách")
        try:
            all_books = system.get_all_book()  # Tìm kiếm rỗng để lấy tất cả
            st.dataframe(all_books, use_container_width=True)
        except Exception as e:
            st.error(f"Lỗi: {str(e)}")
    
    with tab4:
        st.subheader("Xóa sách")
        book_id = st.number_input("Nhập ID sách cần xóa", min_value=1, value=1)
        if st.button("🗑️ Xóa sách"):
            try:
                system.delete_book(book_id)
                st.success(f"Đã xóa sách có ID: {book_id}")
            except Exception as e:
                st.error(f" Lỗi: {str(e)}")

def show_member_management(system):
    """Quản lý độc giả"""
    st.title("👥 Quản Lý Độc Giả")
    
    # Tabs cho các chức năng
    tab1, tab2, tab3, tab4 = st.tabs([" Thêm độc giả", " Tìm kiếm", "Danh sách", "Xóa độc giả"])
    
    with tab1:
        st.subheader("Thêm độc giả mới")
        with st.form("add_member_form"):
            ten = st.text_input("Họ và tên")
            sdt = st.text_input("Số điện thoại")
            
            submitted = st.form_submit_button("Thêm độc giả")
            if submitted:
                try:
                    system.add_member(ten, sdt)
                    st.success(f"  Đã thêm độc giả: {ten}")
                except Exception as e:
                    st.error(f"Lỗi: {str(e)}")
    
    with tab2:
        st.subheader("Tìm kiếm độc giả")
        keyword = st.text_input("Nhập từ khóa tìm kiếm")
        if st.button("🔍 Tìm kiếm"):
            try:
                results = system.search_member(keyword)
                if results is not None:
                    st.dataframe(results, use_container_width=True)
                else:
                    st.warning("Không tìm thấy độc giả nào")
            except Exception as e:
                st.error(f"  Lỗi: {str(e)}")
    
    with tab3:
        st.subheader("Danh sách tất cả độc giả")
        try:
            all_members = system.get_all_member()
            if all_members is not None:
                st.dataframe(all_members, use_container_width=True)
            else:
                st.info("Chưa có độc giả nào trong hệ thống")
        except Exception as e:
            st.error(f"  Lỗi: {str(e)}")
    
    with tab4:
        st.subheader("Xóa độc giả")
        member_id = st.number_input("Nhập ID độc giả cần xóa", min_value=1, value=1)
        if st.button("🗑️ Xóa độc giả"):
            try:
                system.delete_member(member_id)
                st.success(f"  Đã xóa độc giả có ID: {member_id}")
            except Exception as e:
                st.error(f"  Lỗi: {str(e)}")

def show_loan_management(system):
    """Quản lý mượn trả"""
    st.title("📖 Quản Lý Mượn Trả")
    
    # Tabs cho các chức năng
    tab1, tab2, tab3 = st.tabs(["Mượn sách", "Trả sách", "Danh sách mượn"])
    
    with tab1:
        st.subheader("Mượn sách")
        with st.form("borrow_book_form"):
            sach_id = st.number_input("ID Sách", min_value=1, value=1)
            doc_gia_id = st.number_input("ID Độc giả", min_value=1, value=1)
            
            submitted = st.form_submit_button("Mượn sách")
            if submitted:
                try:
                    system.borrow_book(sach_id, doc_gia_id)
                    st.success(f"  Đã cho mượn sách ID: {sach_id} cho độc giả ID: {doc_gia_id}")
                except Exception as e:
                    st.error(f"  Lỗi: {str(e)}")
    
    with tab2:
        st.subheader("Trả sách")
        loan_id = st.number_input("Nhập ID phiếu mượn", min_value=1, value=1)
        if st.button("📥 Trả sách"):
            try:
                system.return_book(loan_id)
                st.success(f"  Đã trả sách cho phiếu mượn ID: {loan_id}")
            except Exception as e:
                st.error(f"  Lỗi: {str(e)}")
    
    with tab3:
        st.subheader("Danh sách mượn sách")
        status_filter = st.selectbox(
            "Lọc theo trạng thái",
            ["Tất cả", "Đang mượn", "Đã trả"]
        )
        
        # Map status
        status_map = {
            "Tất cả": None,
            "Đang mượn": "DangMuon",
            "Đã trả": "DaTra",
        }
        
        try:
            loans = system.get_loan_status(status_map[status_filter])
            if loans is not None:
                st.dataframe(loans, use_container_width=True)
            else:
                st.info("Không có phiếu mượn nào")
        except Exception as e:
            st.error(f"  Lỗi: {str(e)}")
        
        # Hiển thị báo cáo quá hạn
        st.divider()
        st.subheader("⚠️ Báo cáo sách quá hạn")
        try:
            overdue = system.get_overdue_report()
            if overdue is not None and not overdue.empty:
                st.dataframe(overdue, use_container_width=True)
            else:
                st.success("Không có sách quá hạn")
        except Exception as e:
            st.error(f"Lỗi: {str(e)}")

def main():
    """Hàm chính"""
    # Khởi tạo hệ thống
    system = init_system()
    
    # Sidebar
    st.sidebar.title("🏛️ Thư Viện")
    st.sidebar.divider()
    
    # Menu
    menu = st.sidebar.radio(
        "Chọn chức năng",
        ["📊 Dashboard", "📚 Quản lý Sách", "👥 Quản lý Độc giả", "📖 Mượn Trả"],
        label_visibility="collapsed"
    )
    
    st.sidebar.divider()
    st.sidebar.info("💡 Hệ thống quản lý thư viện")
    
    # Điều hướng
    if menu == "📊 Dashboard":
        show_dashboard(system)
    elif menu == "📚 Quản lý Sách":
        show_book_management(system)
    elif menu == "👥 Quản lý Độc giả":
        show_member_management(system)
    elif menu == "📖 Mượn Trả":
        show_loan_management(system)

if __name__ == "__main__":
    main()
