def tower_of_hanoi(n, start, end, mid ):
    if n == 1:
        print(f"Chuyển đĩa 1 từ {start} đến {end}")
        return
    tower_of_hanoi(n-1, start, mid, end)
    print(f"Chuyển đĩa {n} từ {start} đến {end}")
    tower_of_hanoi(n-1, mid, end, start)
tower_of_hanoi(3,'A','C','B')   