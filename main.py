from screen import Screen
import curses

def main():
    curses.wrapper(Screen)
    return

if __name__ == '__main__':
    main()
