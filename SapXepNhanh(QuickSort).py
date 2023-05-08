3
def quick_sort(arr, ascending=True):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        if ascending:
            return quick_sort(less, ascending=True) + [pivot] + quick_sort(greater, ascending=True)
        else:
            return quick_sort(greater, ascending=False) + [pivot] + quick_sort(less, ascending=False)

def create_array():
    n = int(input("Nhập số lượng phần tử của mảng: "))

    arr = []
    for i in range(n):
        value = int(input("Nhập giá trị cho phần tử thứ {}: ".format(i+1)))
        arr.append(value)
    return arr  

# Sử dụng hàm create_array để tạo mảng và nhập giá trị cho biến ascending
arr = create_array()
ascending = input("Sắp xếp tăng hay giảm? (True/False): ")
if ascending.lower() == "true":
    ascending = True
else:
    ascending = False
# Sử dụng hàm quick_sort để sắp xếp mảng với thứ tự tăng/giảm dần tùy thuộc vào biến ascending
sorted_arr = quick_sort(arr, ascending=ascending)
# In kết quả sắp xếp
print("Mảng đã sắp xếp:", sorted_arr)

        