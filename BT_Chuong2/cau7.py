'''
# Nhập một giá trị (chuỗi)
name = input("Nhập tên của bạn: ")
# In ra giá trị đã nhập
print("Xin chào,", name)

# Nhập một số nguyên
age = int(input("Nhập tuổi của bạn: "))
# In ra tuổi đã nhập
print("Bạn", age, "tuổi.")

# Nhập một số thực
height = float(input("Nhập chiều cao của bạn (m): "))   
# In ra chiều cao đã nhập
print("Chiều cao của bạn là:", height, "m")

# Nhap nhhieu gia tri tren mot  dong
a, b = input("Nhập hai số cách nhau bởi dấu cách: ").split()
print("Ban đã nhập:", a, b)
# mac dinh a, b la  chuoi
# Chuyen doi kieu du lieu   
a,b = map(int, input("Nhap hai so nguyen:").split())
print("Tong hai so la:", a + b)

# nhap danh sach nhieu phan tu
num = list(map(int, input("Nhap danh sach so nguyen cach nhau boi dau cach:").split()))
print("Danh sach ban vua nhap la:", num)
'''