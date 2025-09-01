print( 7/2 ) # chia lấy kết quả thực
print(7//2) # chia lấy kết quả nguyên
print(7%2) # chia lấy phần dư   
print(7**2) # lũy thừa 7 mũ 2
print(True and True) #và trả về  true nếu cả hai vế đều true
print(True or False) # trả  về true nếu ít nhất một vế là true

# is
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)  # True  (vì giá trị giống nhau)
print(a is b)  # False (vì khác ô nhớ)
print(a is c)  # True  (vì cùng trỏ đến một list)