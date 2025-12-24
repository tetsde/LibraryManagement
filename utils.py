import pandas as pd
import matplotlib.pyplot as plt


def xuat_bao_cao_excel(data_list, filename="baocaothuvien.xlsx"):
    if not data_list:
        return False
    
    try:
        df = pd.DataFrame(data_list)
        df.to_excel(filename, index=False, engine='openpyxl')
        return True
    except Exception as e:
        print(f"Lỗi khi xuất Excel: {e}")
        return False


def truc_quan_hoa(data_list):
    if not data_list:
        return
    
    try:
        df = pd.DataFrame(data_list)
        thong_ke = df['loai_sach'].value_counts()
        
        plt.rcParams['font.family'] = 'DejaVu Sans'
        
        plt.figure(figsize=(8, 8))
        colors = ['#3498db', '#e74c3c', '#2ecc71', '#f39c12']
        thong_ke.plot(
            kind='pie',
            autopct='%1.1f%%',
            startangle=140,
            colors=colors[:len(thong_ke)]
        )
        
        plt.title("Tỷ lệ các loại tài liệu trong thư viện", fontsize=14, fontweight='bold')
        plt.ylabel("")
        plt.tight_layout()
        plt.show()
    except Exception as e:
        print(f"Lỗi khi tạo biểu đồ: {e}")