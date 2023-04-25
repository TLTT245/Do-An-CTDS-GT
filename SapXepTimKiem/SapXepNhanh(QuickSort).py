def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
def create_array():
    n = int(input("Nhập số lượng phần tử của mảng: "))

    arr = []
    for i in range(n):
        value = int(input("Nhập giá trị cho phần tử thứ {}: ".format(i+1)))
        arr.append(value)
    return arr   
arr = create_array()
new_arr = quick_sort(arr) 
print('Mảng đã được xắp xếp là ',new_arr)