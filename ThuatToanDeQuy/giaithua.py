def giai_thua(n):
    if n == 0:
        return 1
    else:
        return n * giai_thua(n-1)
n = int(input('Nhập n vào từ bàn phím :'))    
print(giai_thua(n))