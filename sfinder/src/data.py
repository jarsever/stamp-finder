from datetime import datetime
import logging, os


'''---------------------| Data() Class |--------------------------#
#                                                                 #
# This Class is to be inherited by the Process() class.           #
#                                                                 #
# I didn't want to use global variables so I designed this class  #
# to store all the data needed.                                   #
#                                                                 #
#---------------------------------------------------------------'''

class Data:

	def __init__(self, args):
		self.welcome()
		self.path = args['p']
		self.Epoch = self.convert_date(args['E'])
		self.Epoch_diff = (self.Epoch - datetime(1970,1,1)).total_seconds()
		self.D_start = self.convert_date(args['s']) if type(args['s']) == str else args['s']
		self.D_end = self.convert_date(args['e']) if type(args['e']) == str else args['e']
		self.Little = args['l']
		self.quick = args['q']

		# These are the dates in seconds for the start and end parameters.
		#
		self.E_Seconds = (self.D_end - self.Epoch).total_seconds()
		self.S_Seconds = (self.D_start - self.Epoch).total_seconds()

		self.set_file_list()
		self.set_image_list()


	def set_file_list(self):

		if os.path.islink(self.path):
			self.path = os.readlink(self.path)

		if self.path[0] == '.':
			self.path = os.path.realpath(self.path)

		if self.path[0] not in ('.', '/'):
			self.path = os.getcwd() + '/' + self.path

		if os.path.isfile(self.path):
			self.file_list = [os.path.basename(self.path)]
			self.path = os.path.dirname(os.path.abspath(self.path))
			
		elif os.path.isdir(self.path):
			os.chdir(self.path)
			self.file_list = [f for f in os.listdir(self.path) if os.path.isfile(f)]

		else:
			raise Exception('File or Directory doesn\'t exist: {0}\n'.format(self.path))


	# This function should not be called manually
	def set_image_list(self):
		self.image_list = []
		for f in self.file_list:
			self.image_list.append(Image(f, self.path))


	def welcome(self):
		print "  ____ _____  _    __  __ ____       _____ ___ _   _ ____  _____ ____  "
		print " / ___|_   _|/ \  |  \/  |  _ \     |  ___|_ _| \ | |  _ \| ____|  _ \ "
		print " \___ \ | | / _ \ | |\/| | |_) |____| |_   | ||  \| | | | |  _| | |_) |"
		print "  ___) || |/ ___ \| |  | |  __/_____|  _|  | || |\  | |_| | |___|  _ < "
		print " |____/ |_/_/   \_\_|  |_|_|        |_|   |___|_| \_|____/|_____|_| \_\\"
		print "                                                                       "


	def convert_date(self, string):
		dt = string.split(',')
		while len(dt) < 6:
			dt.append('00')

		try:
			return datetime.strptime(','.join(dt), '%Y,%m,%d,%H,%M,%S')
		except ValueError:
			print ''
			print '####################################################'
			print ''
			print "  Could not convert Date. Make sure it has ticks('')"
			print '        and is within normal date ranges.'
			print ''
			print "           Yours: '{0}'".format((',').join(dt))
			print "          Format: 'YYYY,MM,DD,HH,mm,ss'"
			print ''
			print "#####################################################"
			print ''
			print '[DEBUG] Check ~/sfinder.log for more information. :('
			print ''
			logging.warn(str(sys.exc_info()[1])[:-20])
			logging.error('Stamp-Finder did NOT finish sucessfully!\n')
			logging.critical(traceback.format_exc())
			sys.exit(1)




'''---------------------| Image() Class |-------------------------#
#                                                                 #
#       This Class used by Data() to create the item_list         #
#                and add items while processing.                  #
#                                                                 #
#---------------------------------------------------------------'''

class Image:

    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.item_list = []
        self.md5 = ''				#
        self.sha1 = ''				# HASHES
        self.sha256 = ''			#
        self.Hash_FN = ''			# Hash-out file name
        self.Out_FN = ''			# CSV-out file name
        self.CSV_started = False	# Just a flag to see if the list has been flushed.


    def add_item(self, offset, hexVal, seconds, date):
    	self.item_list.append(Item(offset, hexVal, seconds, date))



class Item:

	def __init__(self, offset, hexVal, seconds, date):
		self.offset = offset
		self.hexVal = hexVal
		self.seconds = seconds
		self.date = date
