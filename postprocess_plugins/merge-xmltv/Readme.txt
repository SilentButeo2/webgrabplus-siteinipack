Merge-Xmltv V1.0.0
A Utility To Merge Multiple xml Files.
AND/OR Perform Time Corrections.
merge-xmltv.exe -h or --help For More Information.
Time Conversion Code Based on WG2MP.exe Source.
Courtesy of Jan van Straaten http://www.webgrabplus.com
Blackbear199 [12/03/2022]

------------------------------------------
Minimum of 3 Arguments Required.
------------------------------------------

Usage: merge-xmltv.exe [timezone] [output] [input]
-t   --timezone  UTC,LOCAL,KEEP
-o   --output    filename.xml
-h   --help      Display This Message

Examples..

Adjust Times to UTC For a Single File:
merge-xmltv.exe -t UTC -o corrected.xml filename1.xml

Merge Multiple Files With No Time Adjustment:
merge-xmltv.exe --timezone KEEP --output [path to]merged.xml [path to]filename1.xml [path to]filename2.xml

Merge Multiple Files in a Directory (Output File Will Be Excluded if Residing in Same Location):
merge-xmltv.exe --timezone LOCAL --output [path to]merged.xml [directory path]

Linux version requires Dotnet installed.

Have fun !!
