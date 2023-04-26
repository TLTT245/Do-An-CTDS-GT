class Queue:
    # Khởi tạo queue bằng 1 list trống
    def __init__(self):
        self.queue = list()

    # Thêm phần tử mới bằng insert()
    def add(self, value):  # FI (First In)
        if value not in self.queue:
            # Dùng insert(0, giá trị) để đưa giá trị mới vào đầu list. Đẩy giá trị thêm vào trước đi lên
            # VD: Cho list = [2, 3, 4]. insert(0, 1) sẽ cho ra list = [1, 2, 3, 4]
            print("Đã thêm phần tử giá trị", value, "vào queue")
            self.queue.insert(0, value)
        else:
            print("Giá trị đã nằm trong queue!")

    # In queue
    def print_queue(self):
        print("Queue hiện tại:", self.queue)
        print("Kích thước của queue:", self.size())

    # Kích thước của queue
    def size(self):
        return len(self.queue)

    # Loại bỏ phần tử ở queue
    # Hàm pop() bỏ phần tử ở cuối list
    def remove(self):  # FO (First Out)
        if len(self.queue) > 0:
            print("Phần tử", self.queue[-1], "đã bị xóa khỏi queue")
            self.queue.pop()
        else:
            return "Queue không có phần tử nào"


if __name__ == "__main__":
    test_queue = Queue()
    # Bắt đầu bằng 1 giá trị bất kì
    first_val = input("Nhập một giá trị để bắt đầu queue: ")
    test_queue.add(first_val)
    finish = False
    # Tạo vòng lặp vĩnh cửu, chương trình chỉ kết thúc khi finish = True
    while finish is not True:
        print()
        # Đoạn mã nhập lệnh bằng số đơn giản
        # Kiểm tra nếu số người dùng nhập vào là hợp lệ:
        # + Nếu hợp lệ thì thực hiện 1 trong những lệnh liệt kê bên dưới
        # + Nếu không thì báo lỗi và cho người dùng nhập lại
        print("HELP: 1 - Thêm, 2 - In, 3 - Xóa, 4 - Kết thúc")
        select = abs(int(input("Chọn 1 lệnh để thực hiện: ")))
        if (select > 4) or (select < 1):
            print("Số không hợp lệ!")
            continue
        elif select == 1:
            next_val = input("Nhập một giá trị bất kì để thêm vào queue: ")
            test_queue.add(next_val)
            continue
        elif select == 2:
            test_queue.print_queue()
            continue
        elif select == 3:
            test_queue.remove()
            continue
        elif select == 4:
            finish = True
            print("Chương trình kết thúc...")
