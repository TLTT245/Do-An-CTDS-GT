# Đối tượng node
class Node:
    # Khởi tạo node với 2 thuộc tính
    # + children chứa list các node con
    # + value chứa giá trị của node đó
    def __init__(self, value):
        self.children = []
        self.value = value

    # Hàm thêm nút con
    def add_child(self, child):
        print("Đã thêm nút con", child.value , "vào nút", self.value)
        self.children.append(child)


# Đối tượng cây cơ bản
class GenericTree:
    # Khởi tạo với thuộc tính root chứa node gốc
    def __init__(self):
        self.root = None

    # Thêm nút gốc
    def add_root_node(self, value):
        print("Đã thêm nút giá trị", value, "là nút gốc của cây")
        self.root = Node(value)

    # Thêm một nút con vào 1 nút cha sử dụng duyệt cây theo thứ tự trước
    def find_node_to_add(self, curr, child, father):
        if curr.value == father:
            curr.add_child(Node(child))
            return
        if len(curr.children) != 0:
            for i in range(0, len(curr.children)):
                self.find_node_to_add(curr.children[i], child, father)

    # In tất cả các nút với danh sách các nút con của nút đó (nếu có) sử dụng duyệt cây theo thứ tự trước
    def print_all_nodes(self, curr):
        print(curr.value, "->", [child.value for child in curr.children])
        if len(curr.children) != 0:
            for i in range(0, len(curr.children)):
                self.print_all_nodes(curr.children[i])


# Duyệt theo thứ tự trước dùng đệ quy: Node -> Left -> Right, bắt đầu từ nút gốc
def preorder_traversal(node):
    print(node.value, end=" ")  # In giá trị của nút ra
    if len(node.children) != 0:  # Kiểm tra nếu nút có con, nếu có thì duyệt các nút con từ trái -> phải
        for i in range(0, len(node.children)):
            preorder_traversal(node.children[i])


# Duyệt theo thứ tự sau dùng đệ quy: Left -> Right -> Node, bắt đầu từ nút gốc
def postorder_traversal(node):
    if len(node.children) != 0:  # Kiểm tra nếu nút có con, nếu có thì duyệt các nút con từ trái -> phải
        for i in range(0, len(node.children)):
            postorder_traversal(node.children[i])
    print(node.value, end=" ")  # In giá trị của nút ra


if __name__ == '__main__':
    # Bắt đầu bằng 1 giá trị bất kì
    goc = input("Nhập một giá trị để bắt đầu một cây cơ bản: ")
    # Tạo một cây cơ bản với nút gốc chứa giá trị vừa nhập
    generic_tree = GenericTree()
    generic_tree.add_root_node(goc)
    finish = False
    # Tạo vòng lặp vĩnh cửu, chương trình chỉ kết thúc khi finish = True
    while finish is not True:
        print()
        # Đoạn mã nhập lệnh bằng số đơn giản
        # Kiểm tra nếu số người dùng nhập vào là hợp lệ:
        # + Nếu hợp lệ thì thực hiện 1 trong những lệnh liệt kê bên dưới
        # + Nếu không thì báo lỗi và cho người dùng nhập lại
        print("Lựa chọn : 1 - Danh sách nút, 2 - Thêm nút con, 3 - Duyệt cây, 4 - Kết thúc")
        select = abs(int(input("Tùy chọn : ")))
        if select == 1:
            generic_tree.print_all_nodes(generic_tree.root)
            continue
        elif select == 2:
            child_node = input("Nhập giá trị của nút con mới: ")
            parent_node = input("Nhập giá trị của nút cha: ")
            generic_tree.find_node_to_add(generic_tree.root, child_node, parent_node)
            continue
        elif select == 3:
            choice = abs(int(input("Chọn cách duyệt: 1 - Theo thứ tự trước , 2 -  Theo thứ tự sau : ")))
            if choice == 1:
                preorder_traversal(generic_tree.root)
            elif choice == 2:
                postorder_traversal(generic_tree.root)
            else:
                print("Tùy chọn không hợp lệ!")
            continue
        elif select == 4:
            finish = True
            print("Đoạn mã kết thúc ")
        else:
            print("Tùy chọn không hợp lệ ")