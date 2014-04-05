import curses, os
from data import Data
from datetime import datetime

class Screen:

    def __init__(self, screen):
        self.screen = screen
        self.data = Data()
        self.set_colors()
        self.set_screen()
        self.set_subwin()

        # Variables that will be used later
        self.quit = False
        self.option = 0
        self.text = ''
        self.menu_list = [
            "Change Path",
            "Help Menu",
            "Settings",
            "Placeholder",
            "Whatever",
            "Exit"
            ]
        # End Varialbe assignment

        self.main_screen()

    def set_colors(self):
        curses.init_pair(1, curses.COLOR_BLUE, curses.COLOR_WHITE)
        curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
        curses.init_pair(6, curses.COLOR_RED, curses.COLOR_WHITE)
        self.BLUEW = curses.color_pair(1)
        self.BLACKW = curses.color_pair(2)
        self.GREENB = curses.color_pair(3)
        self.CYANB = curses.color_pair(4)
        self.YELLOWB = curses.color_pair(5)
        self.REDW = curses.color_pair(6)
        return

    def set_screen(self):
        self.screen.nodelay(1)
        curses.curs_set(0)
        self.screen.attrset(self.BLUEW)
        self.screen.bkgd(' ', self.BLACKW)
        self.y, self.x = self.screen.getmaxyx()

    def main_screen(self):
        selection = -1

        while self.quit == False:
            action = self.screen.getch()
            self.screen_resize()
            self.graphics = [self.BLUEW]*len(self.menu_list)
            self.graphics[self.option] = self.BLUEW | curses.A_REVERSE

            self.draw_subwin()

            self.draw_menu()

            if action == curses.KEY_UP:
                self.option = (self.option - 1) % len(self.menu_list)
            elif action == curses.KEY_DOWN:
                self.option = (self.option + 1) % len(self.menu_list)
            elif action == ord('\n') or action == ord('\r'):
                selection = self.option
                self.eval_selection(selection)

        return

    def draw_subwin(self):
        now = datetime.now()
        then = (now - datetime(1970,1,1)).total_seconds()
        images = self.data.get_file_list()
        self.sy, sx = self.subwindow.getmaxyx()
        self.settings_list = [
            '        Y, X: ({0}, {1})'.format(self.y, self.x),
            'Directory Is: {0}'.format(self.data.get_path()),
            '   Option Is: {0}'.format(str(self.option)),
            ' Images Path: {0}'.format(self.text)
            ]
        self.subwindow.box()
        self.subwindow.addstr(0, self.x/2-6, "| SETTINGS |")
        self.subwindow.addstr(1, self.x-15, "FILES", self.GREENB | curses.A_UNDERLINE)
        self.subwindow.addstr(self.sy-3, self.x/2-6, "{0}".format(then), self.CYANB)
        self.subwindow.addstr(self.sy-2, self.x/2-14, "{0} {1}".format(now.strftime("%a %b %d, %Y"),
            now.strftime("%I:%M:%S %p")), self.CYANB)

        for num, item in enumerate(images):
            if num == self.sy-6 and len(images) > num:
                self.subwindow.addstr(num+2, self.x-47,
                '{:>30}'.format("....."), self.YELLOWB)
                break
            else:
                self.subwindow.addstr(num+2, self.x-47, '{0:>30}  {1:10,} Kb'.format(item,
                    os.path.getsize(self.data.get_path() + '/' + item)/1024), self.YELLOWB)

        for num, item in enumerate(self.settings_list):
            self.subwindow.addstr((self.sy-3)/len(self.settings_list)+num+1,
                3, item, self.GREENB)

        self.subwindow.refresh()
        return

    def set_subwin(self):
        self.subwindow = curses.newwin(self.y/3, self.x, 0, 0)
        self.subwindow.attrset(curses.A_NORMAL)
        return

    def draw_menu(self):
        for num, item in enumerate(self.menu_list):
            y_val = len(self.menu_list)/2 - num
            self.screen.addstr(self.y/2-y_val, 3, "| {0} |".format(num),
                self.graphics[num])
            self.screen.addstr(self.y/2-y_val, 9, item, self.BLUEW)
	self.screen.addstr(self.sy+1, self.x/2-11, ' STAMP-FINDER v0.1.0 ', self.BLUEW | curses.A_STANDOUT)
        if os.getuid() != 0:
            self.screen.addstr(self.y-2, self.x/2-30,
                ' Warning! You are not running as \'ROOT\'. Running as {!r} '.format(str(os.getlogin())),
                self.REDW | curses.A_BOLD | curses.A_STANDOUT)

    def eval_selection(self, selection):
        if selection == 0:
            curses.echo()
            curses.curs_set(1)
            self.text = self.subwindow.getstr((self.sy-3)/len(self.settings_list)+4, 17)
            if self.text != '':
                if self.text == ' ':
                    self.text = "INVALID PATH"
            if self.text != "INVALID PATH":
                if self.text == 'home':
                    self.text = self.data.go_home()
                elif os.path.isdir(self.text) is False:
                    self.text = "INVALID PATH"
                else:
                    self.data.set_path(self.text)
            self.subwindow.clear()
            curses.noecho()
            curses.curs_set(0)
            return

        if selection == len(self.menu_list)-1:
            self.quit = True
            return

    def screen_resize(self):
        while self.x < 75 or self.y < 30:
            self.screen.clear()
            if self.y > 4 and self.x > 38:
                self.screen.addstr(self.y/2, self.x/2-19,
                    'PLEASE INCREASE THE SIZE OF THE WINDOW!',
                    self.BLUEW | curses.A_BOLD | curses.A_REVERSE)
            self.y, self.x = self.screen.getmaxyx()
            self.screen.refresh()
            if self.x >= 75 and self.y >= 30:
                self.screen.clear()
                break

        resize = curses.is_term_resized(self.y, self.x)

        if resize is True:
            self.screen.clear()
            self.y, self.x = self.screen.getmaxyx()
            curses.resizeterm(self.y, self.x)
            self.subwindow = curses.newwin(self.y/3, self.x, 0, 0)
            self.screen.refresh()
            return
