import curses.ascii, random, time, os
if os.name == 'nt':
    import winsound

# initializations
screen = curses.initscr()
screen.nodelay(True)
screen.keypad(True)
screen.timeout(100)
curses.curs_set(0)
curses.noecho()
sh, sw = screen.getmaxyx()
ship_y, ship_x = int(sh * .95), sw // 2
ship_speed = 1
lasers = []
enemies = []
start_time = time.time()
move_time = time.time()
inWindows = True if os.name == 'nt' else False

while True:

    # controls
    key = screen.getch()
    if key == curses.ascii.ESC:
        curses.endwin()
        quit()
    if key == curses.KEY_LEFT or key == ord('a') and ship_x - 2 > 0:
        ship_x -= ship_speed
    if key == curses.KEY_RIGHT or key == ord('d')  and ship_x + 2 < sw - 1:
        ship_x += ship_speed
    if key == ord(' '):
        lasers.append([ship_y - 2, ship_x])
        if inWindows:
            winsound.PlaySound('laser_sound', winsound.SND_ASYNC)
        
    # drawing and logic
    screen.clear()

    # ship drawing
    screen.addch(ship_y - 1, ship_x, '#')
    screen.addstr(ship_y, ship_x - 2, '#####')

    # laser drawing and movement
    for laser in lasers:
        screen.addch(laser[0], laser[1], '*')
        if laser[0] <= 2:
            lasers.remove(laser)
        else:
            laser[0] -= 1

    # enemy spawn
    if time.time() - start_time >= 3:
        start_time = time.time()
        enemies.append([1, random.randint(2, sw - 3)])

    # enemy drawing
    for enemy in enemies:
        screen.addch(enemy[0], enemy[1], 'O')
        if enemy[0] >= sh - 2:
            enemies.remove(enemy)

    # enemy movement (i created this because enemy is so fast)
    if time.time() - move_time >= 0.3 and len(enemies) > 0:
        move_time = time.time()
        for enemy in enemies:
            enemy[0] += 1

    # collision
    for enemy in enemies:
        for laser in lasers:
            if enemy[0] == laser[0] and enemy[1] == laser[1]:
                if inWindows:
                    winsound.PlaySound('explosion', winsound.SND_ASYNC)
                
                enemies.remove(enemy)
                lasers.remove(laser)

    screen.refresh()
