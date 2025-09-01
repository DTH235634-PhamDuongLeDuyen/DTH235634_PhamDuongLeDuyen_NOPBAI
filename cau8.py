# Cac loi va cach xu ly
# cac loi
# Lỗi cú pháp
'''
Do viết sai cú pháp của Python.
Ví dụ:
print("Hello"  # thiếu dấu đóng ngoặc
Khi chạy sẽ báo SyntaxError.
'''
# Lỗi ngữ nghĩa 
'''
Chương trình chạy được nhưng kết quả sai do logic sai.
Ví dụ:
x = 5
y = 0
print(x / (y + 1))  # Ý muốn chia cho y nhưng cộng 1 bị sai logic
'''
# Lỗi thực thi 

'''
Xảy ra trong quá trình chạy, ví dụ: chia cho 0, truy cập phần tử không tồn tại.
Ví dụ:
a = [1, 2, 3]
print(a[5])  
'''

# Cách xử lý lỗi
'''
Dùng try – except để xử lý lỗi:
try:
    x = int(input("Nhập số: "))
    y = 10 / x
    print("Kết quả:", y)
except ZeroDivisionError:
    print("Lỗi: Không thể chia cho 0!")
except ValueError:
    print("Lỗi: Vui lòng nhập số nguyên!")
except Exception as e:
    print("Lỗi khác:", e)
try: chứa đoạn code có khả năng gây lỗi.
except: xử lý lỗi khi xảy ra.
except Exception as e: bắt mọi lỗi còn lại.
Có thể thêm else (chạy khi không có lỗi) và finally (luôn chạy, kể cả có lỗi).
Ví dụ:
try:
    f = open("data.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("Không tìm thấy file!")
finally:
    print("Hoàn tất xử lý.")
    '''