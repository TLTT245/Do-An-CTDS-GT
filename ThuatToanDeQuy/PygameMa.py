from PIL import Image, ImageDraw
def is_valid_move(x, y, board):
    """Kiểm tra xem nước đi (x, y) có hợp lệ trên bàn cờ hay không"""
    if 0 <= x < len(board) and 0 <= y < len(board) and board[x][y] == -1:
        return True
    return False

def knight_tour(board, move_num, x, y, x_move, y_move):
    """Hàm đệ quy để giải bài toán Mã đi tuần"""
    if move_num == len(board) ** 2:
        return True
    
    for i in range(len(x_move)):
        next_x = x + x_move[i]
        next_y = y + y_move[i]
        if is_valid_move(next_x, next_y, board):
            board[next_x][next_y] = move_num
            if knight_tour(board, move_num+1, next_x, next_y, x_move, y_move):
                return True
            board[next_x][next_y] = -1
    
    return False

def print_board(board):
    image_size = 600

# Kích thước mỗi ô trên bàn cờ
    cell_size = image_size // n

# Tạo ảnh mới với kích thước image_size x image_size, màu trắng
    img = Image.new("RGB", (image_size, image_size), color="white")

# Vẽ bàn cờ lên ảnh
    draw = ImageDraw.Draw(img)
    for i in range(n):
        for j in range(n):
            x0, y0 = j * cell_size, i * cell_size
            x1, y1 = (j+1) * cell_size, (i+1) * cell_size
            color = "black" if (i+j) % 2 == 0 else "white"
            draw.rectangle((x0, y0, x1, y1), fill=color, outline="black")
            if board[i][j] != -1:
                text_size = draw.textsize(str(board[i][j]))
                text_x = x0 + (cell_size - text_size[0]) // 2
                text_y = y0 + (cell_size - text_size[1]) // 2
                draw.text((text_x, text_y), str(board[i][j]), fill="red")

    # Lưu ảnh vào file "knight_tour.png"
    img.save("knight_tour.png")
    print("Đã lưu ảnh bàn cờ vào file knight_tour.png")

n = int(input("Nhập kích thước bàn cờ: "))
start_x, start_y = map(int, input("Nhập tọa độ ô bắt đầu (x, y): ").split())

# Khởi tạo bàn cờ với giá trị -1
board = [[-1] * n for _ in range(n)]

# Đánh số nước đi đầu tiên
board[start_x][start_y] = 0

# Khởi tạo các bước đi của Mã
x_move = [2, 1, -1, -2, -2, -1, 1, 2]
y_move = [1, 2, 2, 1, -1, -2, -2, -1]

if knight_tour(board, 1, start_x, start_y, x_move, y_move):
    print("Đã tìm thấy lời giải:")
    print_board(board)
else:
    print("Không tìm thấy lời giải")
