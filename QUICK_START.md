# ⚡ Quick Start Guide

Hướng dẫn khởi động nhanh cho người dùng mới.

## 🚀 Cài đặt và Chạy trong 3 Bước

### Bước 1: Clone và Di chuyển vào thư mục

```bash
git clone https://github.com/tetsde/LibrarySystemV2.git
cd LibrarySystemV2
```

### Bước 2: Cài đặt Dependencies

```bash
pip install -r requirements.txt
```

### Bước 3: Khởi tạo Database và Chạy

```bash
# Khởi tạo database
cd src
python init_db.py

# Tạo dữ liệu mẫu (tùy chọn)
python seeder.py

# Chạy ứng dụng
streamlit run gui.py
```

✅ **Xong!** Ứng dụng sẽ tự động mở tại `http://localhost:8501`

---

## 📝 Thử Nghiệm Nhanh

### 1. Thêm Sách Mới
1. Click **"Quản lý Sách"** trên sidebar
2. Tab **"Thêm sách"**
3. Nhập thông tin:
   - Tên sách: `Python Crash Course`
   - Tác giả: `Eric Matthes`
   - Số lượng: `5`
   - Thể loại: `Công nghệ thông tin`
4. Click **"Thêm sách"**

### 2. Thêm Độc Giả
1. Click **"Quản lý Độc giả"**
2. Nhập:
   - Tên: `Nguyễn Văn A`
   - SĐT: `0912345678`
3. Click **"Thêm độc giả"**

### 3. Cho Mượn Sách
1. Click **"Mượn Trả"**
2. Tab **"Cho mượn sách"**
3. Chọn sách và độc giả từ dropdown
4. Click **"Cho mượn"**

### 4. Xem Dashboard
1. Click **"Dashboard"**
2. Xem thống kê và biểu đồ

---

## 🆘 Gặp Vấn Đề?

### Lỗi: Module not found
```bash
pip install -r requirements.txt --upgrade
```

### Port 8501 đã được sử dụng
```bash
streamlit run src/gui.py --server.port 8502
```

### Database bị lỗi
```bash
# Xóa database cũ và tạo mới
rm data/library.db
cd src
python init_db.py
python seeder.py
```

---

## 📚 Tìm hiểu thêm

- Xem [README.md](README.md) để biết chi tiết đầy đủ
- Xem [Database Schema](README.md#-database-schema)
- Kiểm tra [Roadmap](README.md#-roadmap)

---

**Chúc bạn sử dụng vui vẻ! 🎉**
