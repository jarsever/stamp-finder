SFINDER
=======

USAGE
-----

`sfinder [-h] [-q] [-E epoch ] [-s start_date ] [-e end_date ] [-l] [-p path ]`

DESCRIPTION
-----------

**sfinder** searches for timestamps in files using only the binary data.
This program is written in Python and had raw cell phone forensic images
in mind. Any file containing raw data can be scanned for timestamps but
*sfinder* is more accurate if given specific search parameters.

This program will take time because it of the conversion from binary data to
timestamps. It also searches for every possibility which means it has to
test every byte in the file. Hashing is also performed to ensure data
integrity.

OPTIONS
-------

`-h`
> Show the help message and exit.

`-q`
> Quit Mode. Run *sfinder* without hashing files to speed up processing.

`-E epoch`
> Set the epoch origin date for the filesystem the image or file was
> created. Formatting: ’YYYY,MM,DD’

`-s *start_date*`
> The date you want the search to start at. All timestamps before this
> date will be disregarded. Can be set down to seconds but requires at
> least the YYYY, MM, and DD to be set. Formatting: ’YYYY,MM,DD,HH,mm,ss’

`-e end_date`
> The date you want the search to stop at. All timestamps after this date
> will be disregarded. Can be set down to seconds but requires at least
> the YYYY, MM, and DD to be set. Formatting: ’YYYY,MM,DD,HH,mm,ss’

`-l`
> Search for timestimps in ’Little Endian’ format *(cd ab)* instead of the
> normal ’Big Endian’ format *(ab cd).*

`-p path`
> The path to the file or directory you want *sfinder* to scan. If it is a
> directory, all files in the directory will be processed.

FILES
-----

`~/sfinder_OUT/`
> The directory containing the output of hashes and timestamp data.

`~/sfinder.log`
> Log file of errors and program run information.

`/opt/sfinder/`
> Directory where the source code is located at.

ENVIRONMENT
-----------

The following are the defaults set when running *sfinder*

`-E`
> Default *epoch* is ’1970,1,1’

`-s`
> Default *start_date* is one(1) year ago from today.

`-e`
> Default *end_date* is today’s date.

`-l`
> Default is *False* and will run as ’Big Endian’.

`-p`
> Default is the currenty directory *sfinder* is being run in.

AUTHOR
------

Jared Everett \<jarsever@gmail.com\>

* * * * *
