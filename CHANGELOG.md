# Changelog

Tất cả các thay đổi đáng chú ý của dự án sẽ được ghi lại trong file này.

Định dạng dựa trên [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
và dự án này tuân theo [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0] - 2026-01-10

### 🎉 Major Release - Hoàn toàn tái thiết kế

#### Added (Tính năng mới)
- ✨ **Streamlit Web Interface**: Giao diện web hiện đại thay thế Tkinter
- 👥 **Quản lý Độc giả**: Module quản lý độc giả hoàn chỉnh
  - Thêm độc giả mới với tên và SĐT
  - Tìm kiếm độc giả theo tên/SĐT
  - Xem danh sách tất cả độc giả
  - Xóa độc giả
- 📖 **Quản lý Mượn/Trả**: Hệ thống mượn trả sách
  - Cho mượn sách với tự động đặt hạn trả (7 ngày)
  - Trả sách và cập nhật trạng thái
  - Theo dõi trạng thái: Đang mượn, Đã trả, Quá hạn
  - Xem danh sách giao dịch mượn/trả
- 📊 **Dashboard Analytics**: Bảng điều khiển phân tích
  - Thống kê tổng quan: Tổng sách, Tổng độc giả, Đang mượn
  - Biểu đồ phân bổ sách theo thể loại (Pie Chart)
  - Biểu đồ trạng thái mượn sách (Pie Chart)
  - Xu hướng mượn trả theo tháng (Line Chart)
  - Top 5 sách được mượn nhiều nhất (Bar Chart)
  - Top 10 độc giả tích cực nhất (Bar Chart)
- 📈 **Interactive Charts**: Biểu đồ Plotly tương tác
  - Zoom, pan, hover tooltips
  - Export to PNG
  - Responsive design
- 🗄️ **Relational Database**: SQLite với Foreign Keys
  - Bảng `the_loai`: Quản lý thể loại sách
  - Bảng `sach`: Thông tin sách với foreign key
  - Bảng `doc_gia`: Thông tin độc giả
  - Bảng `muon_tra`: Giao dịch mượn/trả với constraints
- 📑 **Advanced Reports**: Báo cáo nâng cao
  - Danh sách sách quá hạn
  - Nhật ký hoạt động đầy đủ
  - Xuất báo cáo Excel
- 🎨 **Modern UI/UX**: Thiết kế giao diện chuyên nghiệp
  - Sidebar navigation
  - Tabs organization
  - Custom CSS styling
  - Responsive layout

#### Changed (Thay đổi)
- 🏗️ **Architecture**: Chuyển từ monolithic sang MVC pattern
  - Tách biệt Models, Views, Controllers
  - Modularity cao với 8+ files
  - Dễ bảo trì và mở rộng
- 🎨 **UI Framework**: Tkinter → Streamlit
  - Desktop app → Web app
  - Truy cập từ browser
  - Multi-platform support
- 📊 **Charts Library**: Matplotlib → Plotly
  - Static charts → Interactive charts
  - Better visualization
  - Export capabilities
- 🏷️ **Book Categories**: Đơn giản hóa → Linh hoạt
  - "Sách Giấy/Ebook" → Thể loại tùy chỉnh
  - Dynamic category management
  - Scalable structure
- 📚 **Book Management**: Enhanced CRUD operations
  - Thêm tính năng cập nhật sách
  - Tìm kiếm thông minh hơn
  - Validation tốt hơn

#### Improved (Cải tiến)
- 🔍 **Search Functionality**: Tìm kiếm thông minh hơn
  - Tìm kiếm theo nhiều trường
  - Kết quả hiển thị dạng bảng
  - Real-time search
- 💾 **Database Management**: Cấu trúc database tốt hơn
  - Foreign key constraints
  - Data integrity
  - Better normalization
- 📝 **Code Quality**: Cấu trúc code tốt hơn
  - Separation of concerns
  - Reusable components
  - Better error handling
  - Type hints consideration

#### Technical Details
- 🐍 Python 3.7+ compatibility
- 📦 New dependencies:
  - streamlit 1.52.2
  - plotly 6.5.1
  - pandas 2.3.3
  - openpyxl 3.1.2
  - python-dotenv 1.0.0

---

## [1.0.0] - 2024-12-XX

### Initial Release (Phiên bản đầu tiên)

#### Added
- ➕ Quản lý sách cơ bản
  - Thêm sách giấy và ebook
  - Xóa sách
  - Xem danh sách sách
- 📊 Xuất báo cáo Excel đơn giản
- 📈 Biểu đồ thống kê Matplotlib
  - Biểu đồ tròn phân loại sách
- 🖥️ Giao diện Tkinter Desktop
- 💾 SQLite database đơn giản
  - Bảng `sach` duy nhất

#### Technical Details
- 🐍 Python 3.7+
- 📦 Dependencies:
  - tkinter (built-in)
  - sqlite3 (built-in)
  - pandas
  - matplotlib
  - openpyxl

---

## Upcoming Changes (Sắp tới)

### [2.1.0] - Planned
- [ ] Authentication & Authorization
- [ ] User roles (Admin, Librarian, Member)
- [ ] Email notifications
- [ ] QR Code integration
- [ ] Multi-language support

### [3.0.0] - Future
- [ ] REST API with FastAPI
- [ ] Mobile application
- [ ] Cloud deployment
- [ ] AI/ML recommendations
- [ ] Advanced analytics

---

## Legend (Chú giải)

- **Added**: Tính năng mới
- **Changed**: Thay đổi trong tính năng hiện có
- **Deprecated**: Tính năng sắp bị loại bỏ
- **Removed**: Tính năng đã bị loại bỏ
- **Fixed**: Sửa lỗi
- **Security**: Bảo mật
- **Improved**: Cải tiến hiệu suất hoặc chất lượng
