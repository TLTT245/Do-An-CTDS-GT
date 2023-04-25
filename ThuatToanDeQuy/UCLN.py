def USCLN(a, b):
    if b == 0:
        return a
    else:
        return USCLN(b, a % b) 
a = int(input(' Nhập a vào từ bàn phím ='))
b = int(input('Nhập b vào từ bàn phím =')) 
e = USCLN(a,b) 
print("USCLN CỦA {a} VÀ {b} LÀ :",e) 
     
        
