
class Stack:
    def __init__(self):
        self.stack = []  # Khởi tạo stack bằng 1 list trống

    def add(self, value):
        # Thêm phần tử vào cuối list dùng append() (LI - Last In)
        if value not in self.stack:
            print("Đã thêm phần tử giá trị", value)
            self.stack.append(value)
        else:
            print("Giá trị đã nằm trong stack!")

    # In stack
    def print_stack(self):
        print("Stack hiện tại:", self.stack)
        print("Giá trị nằm trên cùng stack:", self.peek())

    # Hàm peek() để trả giá trị nằm trên cùng stack
    def peek(self):
        return self.stack[-1]

    # Hàm remove() loại bỏ giá trị nằm trên cùng stack (FO - First Out)
    def remove(self):
        if len(self.stack) <= 0:
            return "Không thể bỏ giá trị nào"
        else:
            print("Đã xóa phần tử giá trị", self.peek())
            self.stack.pop()


if __name__ == "__main__":
    test_stack = Stack()
    # Bắt đầu bằng 1 giá trị bất kì
    first_val = input("Nhập một giá trị để bắt đầu stack: ")
    test_stack.add(first_val)
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
            next_val = input("Nhập một giá trị bất kì để thêm vào stack: ")
            test_stack.add(next_val)
            continue
        elif select == 2:
            test_stack.print_stack()
            continue
        elif select == 3:
            test_stack.remove()
            continue
        elif select == 4:
            finish = True
            print("Chương trình kết thúc...")
