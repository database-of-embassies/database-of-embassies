#!/bin/sh

# Pre-requisite: Install and run wikivoyage2osm in a parallel directory

SOURCE=../wikivoyage2osm/enwikivoyage-20150220-pages-articles.xml.csv
OUTPUT=embassies-and-consulates.csv

# Write CSV header
head -n 1 $SOURCE | sed -e "s/TITLE;TYPE;NAME/CITY;SENDER/" > $OUTPUT

# Write consulates and embassies data
grep "\"legation\"" $SOURCE >> $OUTPUT

# Remove "type" column, as all data has this type
sed -i 's/"legation";//g' $OUTPUT
