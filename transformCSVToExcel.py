import os
import pandas as pd
from datetime import datetime

def convert_excel_to_csv(excel_folder, csv_folder):
    # 檢查 CSV 資料夾是否存在，如果不存在則創建它
    if not os.path.exists(csv_folder):
        os.makedirs(csv_folder)

    # 取得 Excel 資料夾下所有的檔案名稱
    excel_files = [f for f in os.listdir(excel_folder) if f.endswith('.xlsx')]

    # 將每個 Excel 檔案轉換成 CSV
    for excel_file in excel_files:
        excel_path = os.path.join(excel_folder, excel_file)
        csv_file = os.path.splitext(excel_file)[0] + '.csv'
        csv_path = os.path.join(csv_folder, csv_file)

        # 讀取 Excel 檔案，保留原始資料型態
        df = pd.read_excel(excel_path, dtype='object')

        # 將 DataFrame 存為 CSV 檔案，不包含索引列
        df.to_csv(csv_path, index=False)

def merge_csv_files(csv_folder, output_csv):
    # 取得 CSV 資料夾下所有的檔案名稱
    csv_files = [f for f in os.listdir(csv_folder) if f.endswith('.csv')]

    # 合併所有 CSV 檔案
    merged_df = pd.concat([pd.read_csv(os.path.join(csv_folder, f), dtype='object') for f in csv_files], ignore_index=True)

    # 將合併後的結果存為 CSV 檔案，不包含索引列
    merged_df.to_csv(output_csv, index=False)

def convert_csv_to_excel(input_csv, output_excel):
    # 讀取合併後的 CSV 檔案，保留原始資料型態
    df = pd.read_csv(input_csv, dtype='object')

    # 將資料轉換回 Excel 格式，不包含索引列
    df.to_excel(output_excel, index=False)

if __name__ == "__main__":
    # 輸入資料夾和輸出檔案名稱
    excel_folder = "C:\\Users\\Modern 14\\Desktop\\excel"
    csv_folder = "C:\\Users\\Modern 14\\Desktop\\csv"
    
    # 取得當天日期並以格式範例 "20230807" 命名檔案
    current_date = datetime.now().strftime("%Y%m%d")
    merged_csv = f"C:\\Users\\Modern 14\\Desktop\\merged_{current_date}.csv"
    output_excel = f"C:\\Users\\Modern 14\\Desktop\\merged_{current_date}.xlsx"

    # 執行 Excel 轉換成 CSV 的功能
    convert_excel_to_csv(excel_folder, csv_folder)

    # 執行合併所有 CSV 檔案的功能
    merge_csv_files(csv_folder, merged_csv)

    # 執行 CSV 轉換成 Excel 的功能
    convert_csv_to_excel(merged_csv, output_excel)
