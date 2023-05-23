# Sắp xếp trộn chia mảng ra làm 2 phần, rồi tiếp tục chia cho đến khi ta có một hỗn hợp mảng chỉ có 1 giá trị
# Sắp xếp từng cặp mảng lại với nhau theo đúng thứ tự, sau đó gộp lại dần. Tiếp tục như vậy cho đến khi có một mảng
# đầy đủ đã hoàn toàn được sắp xếp
# Người ta gọi phương pháp này là chia để trị (divide to conquer)

# Hàm merge gộp hai mảng con lại thành 1 mảng lớn hơn
# Mảng con một có dạng [l .. m]
# Mảng con hai có dạng [m + 1 .. r]
def merge(arr, l, m, r, ascending):
    # Xác định kích thước của hai mảng con
    n1 = m - l + 1
    n2 = r - m

    # Tạo hai mảng con tạm thời
    L = [0] * n1
    R = [0] * n2

    # Copy dữ liệu vào trong hai mảng con này
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Phần sau sẽ gộp hai mảng con này thành 1 mảng lớn hơn
    i = 0  # Index khởi đầu mảng con 1
    j = 0  # Index khởi đầu mảng con 2
    k = l  # Index khởi đầu mảng gộp

    # 1. Kiểm tra nếu index nhỏ hơn kích thước mảng, nếu chưa thì tiến hành sắp xếp
    # 2. Kiểm tra nếu phần tử index i của mảng 1 nhỏ/lớn hơn hoặc bằng phần tử index j của mảng 2:
    # + Nếu đúng thì cho phần tử i vào mảng gộp và tăng i lên 1
    # + Nếu sai thì cho phần tử j vào mảng gộp và tăng j lên 1
    # 3. Tăng index k lên 1
    while i < n1 and j < n2:
        if ascending is True:
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
        else:
            if L[i] >= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
        k += 1

    # Copy các phần tử còn lại của mảng 1 vào mảng gộp nếu như index j vượt quá kích thước mảng 2
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Tương tự với trường hợp ngược lại
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

    print("---")
    print(arr)


# Hàm sắp xếp trộn:
# + Biến arr chỉ mảng cần sắp xếp
# + Biến l chỉ index nằm bên trái cùng của mảng
# + Biến r chỉ index nằm bên phải cùng của mảng
# + Biến ascending quyết định sắp xếp tăng dần hay giảm dần
def merge_sort(arr, l, r, ascending):
    # Nếu như mảng con chứa 2 phần tử trở lên (tức l < r), tiếp tục chia nhỏ ra
    if l < r:
        # Biến m chỉ index nằm chính giữa mảng, biến này giúp ta chia mảng thành 2 mảng con
        # Cho ra kết quả như (l + r) // 2 nhưng tránh tràn bộ nhớ với số quá lớn
        m = l + (r - l) // 2

        # Sắp xếp hai mảng con
        merge_sort(arr, l, m, ascending)
        merge_sort(arr, m + 1, r, ascending)
        # Gộp lại thành một mảng lớn
        merge(arr, l, m, r, ascending)


if __name__ == "__main__":
    n = abs(int(input("Nhap so phan tu n: ")))
    arr = []
    for i in range(n):
        x = int(input("Nhap phan tu thu " + str(i + 1) + ": "))
        arr.append(x)
    is_asc = input("Sap xep theo thu tu tang dan? (True/False): ")
    if is_asc == "True":
        merge_sort(arr, 0, n-1, True)
    elif is_asc == "False":
        merge_sort(arr, 0, n-1, False)