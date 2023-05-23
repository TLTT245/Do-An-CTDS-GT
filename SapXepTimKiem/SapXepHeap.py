# Hàm heap hóa cây tại index i của mảng đầu vào
# n là kích thước heap

def heapify(arr, n, i, ascending):
    swapper = i  # Gán biến giá trị lớn nhất/nhỏ nhất là i
    left = 2 * i + 1  # Nút bên trái = 2*i + 1
    right = 2 * i + 2  # Nút bên phải = 2*i + 2

    # Kiểm tra nếu nút con trái tồn tại và
    # lớn/nhỏ hơn nút gốc
    if ascending:
        if left < n and arr[i] < arr[left]:
            swapper = left
    else:
        if left < n and arr[i] > arr[left]:
            swapper = left

    # Kiểm tra nếu nút con phải tồn tại và
    # lớn/nhỏ hơn nút gốc
    if ascending:
        if right < n and arr[swapper] < arr[right]:
            swapper = right
    else:
        if right < n and arr[swapper] > arr[right]:
            swapper = right

    # Thay nút gốc nếu cần

    if swapper != i:
        (arr[i], arr[swapper]) = (arr[swapper], arr[i])  # Xáo
        print(arr)

        # Heap hóa cây

        heapify(arr, n, swapper, ascending)


# Sắp xếp heap sort
def heap_sort(arr, ascending):
    n = len(arr)
    # Xây một maxheap (nút cha có giá trị lớn hơn nút con)
    # Bắt đầu từ nút cha cuối cùng trong cây
    # Index cho nút cha của 1 nút con (n//2 - 1)
    print("Xây dựng.....")
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, ascending)

    # Lấy từng phần tử một
    print("Sắp xếp.....")
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # Xáo
        print(arr)
        heapify(arr, i, 0, ascending)


if __name__ == "__main__":
    n = abs(int(input("Nhap so phan tu n: ")))
    arr = []
    for i in range(n):
        x = int(input("Nhap phan tu thu " + str(i + 1) + ": "))
        arr.append(x)
    is_asc = input("Sap xep theo thu tu tang dan? (True/False): ")
    if is_asc == "True":
        heap_sort(arr, True)
    elif is_asc == "False":
        heap_sort(arr, False)