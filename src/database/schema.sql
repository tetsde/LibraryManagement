------------KHỞI TẠO DỮ LIỆU----------------------

CREATE TABLE IF NOT EXISTS the_loai (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ten_loai TEXT NOT NULL UNIQUE
);

CREATE TABLE IF NOT EXISTS sach (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ten_sach TEXT NOT NULL,
    tac_gia TEXT,
    so_luong_tong INTEGER DEFAULT 0 CHECK (so_luong_tong >= 0), 
    the_loai_id INTEGER,
    link_tai TEXT,
    ngay_nhap TEXT DEFAULT (DATE('now')), 
    FOREIGN KEY (the_loai_id) REFERENCES the_loai(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS doc_gia (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ten_doc_gia TEXT NOT NULL,
    so_dien_thoai TEXT,
    ngay_tham_gia TEXT DEFAULT (DATE('now'))
);

CREATE TABLE IF NOT EXISTS muon_tra (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sach_id INTEGER NOT NULL,
    doc_gia_id INTEGER NOT NULL,
    ngay_muon TEXT DEFAULT (DATE('now')),
    ngay_tra_du_kien TEXT NOT NULL,
    ngay_tra_thuc_te TEXT, 
    trang_thai TEXT DEFAULT 'DangMuon', 
    ghi_chu TEXT,
    FOREIGN KEY (sach_id) REFERENCES sach(id),
    FOREIGN KEY (doc_gia_id) REFERENCES doc_gia(id)
);

----------SAMPLE DATA (DỮ LIỆU MẪU)----------------
-- 1. Thêm thể loại 
INSERT OR IGNORE INTO the_loai (ten_loai) VALUES
('Công nghệ thông tin'),
('Tiểu thuyết'),
('Ngôn tình');

-- 2. Thêm sách 
INSERT OR IGNORE INTO sach (ten_sach, tac_gia, so_luong_tong, the_loai_id, ngay_nhap) VALUES
('Python Developer', 'Hoài Nam', 10, 1, DATE('now'));

-- 3. Thêm độc giả
INSERT OR IGNORE INTO doc_gia (ten_doc_gia, so_dien_thoai) VALUES
('Nguyễn Văn A', '0858459934');

-- 4. Thêm mượn trả
INSERT OR IGNORE INTO muon_tra (sach_id, doc_gia_id, ngay_muon, ngay_tra_du_kien, trang_thai, ghi_chu) VALUES
(1, 1, DATE('now'), DATE('now', '+7 days'), 'DangMuon', 'Mượn về học code');
