# Sắp xếp chọn sắp xếp các phần tử trong mảng bằng việc tìm số nhỏ nhất trong mảng chưa sắp xếp
# và đưa về vị trí đầu tiên. Lặp đi lặp lại cho đến khi sắp xếp xong.

def selection_sort(array, ascending):
    for ind in range(len(array)):
        min_index = ind  # Gán min_index cho index của phần tử đang kiểm tra hiện tại
        for j in range(ind + 1, len(array)):  # Duyệt từ phần tử hiện tại đến hết danh sách
            if ascending is True:  # Sắp xếp tăng dần
                if array[j] < array[min_index]:  # Nếu tìm được giá trị nhỏ hơn giá trị ở min_index
                    min_index = j   # Gán min_index là index của phần tử đó
            else:   # Tương tự ngược lại
                if array[j] > array[min_index]:
                    min_index = j
        array[ind], array[min_index] = array[min_index], array[ind]  # Thay đổi vị trí 2 phần tử
        print("Buoc", ind + 1, ":", array)  # In từng bước


if __name__ == "__main__":
    n = abs(int(input("Nhập số phần tử của array  ")))
    arr = []
    for i in range(n):
        x = int(input("Nhập phần tử thứ " + str(i + 1) + ": "))
        arr.append(x)
    is_asc = input("Sắp xếp theo thứ tự tăng dần ( True - > Tăng dần, False -> Giảm dần ): ")
    if is_asc == "True":
       selection_sort(arr, True)
    elif is_asc == "False":
       selection_sort(arr, False)


