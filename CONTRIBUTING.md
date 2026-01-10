# Contributing to Library Management System V2

Cảm ơn bạn đã quan tâm đến việc đóng góp cho dự án! 🎉

## 🤝 Các Cách Đóng Góp

Có nhiều cách để đóng góp cho dự án:

1. 🐛 **Báo lỗi (Bug Reports)**
2. 💡 **Đề xuất tính năng (Feature Requests)**
3. 📝 **Cải thiện tài liệu (Documentation)**
4. 💻 **Viết code (Code Contributions)**
5. 🧪 **Viết tests**
6. 🎨 **Cải thiện UI/UX**

---

## 🐛 Báo Lỗi

### Trước khi báo lỗi:
- ✅ Kiểm tra [Issues](https://github.com/tetsde/LibrarySystemV2/issues) xem lỗi đã được báo chưa
- ✅ Đảm bảo bạn đang sử dụng phiên bản mới nhất
- ✅ Thử tái tạo lỗi để xác nhận

### Khi tạo Bug Report:
Sử dụng template sau:

```markdown
**Mô tả lỗi:**
Mô tả rõ ràng và ngắn gọn về lỗi.

**Các bước tái tạo:**
1. Vào '...'
2. Click vào '...'
3. Cuộn xuống '...'
4. Thấy lỗi

**Kết quả mong đợi:**
Mô tả bạn mong đợi điều gì xảy ra.

**Kết quả thực tế:**
Mô tả điều gì thực sự xảy ra.

**Screenshots:**
Nếu có thể, thêm screenshots.

**Môi trường:**
- OS: [e.g. macOS 12.0]
- Python version: [e.g. 3.9.7]
- Streamlit version: [e.g. 1.52.2]

**Thông tin bổ sung:**
Thêm bất kỳ thông tin nào khác về vấn đề.
```

---

## 💡 Đề Xuất Tính Năng

### Trước khi đề xuất:
- ✅ Kiểm tra [Roadmap](README.md#-roadmap)
- ✅ Xem [Issues](https://github.com/tetsde/LibrarySystemV2/issues) với label `enhancement`

### Khi tạo Feature Request:
```markdown
**Tính năng bạn muốn:**
Mô tả rõ ràng tính năng.

**Tại sao tính năng này hữu ích:**
Giải thích tại sao tính năng này nên được thêm vào.

**Giải pháp bạn đề xuất:**
Mô tả cách bạn muốn tính năng được implement.

**Các alternatives:**
Mô tả các giải pháp thay thế khác.
```

---

## 💻 Đóng Góp Code

### Setup Development Environment

1. **Fork repository**
   ```bash
   # Fork trên GitHub, sau đó clone
   git clone https://github.com/YOUR_USERNAME/LibrarySystemV2.git
   cd LibrarySystemV2
   ```

2. **Tạo virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   # hoặc
   venv\Scripts\activate  # Windows
   ```

3. **Cài đặt dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Tạo development branch**
   ```bash
   git checkout -b feature/ten-tinh-nang-moi
   # hoặc
   git checkout -b fix/sua-loi-abc
   ```

### Coding Guidelines

#### 1. Python Style Guide
- ✅ Tuân theo [PEP 8](https://pep8.org/)
- ✅ Sử dụng 4 spaces cho indentation
- ✅ Maximum line length: 100 characters
- ✅ Sử dụng meaningful variable names

#### 2. Code Organization
```python
# Imports order:
# 1. Standard library
import os
import sys

# 2. Third-party libraries
import streamlit as st
import pandas as pd

# 3. Local imports
from models.book import BookModel
from database.db_manager import DBManager
```

#### 3. Naming Conventions
- **Functions/Methods**: `snake_case`
  ```python
  def get_all_books():
      pass
  ```

- **Classes**: `PascalCase`
  ```python
  class BookModel:
      pass
  ```

- **Constants**: `UPPER_SNAKE_CASE`
  ```python
  MAX_LOAN_DAYS = 7
  DEFAULT_PORT = 8501
  ```

- **Variables**: `snake_case`
  ```python
  total_books = 100
  user_name = "John"
  ```

#### 4. Docstrings
Sử dụng Google-style docstrings:

```python
def add_book(self, title, author, quantity, category_id):
    """
    Thêm sách mới vào thư viện.
    
    Args:
        title (str): Tên sách
        author (str): Tác giả
        quantity (int): Số lượng sách
        category_id (int): ID thể loại
        
    Returns:
        bool: True nếu thêm thành công, False nếu thất bại
        
    Raises:
        ValueError: Nếu quantity < 0
    """
    if quantity < 0:
        raise ValueError("Số lượng phải >= 0")
    # Implementation
    return True
```

#### 5. Error Handling
```python
# Good ✅
try:
    result = self.db.execute(query)
except sqlite3.Error as e:
    print(f"Database error: {e}")
    return None

# Bad ❌
try:
    result = self.db.execute(query)
except:
    pass
```

#### 6. Comments
```python
# Good ✅ - Explain WHY, not WHAT
# Calculate loan due date (7 days from now) for library policy compliance
due_date = datetime.now() + timedelta(days=7)

# Bad ❌ - States the obvious
# Add 7 days to current date
due_date = datetime.now() + timedelta(days=7)
```

### Testing

Trước khi submit PR:
- ✅ Test manually tất cả tính năng bị ảnh hưởng
- ✅ Kiểm tra không có SQL injection vulnerabilities
- ✅ Test trên browser khác nhau (Chrome, Firefox, Safari)
- ✅ Test responsive design

### Commit Messages

Sử dụng conventional commits:

```bash
# Format:
<type>(<scope>): <subject>

# Types:
feat:     Tính năng mới
fix:      Sửa lỗi
docs:     Cập nhật documentation
style:    Formatting, missing semi colons, etc
refactor: Code refactoring
test:     Thêm tests
chore:    Cập nhật build tasks, package manager configs, etc

# Examples:
feat(book): add search by author functionality
fix(loan): resolve overdue calculation bug
docs(readme): update installation instructions
refactor(db): optimize query performance
```

### Pull Request Process

1. **Update documentation** nếu cần
   - README.md
   - CHANGELOG.md
   - Docstrings

2. **Test kỹ lưỡng**
   - Manual testing
   - Edge cases
   - Error scenarios

3. **Tạo Pull Request**
   ```markdown
   ## Mô tả
   Mô tả ngắn gọn về thay đổi.
   
   ## Loại thay đổi
   - [ ] Bug fix
   - [ ] New feature
   - [ ] Breaking change
   - [ ] Documentation update
   
   ## Checklist
   - [ ] Code follows style guidelines
   - [ ] Self-review completed
   - [ ] Documentation updated
   - [ ] Tested thoroughly
   - [ ] No breaking changes (or documented)
   ```

4. **Đợi review** và giải quyết feedback

5. **Merge** sau khi được approve

---

## 📝 Documentation Guidelines

### README Updates
- Cập nhật nếu thêm tính năng mới
- Thêm screenshots nếu thay đổi UI
- Cập nhật dependencies nếu thêm libraries

### Code Comments
- Comment cho logic phức tạp
- Explain WHY, not WHAT
- Sử dụng Tiếng Việt hoặc English consistently

### CHANGELOG
- Luôn cập nhật CHANGELOG.md
- Theo format [Keep a Changelog](https://keepachangelog.com/)

---

## 🎨 UI/UX Guidelines

### Streamlit Components
- Sử dụng sidebar cho navigation
- Tabs cho tổ chức nội dung
- Columns cho layout responsive
- Expanders cho content dài

### Color Scheme
- Primary: Blue (#0068C9)
- Success: Green (#28A745)
- Warning: Orange (#FFA500)
- Danger: Red (#DC3545)

### Typography
- Headers: Clear và descriptive
- Labels: Concise và meaningful
- Help text: When needed for clarity

---

## 🚀 Release Process

(Dành cho maintainers)

1. Update version in relevant files
2. Update CHANGELOG.md
3. Create release branch: `release/vX.Y.Z`
4. Test thoroughly
5. Create GitHub Release
6. Tag version: `vX.Y.Z`
7. Deploy (if applicable)

---

## 📞 Liên Hệ

- 📧 Email: hoainam@example.com
- 💬 GitHub Issues: [Create new issue](https://github.com/tetsde/LibrarySystemV2/issues)
- 🌐 GitHub Discussions: [Start discussion](https://github.com/tetsde/LibrarySystemV2/discussions)

---

## 📜 Code of Conduct

### Our Standards

✅ **Encouraged:**
- Respect và professionalism
- Constructive feedback
- Helping others
- Being open to feedback

❌ **Not Acceptable:**
- Harassment hoặc discrimination
- Trolling hoặc insulting comments
- Personal hoặc political attacks
- Public hoặc private harassment

### Enforcement

Vi phạm có thể dẫn đến:
1. Warning
2. Temporary ban
3. Permanent ban

---

## 🙏 Cảm Ơn

Cảm ơn tất cả contributors đã giúp dự án này tốt hơn! 🎉

Mọi đóng góp, dù lớn hay nhỏ, đều được đánh giá cao! ❤️
