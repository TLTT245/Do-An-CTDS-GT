# Node class
class Node:

    # Hàm tạo node
    def __init__(self, data):
        self.data = data  # Thuộc tính dữ liệu, lấy tham số đầu vào data
        self.next = None  # Thuộc tính next trỏ đến nút tiếp theo
# Linked List class
class LinkedList:
    # Hàm tạo object danh sách liên kết
    def __init__(self):
        self.head = None
    # Hàm in nội dung danh sách liên kết bắt đầu từ node đầu (head)
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    # Hàm thêm node vào đầu danh sách
    def them_vaodauds(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        print("Nút ", value, "đã được thêm vào danh sách")

    # Hàm thêm node vào cuối danh sách
    def them_vaocuoids(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        print("Nút", value, "đã được thêm vào cuối danh sách")

    # Hàm thêm node vào giữa 2 node có sẵn trong danh sách
    def them_vaogiua(self, node_value, value):
        curr_node = self.head
        while curr_node.data != node_value:
            if curr_node.next is None:
                print("Không có node như vậy tồn tại")
                return
            curr_node = curr_node.next
        new_node = Node(value)
        new_node.next = curr_node.next
        curr_node.next = new_node
        print("Nút", value, "đã được thêm vào sau nút", curr_node.data)

    # Xóa 1 node
    def xoa_khoids(self, value):
        if self.head is None:
            print("Danh sách trống!")
            return
        if (self.head.next is None) and (self.head.data == value):
            self.head = None
            print("Nút duy nhất trong danh sách đã bị xóa!")
            return
        curr_node = self.head
        if self.head.data == value:
            self.head = self.head.next
            print("Nút ", curr_node.data,"Đã bị xóa")
            curr_node.data = None
            return
        while curr_node.data != value:
            if curr_node.next is None:
                print("Không có node như vậy tồn tại")
                return
            prev_node = curr_node
            curr_node = curr_node.next
        prev_node.next = curr_node.next
        print("Nút", curr_node.data,"Đã bị xóa")
        curr_node.data = None
        curr_node.next = None


if __name__ == '__main__':
    # Bắt đầu bằng list trống
    giatri_batdau = input("Nhập một giá trị để bắt đầu danh sách liên kết đơn: ")
    linked_list = LinkedList()
    linked_list.head = Node(giatri_batdau)
    finish = True
    while finish is not False:
        print()
        print("Tùy Chọn: 11:Thêm vào đầu danh sách, 12:Thêm vào cuối danh sách, 13:Thêm sau nút trong danh sách ")
        print("Tùy Chọn: 2:In danh sách, 3:Xóa nút trong danh sách, 4:Kết thúc chương trình")
        select = abs(int(input("Chọn 1 lệnh để thực hiện: ")))
        if select == 11:
            next_val = input("Nhập một giá trị bất kì: ")
            linked_list.them_vaodauds(next_val)
            continue
        elif select == 12:
            next_val = input("Nhập một giá trị bất kì: ")
            linked_list.them_vaocuoids(next_val)
            continue
        elif select == 13:
            after_node = input("Nhập giá trị nút để thêm sau nó: ")
            next_val = input("Nhập một giá trị bất kì: ")
            linked_list.them_vaogiua(after_node, next_val)
            continue
        elif select == 2:
            linked_list.print_list()
            continue
        elif select == 3:
            value = input("Nhập một giá trị bất kì: ")
            linked_list.xoa_khoids(value)
            continue
        elif select == 4:
            finish = True
            print("Chương trình kết thúc...")
        else:
            print("Số không hợp lệ!")
            