import pygame


kx_move = [-2, -2, -1, -1, 1, 1, 2, 2]
ky_move = [-1, 1, -2, 2, -2, 2, -1, 1]


def make_screen(n):
    X = 400
    Y = 400
    pygame.init()
    scrn_display = pygame.display
    scrn_display.set_caption("Result")
    size = scrn_display.set_mode([X, Y])

    m = 0

    window = True
    while window:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                window = False

        while m < n*n:
            pygame.time.wait(500)
            size.fill((210, 210, 210))
            for i in range(n):
                for j in range(n):
                    if (i + j) % 2 == 0:
                        pygame.draw.rect(size, (0, 0, 0), pygame.Rect((X / n) * i, (Y / n) * j, X / n, Y / n))
            for k in range(m):
                pygame.draw.circle(size, (0, 255, 0), ((korder_y[k]+0.5)*(Y/n), (korder_x[k] + 0.5) * (X / n)), X / n / 3)
            pygame.draw.circle(size, (255, 0, 0), ((korder_y[m] + 0.5) * (Y / n), (korder_x[m] + 0.5) * (X / n)), X / n / 3)
            pygame.display.flip()
            pygame.event.get()
            m += 1

    pygame.quit()

# Vẽ bàn cờ
def result():
    for i in range(n):
        for j in range(n):
            print(chess[i][j], end=" ")  # In giá trị, giá trị đó biểu hiện bước đi của quân mã
            korder_x[chess[i][j] - 1] = i  # Lưu vị trí x vào 1 list tạm để vẽ cửa sổ
            korder_y[chess[i][j] - 1] = j  # Lưu vị trí y vào 1 list tạm để vẽ cửa sổ
        print()


def move(x, y):
    global step
    step += 1 # Tăng số bước lên 1
    chess[x][y] = step
    for i in range(8):  # Lặp lại 8 trường hợp quân mã có thể đi
        if step == n*n:   # Kiểm tra nếu số bước vượt quá số vị trí của bàn cờ. Nếu có thì kết thúc chương trình
            print("Buoc di chuyen cua quan ma:")
            result()
            make_screen(n)
            quit()
        # Di chuyển đến vị trí mới
        u = x + kx_move[i]
        v = y + ky_move[i]
        if (u >= 0) and (u < n) and (v >= 0) and (v < n) and (chess[u][v] == 0):
            # Kiểm tra nếu vị trí mới nằm trong bàn cờ và vị trí đó chưa đi qua
            move(u, v)
    # Lùi lại 1 bước nếu không tìm được bước đi tiếp theo
    step -= 1
    chess[x][y] = 0  # Reset lại vị trí ô cờ thành ô chưa đi qua


flag = False


n = abs(int(input("Nhap so n (ban co nxn): ")))


# Khởi tạo số bước là 0 và tạo bàn cờ trống (tất cả các phần tử bằng 0)
# Hai danh sách dưới dùng để lưu nước đi của quân mã
step = 0
chess = [[0 for i in range(n)] for j in range(n)]
korder_x = n*n*[0]
korder_y = n*n*[0]


while not flag:
    print("HELP: Vi tri goc tren cung ben trai la x, y = (0, 0)")
    a = abs(int(input("Nhap vi tri xuat phat x: ")))
    b = abs(int(input("Nhap vi tri xuat phat y: ")))
    # Kiểm tra nếu vị trí ban đầu nằm ngoài bàn cờ. Nếu nằm ngoài người dùng phải nhập lại vị trí
    if a < n and b < n:
        flag = True
        move(b, a)
        print("No move")
    else:
        print("x hoac y vuot qua so luong quy dinh!")