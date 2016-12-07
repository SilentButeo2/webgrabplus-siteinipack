#!/bin/bash

echo "****************** Updating Tring.al Channel Site Id's ******************"
echo -e "\n"

cd /home/mike/Downloads/WebGrab+Plus

wget -O tring.al.txt "http://www.tring.al/guide/index.php?size=1"
sed -n "s/.*name = \"epg\([0-9][0-9]-.*\)\".*/\1/p" < tring.al.txt > tring_date_id.txt
date_id=$(cat tring_date_id.txt)
sed -i "s/[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9][0-9][0-9]/$date_id/g" WebGrab++.config.xml
sed -i "s/[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]-[0-9][0-9][0-9][0-9][0-9][0-9]/$date_id/g" tring.al.ini

rm tring.al.txt
rm tring_date_id.txt

mono WebGrab+Plus.exe "$(pwd)"

