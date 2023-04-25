from Pillow import Image,ImageDraw
def is_valid(board, row, col, n):
    # Kiểm tra xem vị trí (row, col) có thể đặt được quân hậu không
    for i in range(row):
        if board[i][col] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False
    return True

def solve(board, row, n, solutions):
    # Nếu đã đặt được n quân hậu thì thêm giải pháp vào danh sách và trả về True
    if row == n:
        solutions.append([row[:] for row in board])
        return True
    found_solution = False
    for col in range(n):
        if is_valid(board, row, col, n):
            # Đặt quân hậu vào vị trí (row, col)
            board[row][col] = 1
            # Gọi đệ quy để đặt các quân hậu tiếp theo
            if solve(board, row+1, n, solutions):
                found_solution = True
            # Đặt quân hiện tại trở lại 0
            board[row][col] = 0
    # Trả về kết quả
    return found_solution


def print_solution(board):
    # Tạo hình ảnh bàn cờ
    cell_size = 50
    img_size = cell_size * len(board)
    img = Image.new('RGB', (img_size, img_size), 'white')
    draw = ImageDraw.Draw(img)

    # Vẽ các ô trống và quân hậu lên bàn cờ
    for i in range(len(board)):
        for j in range(len(board)):
            x0, y0 = i * cell_size, j * cell_size
            x1, y1 = x0 + cell_size, y0 + cell_size
            if (i + j) % 2 == 0:
                draw.rectangle((x0, y0, x1, y1), fill='black')
            if board[i][j] == 1:
                draw.ellipse((x0 + 5, y0 + 5, x1 - 5, y1 - 5), fill='red')

    # Hiển thị hình ảnh bàn cờ
    img.show()

def n_queens(n):
    # Khởi tạo bàn cờ rỗng
    board = [[0 for _ in range(n)] for _ in range(n)]
    # Tìm tất cả các giải pháp
    solutions = []
    solve(board, 0, n, solutions)
    # In ra các giải pháp
    if solutions:
        for i, solution in enumerate(solutions):
            print("Solution", i+1)
            print_solution(solution)
    else:
        print("No solutions found")

# Tìm tất cả các giải pháp của bài toán 8 quân hậu
n_queens(8)