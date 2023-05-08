# Sắp xếp chèn chạy lần lượt các phần tử ở mảng chưa sắp xếp và chèn vào trong mảng sắp xếp
# lặp đi lặp lại cho đến khi sắp xếp hết mảng

def insertion_sort(array, ascending):
    for i in range(1, len(array)):
        key = array[i]  # Gán key cho giá trị của phần tử đang kiểm tra
        j = i - 1   # Đặt biến chỉ index của phần tử nằm sau phần tử kiểm tra
        if ascending is True:   # Sắp xếp tăng dần
            # Kiểm tra nếu index j vẫn nằm sau phần tử kiểm tra (>=0)
            # và giá trị tại j lớn hơn giá trị key
            while j >= 0 and key < array[j]:
                # Đẩy số lên 1 index
                array[j+1] = array[j]
                # Trỏ đến số nằm sau
                j = j-1
            # Chèn key vào vị trí mới
            array[j+1] = key
        else:  # Tương tự ngược lại
            while j >= 0 and key > array[j]:
                array[j+1] = array[j]
                j = j-1
            array[j+1] = key
        print("Sắp xếp lần thứ ", i, ":", array)  # In bước


if __name__ == "__main__":
    n = abs(int(input("Nhập số phần tử của array  ")))
    arr = []
    for i in range(n):
        x = int(input("Nhập phần tử thứ " + str(i + 1) + ": "))
        arr.append(x)
    is_asc = input("Sắp xếp theo thứ tự tăng dần ( True - > Tăng dần, False -> Giảm dần ): ")
    if is_asc == "True":
        insertion_sort(arr, True)
    elif is_asc == "False":
        insertion_sort(arr, False)