import os
import sys

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

from database.db_manager import DBManager

def db_init(schema_path):
    base_dir = os.path.dirname(current_dir)
    db_path = os.path.join(base_dir, 'data', 'library.db')
    schema_path = os.path.join(current_dir, 'database', 'schema.sql')

    print('Đang khởi tạo database từ',db_path)
    print("Đang đọc schema từ ",schema_path)

    try:
        with DBManager(db_path) as db:
            db.execute_script(schema_path)
            print("\n Kiểm tra danh sách bảng đã tạo:")
            tables = db.fetch_all("SELECT name FROM sqlite_master WHERE type='table';")
            for table in tables:
                print(f"  - Bảng: {table['name']}")
                
            books = db.fetch_all("SELECT * FROM sach")
            print(f"\nSố lượng sách mẫu hiện có: {len(books)}")

    except Exception as e:
        print(f"Lỗi khởi tạo: {e}")

if __name__ == "__main__":
    db_init('LibrarySystemV2/src/database/schema.sql')
