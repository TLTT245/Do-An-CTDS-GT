row = [2, 1, -1, -2, -2, -1, 1, 2, 2]
col = [1, 2, 2, 1, -1, -2, -2, -1, 1]

# Kiểm tra nếu (x, y)`là ô nằm trên bàn cờ
def isValid(x, y):
    return not (x < 0 or y < 0 or x >= N or y >= N)
def knightTour(visited, x, y, pos, found, count):
    visited[x][y] = pos
    # Nếu tất cả các ô đã được đi qua, in ra giải pháp
    if pos >= N * N:
        for r in visited:
            print(r)
        print()
        found[0] = True    # Tìm thấy giải pháp
        count[0] += 1      # Cộng vào biến count lưu giá trị số giải pháp tìm thấy
        visited[x][y] = 0  # Không tìm thấy giải pháp, quay lui
        return
    # Kiểm tra tất cả 8 bước di chuyển có thể thực hiện của một quân mã
    for k in range(8):
        # Di chuyển đến vị trí mới của quân mã từ vị trí hiện tại trên bàn cờ
        newX = x + row[k]
        newY = y + col[k]
        # Nếu vị trí mới là hợp lệ và chưa được thăm trước đó
        if isValid(newX, newY) and visited[newX][newY] == 0:
            knightTour(visited, newX, newY, pos + 1, found, count)
    # Quay lui từ ô hiện tại và dời nó khỏi đường đi hiện tại
    visited[x][y] = 0

N = int(input('Nhập N = '))
visited = [[0 for x in range(N)] for y in range(N)]
 # Vị trí đầu tiên của quân mã mặc định là 1
pos = 1
# Giải mã đi tuần từ tọa độ (x,y)
print('\n__ __ __Nhập vào vị trí khởi đầu của con mã__ __ __')
print('\t**Lưu ý: Các chỉ số hàng và cột chạy từ 0 đến n-1**')
x, y = int(input('\tNhập vào vị trí hàng ban đầu của con mã: x = ')), int(
        input('\tNhập vào vị trí cột ban đầu của con mã: y = '))

found = [False]
count = [0]
knightTour(visited, x, y, pos, found, count)

if not found[0]:
    print("Không tìm thấy giải pháp")
else:
    print("Số giải pháp: ", count[0])
#  Nhập vào vị trí khởi đầu của con mã__ __ __
# 	**Lưu ý: Các chỉ số hàng và cột chạy từ 0 đến n-1**
# 	Nhập vào vị trí hàng ban đầu của con mã: x = 2
# 	Nhập vào vị trí cột ban đầu của con mã: y = 2   
    #=========

# _Nhập vào vị trí khởi đầu của con mã__ __ __
# 	**Lưu ý: Các chỉ số hàng và cột chạy từ 0 đến n-1**
# 	Nhập vào vị trí hàng ban đầu của con mã: x = 2
# 	Nhập vào vị trí cột ban đầu của con mã: y = 3
# Không tìm thấy giải pháp
