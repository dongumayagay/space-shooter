import curses.ascii

screen = curses.initscr()
screen.nodelay(True)
screen.keypad(True)
screen.timeout(100)
curses.curs_set(0)

sh, sw = screen.getmaxyx()

ship_y, ship_x = int(sh * .9), sw // 2
ship_speed = 2
lasers = []


while True:
    key = screen.getch()
    if key == curses.ascii.ESC:
        curses.endwin()
        quit()
    if key == curses.KEY_LEFT:
        ship_x -= ship_speed
    if key == curses.KEY_RIGHT:
        ship_x += ship_speed
    if key == ord(' '):
        lasers.append([ship_y-2, ship_x])




    screen.clear()
    screen.addch(ship_y-1, ship_x, '#')
    screen.addstr(ship_y, ship_x-2,'#####')
    for laser in lasers:
        screen.addch(laser[0],laser[1],'*')
        if laser[0] <= 2:
            lasers.remove(laser)
        else:
            laser[0] -= 1
    screen.refresh()