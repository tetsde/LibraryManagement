# Hệ thống Quản lý Thư viện 📚

Ứng dụng quản lý thư viện đơn giản sử dụng Python và Tkinter GUI.

## ✨ Tính năng

- ➕ **Thêm tài liệu**: Thêm sách giấy và ebook vào thư viện
- 📊 **Xuất báo cáo Excel**: Xuất danh sách tài liệu ra file Excel
- 📈 **Biểu đồ thống kê**: Hiển thị biểu đồ tròn thống kê tỷ lệ các loại tài liệu
- 📋 **Xem danh sách**: Hiển thị danh sách tất cả tài liệu trong thư viện

## 🚀 Cài đặt

### Yêu cầu hệ thống

- Python 3.7 trở lên
- pip (Python package installer)

### Các bước cài đặt

1. **Clone repository**

```bash
git clone https://github.com/your-username/StudentManagement.git
cd StudentManagement
```

2. **Cài đặt các thư viện cần thiết**

```bash
pip install -r requirements.txt
```

## 📖 Hướng dẫn sử dụng

### Chạy ứng dụng

```bash
python main.py
```

### Sử dụng giao diện

1. **Thêm sách giấy**:
   - Nhập tên sách
   - Nhập số lượng
   - Chọn "Sách Giấy" trong dropdown
   - Click "Thêm Tài Liệu"

2. **Thêm Ebook**:
   - Nhập tên sách
   - Chọn "Ebook" trong dropdown
   - Nhập link tải
   - Click "Thêm Tài Liệu"

3. **Xuất báo cáo Excel**:
   - Click "Xuất Excel"
   - File `danh_sach_sach.xlsx` sẽ được tạo trong thư mục hiện tại

4. **Xem biểu đồ**:
   - Click "Xem Biểu Đồ"
   - Biểu đồ tròn sẽ hiển thị tỷ lệ các loại tài liệu

5. **Xem danh sách**:
   - Click "Danh Sách"
   - Danh sách chi tiết sẽ được in ra console

## 📁 Cấu trúc thư mục

```
StudentManagement/
│
├── main.py              # File chính chạy ứng dụng
├── config.py            # File cấu hình
├── database.py          # Module quản lý database
├── model.py             # Module định nghĩa các class model
├── utils.py             # Module chứa các hàm tiện ích
│
├── database/            # Thư mục chứa database
│   └── book.db          # SQLite database (tạo tự động)
│
├── requirements.txt     # Danh sách thư viện cần thiết
├── README.md            # File hướng dẫn
├── LICENSE              # Giấy phép
└── .gitignore          # File gitignore
```

## 🛠️ Công nghệ sử dụng

- **Python 3**: Ngôn ngữ lập trình chính
- **Tkinter**: Thư viện GUI
- **SQLite3**: Database để lưu trữ dữ liệu
- **Pandas**: Xử lý và xuất dữ liệu Excel
- **Matplotlib**: Tạo biểu đồ thống kê
- **openpyxl**: Hỗ trợ xuất file Excel

## 📝 Database Schema

```sql
CREATE TABLE sach (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ten TEXT NOT NULL,
    so_luong INTEGER DEFAULT 0,
    loai_sach TEXT NOT NULL,
    link_tai TEXT
);
```

## 🎨 Giao diện

Ứng dụng có giao diện thân thiện với người dùng:
- Header màu xanh đậm chuyên nghiệp
- Form nhập liệu rõ ràng, dễ sử dụng
- Các nút chức năng có icon và màu sắc phân biệt
- Tự động validate input
- Thông báo lỗi và thành công rõ ràng

## 🤝 Đóng góp

Nếu bạn muốn đóng góp cho dự án:

1. Fork repository
2. Tạo branch mới (`git checkout -b feature/AmazingFeature`)
3. Commit thay đổi (`git commit -m 'Add some AmazingFeature'`)
4. Push lên branch (`git push origin feature/AmazingFeature`)
5. Tạo Pull Request

## 📄 Giấy phép

Dự án này được phân phối dưới giấy phép MIT. Xem file `LICENSE` để biết thêm chi tiết.

## 👨‍💻 Tác giả

**Tong Phuoc Hoai Nam**

- GitHub: [@tetsde](https://github.com/tetsde)

## 📞 Liên hệ

Nếu bạn có câu hỏi hoặc góp ý, vui lòng tạo issue trên GitHub hoặc liên hệ qua email.

---

⭐ Nếu bạn thấy dự án hữu ích, hãy cho một star nhé! ⭐
