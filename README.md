SFINDER
=======

SYNOPSIS
--------

`sfinder [-h] [-q] [-E *epoch* ] [-s *start\_date* ] [-e *end\_date* ] [-l] [-p *path* ]**`

DESCRIPTION
-----------

**sfinder** searches for timestamps in files using only the binary data.
This program is written in Python and had raw cell phone forensic images
in mind. Any file containing raw data can be scanned for timestamps but
*sfinder* is more accurate if given specific search parameters. This
program will take time because it of the conversion from binary data to
timestamps. It also searches for every possibility which means it has to
test every byte in the file. Hashing is also performed to ensure data
integrity.

OPTIONS
-------

> `-h`
>> Show the help message and exit.

> `-q`
>> Quit Mode. Run *sfinder* without hashing files to speed up processing.

> `-E *epoch*`
>> Set the epoch origin date for the filesystem the image or file was
>> created. Formatting: ’YYYY,MM,DD’

`-s *start\_date*`
&nbsp;&nbsp;&nbsp;&nbsp;The date you want the search to start at. All timestamps before this
&nbsp;&nbsp;&nbsp;&nbsp;date will be disregarded. Can be set down to seconds but requires at
&nbsp;&nbsp;&nbsp;&nbsp;least the YYYY, MM, and DD to be set. Formatting: ’YYYY,MM,DD,HH,mm,ss’

`-e end\_date`
&nbsp;&nbsp;&nbsp;&nbsp;The date you want the search to stop at. All timestamps after this date
&nbsp;&nbsp;&nbsp;&nbsp;will be disregarded. Can be set down to seconds but requires at least
&nbsp;&nbsp;&nbsp;&nbsp;the YYYY, MM, and DD to be set. Formatting: ’YYYY,MM,DD,HH,mm,ss’

`-l`
&nbsp;&nbsp;&nbsp;&nbsp;Search for timestimps in ’Little Endian’ format *(cd ab)* instead of the
&nbsp;&nbsp;&nbsp;&nbsp;normal ’Big Endian’ format *(ab cd).*

`-p path`
&nbsp;&nbsp;&nbsp;&nbsp;The path to the file or directory you want *sfinder* to scan. If it is a
&nbsp;&nbsp;&nbsp;&nbsp;directory, all files in the directory will be processed.

FILES
-----

`\~/sfinder\_OUT/`
&nbsp;&nbsp;&nbsp;&nbsp;The directory containing the output of hashes and timestamp data.

`\~/sfinder.log`
&nbsp;&nbsp;&nbsp;&nbsp;Log file of errors and program run information.

`/opt/sfinder/`
&nbsp;&nbsp;&nbsp;&nbsp;Directory where the source code is located at.

ENVIRONMENT
-----------

The following are the defaults set when running *sfinder*

`-E`
&nbsp;&nbsp;&nbsp;&nbsp;Default *epoch* is ’1970,1,1’

`-s`
&nbsp;&nbsp;&nbsp;&nbsp;Default *start\_date* is one(1) year ago from today.

`-e`
&nbsp;&nbsp;&nbsp;&nbsp;Default *end\_date* is today’s date.

`-l`
&nbsp;&nbsp;&nbsp;&nbsp;Default is *False* and will run as ’Big Endian’.

`-p`
&nbsp;&nbsp;&nbsp;&nbsp;Default is the currenty directory *sfinder* is being run in.

AUTHOR
------

Jared Everett <jarsever at gmail dot com\>

* * * * *
