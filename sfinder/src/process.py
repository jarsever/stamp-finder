import os, sys, hashlib, logging, traceback
from data import Data
from datetime import datetime, timedelta
from glob import glob1
from progressbar import ProgressBar, ETA, Bar, Percentage, FileTransferSpeed



class Process(Data):

	def __init__(self, args):
		logging.info('==================> Started Stamp-Finder <==================')
		Data.__init__(self, args)

		# See if a quick run is wanted.
		if not self.quick:
			Q = raw_input('\nDo you want to skip Hashing for faster run? [yN] ')
			if Q == ('y' or 'Y'):
				self.quick = True

		self.create_files()

		if not self.quick:
			self.Main_hash()

		self.sfinder()

		if not self.quick:
			self.Main_hash(final=True)

		return


	# Loop over list and create the hashes that will be recordered
	# and compared later to verify nothing changed.
	#
	def Main_hash(self, final=False):

		for image in self.image_list:
			if not final:
				print '[INFO] RUNNING HASH: {0}\n'.format(image.name)
				logging.info('Running First hash on: {0}'.format(image.name))
			else:
				print '\n[INFO] VERIFYING HASH: {0}'.format(image.name)
				logging.info('Running Last hash on: {0}'.format(image.name))

			hashes = self.hash_all(image.path + '/' + image.name)

			if final is False:
				image.md5 = hashes[0]
				image.sha1 = hashes[1]
				image.sha256 = hashes[2]
				
			self.writeHashes(image, hashes, final)



	# Create the files needed for the ouput. If the scan is on a directory
	# each file will then have it's own directory to store files. Files
	# will also increment by one(1) if there are already files in the
	# directory.
	#
	def create_files(self):
		home = "{0}/sfinder".format(os.path.expanduser('~'))
		today = "{0}/{1}".format(home, datetime.now().strftime('%m-%d-%Y'))
		curr_dir = "{0}/{1}".format(today, os.path.basename(self.path))

		print "\n[INFO] OUTPUT: {0}\n".format(today)
		print '[INFO] LOG: {0}\n'.format(os.path.expanduser('~') + '/' + 'sfinder.log')
		logging.info("Output files located at: {0}".format(today))

		if not os.path.exists(home):
			os.makedirs(home)

		if not os.path.exists(today):
			os.makedirs(today)

		if os.path.isdir(self.path):
			if not os.path.exists(curr_dir):
				os.makedirs(curr_dir)

		for image in self.image_list:

			# Check and make sure the file is readable or not.
			# Create the folder and files if it is readable.
			#
			if os.access(image.path, os.R_OK):
				local_home = "{0}/{1}".format(today if not os.path.isdir(self.path) else curr_dir,
					image.name)

				if not os.path.exists(local_home):
					os.makedirs(local_home)

				num = len(glob1(local_home, '*{0}_OUT*'.format(image.name)))

				if not self.quick:
					image.Hash_FN = '{0}/{1:02d}-{2}{3}.txt'.format(local_home, num+1, image.name, '_HASH')
					hf = open(image.Hash_FN, 'w')
					hf.close()

				image.Out_FN = '{0}/{1:02d}-{2}{3}.csv'.format(local_home, num+1, image.name, '_OUT')
				of = open(image.Out_FN, 'w')
				of.close()


	def hash_all(self, path):	# Hashing function.
		hashes = []
		with open(path, 'rb') as f:
			h = hashlib.md5()
			s1 = hashlib.sha1()
			s256 = hashlib.sha256()
			while True:
				data = f.read(8192)		# Read in buffer to acommodate large files.
				if not data:
					break
				h.update(data)
				s1.update(data)
				s256.update(data)
			f.close()
			hashes.append(h.hexdigest())
			hashes.append(s1.hexdigest())
			hashes.append(s256.hexdigest())
			return hashes


	def writeHashes(self, image, hashes, final):	# Function to write the hashes to file.

		with open(image.Hash_FN, 'ab') as f:

			if final:
				f.write("                  VERIFYING HASHES\r\n\r\n")

			if not final:
				f.write("                 GENERATING HASHES\r\n\r\n")

			f.write("{0}\r\n\r\n".format(datetime.now().strftime('%m/%d/%Y %H:%M:%S')))
			f.write('NAME: {0}\r\n'.format(image.name))

			if not final:
				f.write('SIZE: {0:.2f} Mbytes\r\n'.format(
					os.stat(image.path + '/' + image.name).st_size/1024.0/1024))

			if not final:
				f.write("\r\nMD5:\t{0}\r\n".format(image.md5))
				f.write("SHA1:\t{0}\r\n".format(image.sha1))
				f.write("SHA256:\t{0}\r\n\r\n".format(image.sha256))
			else:
				f.write("\r\nMD5:\t{0}\r\n".format(hashes[0]))
				f.write("SHA1:\t{0}\r\n".format(hashes[1]))
				f.write("SHA256:\t{0}\r\n\r\n".format(hashes[2]))

				f.write("MD5 Pass: {0}\r\n".format(image.md5 == hashes[0]))
				f.write("SHA1 Pass: {0}\r\n".format(image.sha1 == hashes[1]))
				f.write("SHA256 Pass: {0}\r\n\r\n".format(image.sha256 == hashes[2]))

			f.write("\r\n")
			f.close()



	# This is the most complicated function in this program. It will loop over
	# all of the images and search one byte at a time for timestamps. Because
	# Python doesn't truly read files as binary, we need to convert it to binary
	# and then a base 10 number. Search parameters should be very specific in
	# order to reduce the number of dates found.
	#
	def sfinder(self):

		E_Seconds = (self.D_end - self.Epoch).total_seconds()

		print '[WARNING] This process may take a while to finish.\n'

		for image in self.image_list:

			try:

				name = image.path + '/' + image.name
				c_count = 0
				found = []
				lastDate = 0

				print '[INFO] PROCESSING: ', image.name
				logging.info('STARTED timestamp search for: {0}'.format(image.name))


				# This is the progress bar that is displayed.
				#
				widgets = [' ', ETA(), ' ', Bar(marker='#', left='[', right=']'), ' ', Percentage(), ' ',
					'(', FileTransferSpeed(), ' )']
				pbar = ProgressBar(widgets=widgets, maxval=os.stat(name).st_size)

				pbar.start()
				with open(name, 'rb') as f:
					while True:
						pbar.update(f.tell())
						data = f.read(2048)

						if not data:
							break

						try:
							for c in data:

								found.append('{0:08b}'.format(ord(c)))

								if len(found) > 4:
									del found[0]

								if len(found) == 4:

									if not self.Little:

										try:
											X = int(''.join(found), 2)
											x = datetime.fromtimestamp(X + self.Epoch_diff)
										except:
											x = False

										if x != False:
											if X <= self.E_Seconds and X >= self.S_Seconds:
												if lastDate == 0:
													lastDate = x
													seconds = ''
												else:
													seconds = (x - lastDate).total_seconds()
													lastDate = x
													if seconds < 0:
														seconds = ''

												image.add_item(c_count, hex(int(''.join(found), 2)),
													seconds if seconds <= 2400 else '', x)

									if self.Little:

										try:
											Y = int(''.join(reversed(found), 2))
											y = datetime.fromtimestamp(Y + self.Epoch_diff)
										except:
											y = False

										if y != False:
											if Y <= self.E_Seconds and Y >= self.S_Seconds:
												if lastDate == 0:
													lastDate = y
													seconds = ''
												else:
													seconds = (y - lastDate).total_seconds()
													lastDate = y
													if seconds < 0:
														seconds = ''

												image.add_item((c_count), hex(int(''.join(found), 2)),
													seconds if seconds <= 2400 else '', y)

									if len(image.item_list) > 5000:
										self.writeCSV(image)

									c_count += 1
						except KeyboardInterrupt:
							raise Exception('User has canceled processing!\n')

					logging.info('FINISHED timestamp search for: {0}'.format(image.name))
					f.close()
					pbar.finish()
					self.writeCSV(image)

			except Exception as e:
				print "[ERROR] {0}".format(e)
				print "[INFO] Skipping {0} due to Error.".format(image.name)
				logging.error(e)


	# This function is called when the 'item' list needs to be
	# flushed to reduce size or to finish an image after
	# processing.
	#
	def writeCSV(self, image):

		f = open(image.Out_FN, 'ab')
		if not image.CSV_started:
			f.write('"OFFSET","HEX VALUE","ENDIAN","DATE","FROM LAST"\n')
			image.CSV_started = True

		for item in image.item_list:

			f.write('"{0}","{1}","{2}","{3}"\n'.format(item.offset,
				item.hexVal, item.date, item.seconds))

		f.close()
		image.item_list = []
