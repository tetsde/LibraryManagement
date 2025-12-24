from database import DataManager
import config


class SachGiay:
    
    def __init__(self, ten, so_luong, loai_sach, link_tai):
        self.ten = ten
        self.so_luong = so_luong
        self.loai_sach = loai_sach
        self.link_tai = link_tai
    
    def muon_sach(self):
        db = DataManager(config.DATABASE_PATH)
        query = "UPDATE sach SET so_luong = so_luong - 1 WHERE ten = ?"
        db.thuc_thi(query, (self.ten,))
        print(f"Mượn sách giấy '{self.ten}' thành công")
    
    def them_sach(self):
        db = DataManager(config.DATABASE_PATH)
        query = "INSERT INTO sach (ten, loai_sach, so_luong) VALUES (?, ?, ?)"
        db.thuc_thi(query, (self.ten, self.loai_sach, self.so_luong))
        print(f"Đã thêm sách giấy '{self.ten}' vào hệ thống")


class Ebook(SachGiay):
    
    def __init__(self, ten, so_luong, loai_sach, link_tai):
        super().__init__(ten, so_luong, loai_sach, link_tai)
        self.link_tai = link_tai
    
    def muon_sach(self):
        db = DataManager(config.DATABASE_PATH)
        query = "SELECT link_tai FROM sach WHERE ten = ?"
        result = db.thuc_thi(query, (self.ten,))
        print(f"Mượn Ebook thành công! Link tải '{self.ten}': {result}")
    
    def them_sach(self):
        db = DataManager(config.DATABASE_PATH)
        query = "INSERT INTO sach (ten, so_luong, loai_sach, link_tai) VALUES (?, ?, ?, ?)"
        db.thuc_thi(query, (self.ten, self.so_luong, self.loai_sach, self.link_tai))
        print(f"Đã thêm Ebook '{self.ten}' vào hệ thống")


