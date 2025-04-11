import os
import datetime

def main():
    # 先定義要寫入的資料夾名稱
    folder_name = "auto_gen"
    # 確保資料夾存在，若不存在就自動建立
    os.makedirs(folder_name, exist_ok=True)

    # 以當前時間做為檔名一部分，以避免重名
    now_str = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"auto-file-{now_str}.md"

    # 組出完整路徑：myfolder/auto-file-YYYYMMDD-HHMMSS.md
    file_path = os.path.join(folder_name, filename)

    # 寫入內容
    content = f"""# Example File

This file was generated at {datetime.datetime.now()}.
"""

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"File saved to: {file_path}")

if __name__ == "__main__":
    main()
