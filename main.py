import tkinter as tk
from tkinter import messagebox, ttk
import database as db
import model
import utils
import config


class LibraryApps:
    
    def __init__(self, root):
        self.root = root
        self.root.title(config.WINDOW_TITLE)
        self.root.geometry(config.WINDOW_SIZE)
        self.root.configure(bg='#ecf0f1')
        
        self.manager = db.DataManager(config.DATABASE_PATH)
        self._tao_giao_dien()
    
    def _tao_giao_dien(self):
        header_frame = tk.Frame(self.root, bg=config.MAIN_COLOR, height=80)
        header_frame.pack(fill='x', pady=(0, 20))
        
        tk.Label(
            header_frame,
            text="QUẢN LÝ THƯ VIỆN",
            font=(config.FONT_FAMILY, 20, 'bold'),
            bg=config.MAIN_COLOR,
            fg='white',
            pady=20
        ).pack()
        
        content_frame = tk.Frame(self.root, bg='#ecf0f1')
        content_frame.pack(padx=40, pady=10, fill='both', expand=True)
        
        self._tao_form_nhap_lieu(content_frame)
        self._tao_buttons(content_frame)
    
    def _tao_form_nhap_lieu(self, parent):
        form_frame = tk.Frame(parent, bg='white', relief='raised', bd=2)
        form_frame.pack(fill='x', pady=10, padx=10)
        
        form_inner = tk.Frame(form_frame, bg='white')
        form_inner.pack(padx=20, pady=20, fill='both', expand=True)
        
        tk.Label(
            form_inner,
            text="Tên sách:",
            font=(config.FONT_FAMILY, 11, 'bold'),
            bg='white',
            fg=config.MAIN_COLOR
        ).grid(row=0, column=0, sticky='w', pady=8)
        
        self.ent_ten = tk.Entry(
            form_inner,
            font=(config.FONT_FAMILY, 10),
            width=40,
            relief='solid',
            bd=1
        )
        self.ent_ten.grid(row=0, column=1, pady=8, padx=10, sticky='ew')
        
        tk.Label(
            form_inner,
            text="Số lượng:",
            font=(config.FONT_FAMILY, 11, 'bold'),
            bg='white',
            fg=config.MAIN_COLOR
        ).grid(row=1, column=0, sticky='w', pady=8)
        
        self.ent_so_luong = tk.Entry(
            form_inner,
            font=(config.FONT_FAMILY, 10),
            width=40,
            relief='solid',
            bd=1
        )
        self.ent_so_luong.grid(row=1, column=1, pady=8, padx=10, sticky='ew')
        self.ent_so_luong.insert(0, "0")
        
        tk.Label(
            form_inner,
            text="Loại tài liệu:",
            font=(config.FONT_FAMILY, 11, 'bold'),
            bg='white',
            fg=config.MAIN_COLOR
        ).grid(row=2, column=0, sticky='w', pady=8)
        
        self.cbo_loai = ttk.Combobox(
            form_inner,
            values=["Sách Giấy", "Ebook"],
            font=(config.FONT_FAMILY, 10),
            width=38,
            state='readonly'
        )
        self.cbo_loai.grid(row=2, column=1, pady=8, padx=10, sticky='ew')
        self.cbo_loai.bind('<<ComboboxSelected>>', self._on_loai_changed)
        
        tk.Label(
            form_inner,
            text="Link tải (Ebook):",
            font=(config.FONT_FAMILY, 11, 'bold'),
            bg='white',
            fg=config.MAIN_COLOR
        ).grid(row=3, column=0, sticky='w', pady=8)
        
        self.ent_link_tai = tk.Entry(
            form_inner,
            font=(config.FONT_FAMILY, 10),
            width=40,
            relief='solid',
            bd=1,
            state='disabled'
        )
        self.ent_link_tai.grid(row=3, column=1, pady=8, padx=10, sticky='ew')
        
        form_inner.columnconfigure(1, weight=1)
    
    def _on_loai_changed(self, event=None):
        loai = self.cbo_loai.get()
        if loai == "Ebook":
            self.ent_link_tai.config(state='normal')
            self.ent_so_luong.delete(0, tk.END)
            self.ent_so_luong.insert(0, "0")
            self.ent_so_luong.config(state='disabled')
        else:
            self.ent_link_tai.config(state='disabled')
            self.ent_so_luong.config(state='normal')
    
    def _tao_buttons(self, parent):
        btn_frame = tk.Frame(parent, bg='#ecf0f1')
        btn_frame.pack(pady=20)
        
        btn_style = {
            'font': (config.FONT_FAMILY, 10, 'bold'),
            'width': 18,
            'height': 2,
            'relief': 'raised',
            'bd': 0,
            'cursor': 'hand2'
        }
        
        btn_them = tk.Button(
            btn_frame,
            text="Thêm Tài Liệu",
            bg=config.SUCCESS_COLOR,
            fg='white',
            command=self.handle_add,
            **btn_style
        )
        btn_them.grid(row=0, column=0, padx=8, pady=5)
        
        btn_excel = tk.Button(
            btn_frame,
            text="Xuất Excel",
            bg=config.ACCENT_COLOR,
            fg='white',
            command=self.handle_excel,
            **btn_style
        )
        btn_excel.grid(row=0, column=1, padx=8, pady=5)
        
        btn_chart = tk.Button(
            btn_frame,
            text="Xem Biểu Đồ",
            bg='#9b59b6',
            fg='white',
            command=self.handle_chart,
            **btn_style
        )
        btn_chart.grid(row=0, column=2, padx=8, pady=5)
        
        btn_list = tk.Button(
            btn_frame,
            text="Danh Sách",
            bg='#34495e',
            fg='white',
            command=self.hien_thi_danh_sach_sach,
            **btn_style
        )
        btn_list.grid(row=1, column=0, columnspan=3, padx=8, pady=5, sticky='ew')
    
    def _validate_input(self):
        ten = self.ent_ten.get().strip()
        loai = self.cbo_loai.get()
        
        if not ten:
            messagebox.showwarning("Lỗi", "Vui lòng nhập tên sách!")
            return False
        
        if not loai:
            messagebox.showwarning("Lỗi", "Vui lòng chọn loại tài liệu!")
            return False
        
        if loai == "Sách Giấy":
            try:
                sl = int(self.ent_so_luong.get())
                if sl < 0:
                    messagebox.showwarning("Lỗi", "Số lượng phải là số dương!")
                    return False
            except ValueError:
                messagebox.showwarning("Lỗi", "Số lượng phải là số nguyên!")
                return False
        
        if loai == "Ebook":
            link = self.ent_link_tai.get().strip()
            if not link:
                messagebox.showwarning("Lỗi", "Vui lòng nhập link tải cho Ebook!")
                return False
        
        return True
    
    def handle_add(self):
        if not self._validate_input():
            return
        
        ten = self.ent_ten.get().strip()
        loai = self.cbo_loai.get()
        
        try:
            if loai == "Ebook":
                duong_dan = self.ent_link_tai.get().strip()
                obj = model.Ebook(
                    ten=ten,
                    so_luong=0,
                    loai_sach=loai,
                    link_tai=duong_dan
                )
            else:
                sl = int(self.ent_so_luong.get())
                obj = model.SachGiay(
                    ten=ten,
                    so_luong=sl,
                    loai_sach=loai,
                    link_tai=None
                )
            
            obj.them_sach()
            messagebox.showinfo(
                "Thành công",
                f"Đã thêm '{ten}' vào thư viện!"
            )
            
            self._clear_form()
            
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể thêm tài liệu: {str(e)}")
    
    def _clear_form(self):
        self.ent_ten.delete(0, tk.END)
        self.ent_so_luong.config(state='normal')
        self.ent_so_luong.delete(0, tk.END)
        self.ent_so_luong.insert(0, "0")
        self.ent_link_tai.delete(0, tk.END)
        self.cbo_loai.set('')
        self.ent_link_tai.config(state='disabled')
    
    def hien_thi_danh_sach_sach(self):
        data = self.manager.lay_tat_ca_sach()
        if not data:
            messagebox.showinfo("Thông báo", "Thư viện hiện đang trống!")
            return
        
        print("\n" + "="*60)
        print("DANH SÁCH TÀI LIỆU TRONG THƯ VIỆN")
        print("="*60)
        for idx, item in enumerate(data, 1):
            if item['loai_sach'] == "Ebook":
                obj = model.Ebook(
                    item['ten'],
                    item['so_luong'],
                    item['loai_sach'],
                    item['link_tai']
                )
                print(f"{idx}. [{obj.loai_sach}] {obj.ten}")
                print(f"   Link: {obj.link_tai}")
            else:
                obj = model.SachGiay(
                    item['ten'],
                    item['so_luong'],
                    item['loai_sach'],
                    item['link_tai']
                )
                print(f"{idx}. [{obj.loai_sach}] {obj.ten} - Số lượng: {obj.so_luong}")
        print("="*60 + "\n")
        
        messagebox.showinfo(
            "Thông báo",
            f"Có {len(data)} tài liệu. Xem chi tiết trong console!"
        )
    
    def handle_excel(self):
        data = self.manager.lay_tat_ca_sach()
        if not data:
            messagebox.showwarning("Thông báo", "Không có dữ liệu để xuất Excel!")
            return
        
        filename = "danh_sach_sach.xlsx"
        success = utils.xuat_bao_cao_excel(data, filename)
        
        if success:
            messagebox.showinfo(
                "Thành công",
                f"Đã xuất file Excel: {filename}"
            )
        else:
            messagebox.showerror("Lỗi", "Không thể xuất file Excel!")
    
    def handle_chart(self):
        data = self.manager.lay_tat_ca_sach()
        if not data:
            messagebox.showwarning(
                "Thông báo",
                "Không có dữ liệu để tạo biểu đồ!"
            )
            return
        
        try:
            utils.truc_quan_hoa(data)
        except Exception as e:
            messagebox.showerror("Lỗi", f"Không thể tạo biểu đồ: {str(e)}")


def main():
    root = tk.Tk()
    app = LibraryApps(root)
    root.mainloop()


if __name__ == "__main__":
    main()