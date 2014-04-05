from screen import Screen
import curses
import sys


def print_help():
    print "SFINDER - Stamp-Finder v0.1.0"
    print ""
    print "NOTE: Run using elevated privileges with read/write permissions."
    print ""
    print "USAGE: sfinder [arguments]"
    print "   or: sfinder -s {-d|-p} <path> [-m <method> -b <date> -e <date> -o <path>]"
    print ""
    print "ARGUMENTS:"
    print "   -h or --help                Print Help (this message) and exit"
    print "   -s                          Run program as script with no GUI (requires '-d' or '-p')"
    print "   -d[dir_path]                Directory containing images (e.g. '/etc/folder')"
    print "   -p[file_path]               Path to single file (e.g. '/etc/file.img')"
    print "   -m[method]                  The timestamp format to be used"
    print "   -b[yyyy-mm-dd,hh:mm:ss]     Beginning date (yyyy-mm-dd,hh:mm:ss)"
    print "   -e[yyyy-mm-dd,hh:mm:ss]     End date (yyyy-mm-dd,hh:mm:ss)"
    print "   -o[dir_path]                Output folder location (default: current folder)"
    print ""
    sys.exit()

def main(argv):
    h = ('-h' or '--help' or '-help' or '-?')
    args = ('-s' or '-d' or '-p' or '-b' or '-e' or '-o')

    if h in argv:
        print_help()
    elif len(argv) > 1 and args not in argv:
        print_help()

    curses.wrapper(Screen)
    return

if __name__ == '__main__':
    main(sys.argv)
