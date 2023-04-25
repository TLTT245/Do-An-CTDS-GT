def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def create_array():
    n = int(input("Nhập số lượng phần tử của mảng: "))

    arr = []
    for i in range(n):
        value = int(input("Nhập giá trị cho phần tử thứ {}: ".format(i+1)))
        arr.append(value)

    return arr
arr = create_array()
insertion_sort(arr)
print("Mảng đã sắp xếp: ", arr)
# Đầu tiên, ta định nghĩa hàm insertion_sort(arr) nhận vào một mảng arr là danh sách các số nguyên cần được sắp xếp. 
# Trong hàm, ta sử dụng vòng lặp for để duyệt qua từng phần tử của mảng, bắt đầu từ phần tử thứ hai, bởi vì danh sách đã sắp xếp ban đầu chỉ có một phần tử và ta coi nó đã được sắp xếp.
# Ở mỗi bước, ta lấy giá trị của phần tử hiện tại làm key và so sánh nó với các phần tử trong danh sách đã sắp xếp. 
# Nếu key nhỏ hơn một phần tử trong danh sách đã sắp xếp, ta di chuyển phần tử đó lên một vị trí và tiếp tục so sánh key với phần tử trước đó. 
# Nếu key không nhỏ hơn bất kỳ phần tử nào trong danh sách đã sắp xếp, ta chèn key vào vị trí đúng trong danh sách.
# Sau khi hoàn thành vòng lặp for, danh sách đã được sắp xếp và được lưu trữ trong biến arr. Ta sử dụng hàm print() để in ra mảng đã sắp xếp. Kết quả đầu ra của chương trình là:
