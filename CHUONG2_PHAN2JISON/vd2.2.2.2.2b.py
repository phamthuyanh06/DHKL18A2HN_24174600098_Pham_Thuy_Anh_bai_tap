import json
# Đội tượng Python (đôi tượng dict)
data={
    "Ho va ten": "Nguyễn Văn A",
    "Nam sinh": 2025,
    "Gioi tinh": "Nam",
    "so_dt": "0123456789",
    "email": "nguyenvana@uneti.edu.vn"
}
#Sử dụng 'with open" để mà tệp thongtin.json" với chế độ ghi ('w') và mã hó #Ham json.dump() sẽ ghi đôi tượng Python trực tiếp vào tệp đã mở. f là biên
with open('thongtin.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
- print("Dữ Liệu đã được ghi thành công vào tập 'thongtin.json'.")
# open('thongtin.json', 'r', encoding='utf-8') as f: print("\n- Nội dung tệp 'thongtin.json')コ
# print(f.read())