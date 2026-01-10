import sys
import os
import random
from faker import Faker
import datetime

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from database.db_manager import DBManager


DB_PATH = os.path.join(os.path.dirname(current_dir), 'data', 'library.db')
fake = Faker('vi_VN') # Dùng tiếng Việt

def seed_data():
    print(f"Đang kết nối Database: {DB_PATH}")
    db = DBManager(DB_PATH)

    categories = db.fetch_all("SELECT id FROM the_loai")
    if not categories:
        db.execute_query("INSERT INTO the_loai (ten_loai) VALUES (?)", ("Tổng hợp",))
        categories = db.fetch_all("SELECT id FROM the_loai")
    cat_ids = [c['id'] for c in categories]

    print("Đang tạo 5000 sách mẫu...")
    books = []
    for _ in range(5000):
        ten_sach = fake.sentence(nb_words=4).replace(".", "").title()
        tac_gia = fake.name()
        so_luong = random.randint(5, 50)
        cat_id = random.choice(cat_ids)
        link_tai = ""
        books.append((ten_sach, tac_gia, so_luong, cat_id, link_tai))
    
    db.cursor.executemany(
        "INSERT INTO sach (ten_sach, tac_gia, so_luong_tong, the_loai_id, link_tai) VALUES (?, ?, ?, ?, ?)", 
        books
    )
    db.connection.commit()

    print("Đang tạo 1000 độc giả giả lập...")
    users = [(fake.name(), fake.phone_number()) for _ in range(1000)]
    db.cursor.executemany(
        "INSERT INTO doc_gia (ten_doc_gia, so_dien_thoai) VALUES (?, ?)", 
        users
    )
    db.connection.commit()

    all_books = db.fetch_all("SELECT id FROM sach")
    all_members = db.fetch_all("SELECT id FROM doc_gia")

    if not all_books:
        print("Cần có ít nhất 1 cuốn sách trong kho để tạo dữ liệu mượn!")
        return

    book_ids = [b['id'] for b in all_books]
    member_ids = [m['id'] for m in all_members]

    print("Đang tạo 5000 lượt mượn trong 2 năm qua...")
    loans = []
    start_date = datetime.date(2023, 1, 1)
    end_date = datetime.date.today()

    for _ in range(5000):
        s_id = random.choice(book_ids)
        m_id = random.choice(member_ids)

        random_days = random.randint(0, (end_date - start_date).days)
        ngay_muon = start_date + datetime.timedelta(days=random_days)
        ngay_du_kien = ngay_muon + datetime.timedelta(days=random.randint(7, 14))

        status_dice = random.random()
        if status_dice < 0.9:
            trang_thai = 'DaTra'
            ngay_tra_thuc = ngay_du_kien + datetime.timedelta(days=random.randint(-2, 5))
        else:
            trang_thai = 'DangMuon'
            ngay_tra_thuc = None

        loans.append((
            s_id,
            m_id,
            ngay_muon.strftime('%Y-%m-%d'),
            ngay_du_kien.strftime('%Y-%m-%d'),
            ngay_tra_thuc.strftime('%Y-%m-%d') if ngay_tra_thuc else None,
            trang_thai
        ))

    query_loan = """
    INSERT INTO muon_tra (sach_id, doc_gia_id, ngay_muon, ngay_tra_du_kien, ngay_tra_thuc_te, trang_thai)
    VALUES (?, ?, ?, ?, ?, ?)
    """
    db.cursor.executemany(query_loan, loans)
    db.connection.commit()

    print("HOÀN TẤT! Database đã có dữ liệu mẫu.")
if __name__ == "__main__":
    seed_data()