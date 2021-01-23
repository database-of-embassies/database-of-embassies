import os
import sys
from urllib import unquote
import hashlib
import re

def safe_for_url(string):
    return string.lower().replace(' ', '_').replace("'", '_')

# Does not work for https://commons.wikimedia.org/wiki/File:%E3%82%B8%E3%83%96%E3%83%81%E5%A4%A7%E4%BD%BF%E9%A4%A8%E3%81%AF%E4%B8%80%E8%BB%92%E5%AE%B6.jpg
def commons_thumbnail(image, width=300): # image = e.g. from Wikidata, width in pixels
    image = image[len('http://commons.wikimedia.org/wiki/Special:FilePath/'):]
    image = unquote(image)
    image = image.replace(' ', '_') # need to replace spaces with underline 
    m = hashlib.md5()
    m.update(image.encode('utf-8'))
    d = m.hexdigest()
    return "https://upload.wikimedia.org/wikipedia/commons/thumb/"+d[0]+'/'+d[0:2]+'/'+image+'/'+str(width)+'px-'+image

class DiplomaticRepresentation:
    def __init__(self, csv_row):
        cells = csv_row.rstrip().split(';') # rstrip removes the trainling \n character.
        self.operator = cells[0]
        self.operatorQID = cells[1]
        self.jurisdictions = cells[2].split('|')
        self.jurisdictionQIDs = cells[3].split('|')
        self.country = cells[4]
        self.countryQID = cells[5]
        self.city = cells[6]
        self.cityQID = cells[7]
        self.address = cells[8]
        self.latitude = cells[9]
        self.longitude = cells[10]
        self.phone = cells[11]
        self.email = cells[12]
        self.website = cells[13]
        self.facebook = cells[14]
        self.twitter = cells[15]
        self.youtube = cells[16]
        self.picture = cells[17]
        self.pictureAuthor = cells[18]
        self.pictureLicense = cells[19]
        self.pictureLicenseURL = cells[20]
        self.type = cells[21]
        self.typeQID = cells[22]
        self.creation = cells[23]
        self.QID = cells[24]

    def title(self, include_city, include_jurisdiction):
        title = self.type # example: 'embassy'
        title = "%s%s" % (title[0].upper(), title[1:]) # example: 'Embassy'
        title += ' of ' + self.operator + ' in '
        if include_city:
            title += self.city + ', '
        title += self.country
        if include_jurisdiction:
            title += ' for ' + ', '.join(self.jurisdictions)

        return title

    def url_name(self, include_city, include_jurisdiction):
        name = safe_for_url(diplo.type) + '_of_'
        if (include_city):
            name += safe_for_url(self.operator) + '_in_' + safe_for_url(self.city) + '_' + safe_for_url(self.country)
        else:
            name += safe_for_url(self.operator) + '_in_' + safe_for_url(self.country)
        if include_jurisdiction:
            name += '_for_' + '_'.join(self.jurisdictions)

        # Truncate due to macOS default filesystem length limitation to 255 characters
        name = name[:255 - len(".html")]

        return name

class Operator:
    def __init__(self, name, QID):
        self.name = name
        self.QID = QID
        self.countries = {} # Key: countryQID, value: list of DiplomaticRepresentations

    def add_diplomatic_representation(self, diplo):
        countryQID = diplo.countryQID
        if ( not self.countries.has_key(countryQID)):
            self.countries[countryQID] = {}
        self.countries[countryQID][diplo.QID] = diplo

        
class World:
    def __init__(self):
        self.operators = {}

    def add_diplomatic_representation(self, diplo):
        operatorQID = diplo.operatorQID
        if ( not self.operators.has_key(operatorQID)):
            self.operators[operatorQID] = Operator(diplo.operator, diplo.operatorQID)
        self.operators[operatorQID].add_diplomatic_representation(diplo)

world = World()

# Parse CSV file
csv = open('../../database_of_embassies.csv', 'r') 
csv_rows = csv.readlines() 
for csv_row in csv_rows:
    diplo = DiplomaticRepresentation(csv_row)
    world.add_diplomatic_representation(diplo)

index_file = open('../../../database-of-embassies.github.io/index.html', 'w')
index_file.write('<html><head><title>Database of embassies and consulates</title><meta name="viewport" content="width=device-width, initial-scale=1"></head><body>\n')
index_file.write('<h1>Database of embassies and consulates</h1>\n')
index_file.write('<p>This website aims to provide useful and accessible information about diplomatic representations. You can also <a href="https://github.com/database-of-embassies/database-of-embassies/blob/master/database_of_embassies.csv?raw=true">download the data as CSV</a> and even <a href="https://github.com/database-of-embassies/database-of-embassies">help us improve the data</a>.</p>\n')

# Output webpage of each diplomatic representation
for operator in world.operators.values():
    index_file.write('<h2>Diplomatic representations operated by ' + operator.name + '</h2>\n')
    index_file.write('<ul>\n')
    # print('operator: ' + str(operator))
    for country in operator.countries.values():
        # print('country: ' + str(country))
        for diplo in country.values():
            # print('diplo: ' + str(diplo))
            include_city = len(country) > 1
            include_jurisdiction = len(diplo.jurisdictions) > 0 #and diplo.jurisdictionQIDs != diplo.countryQID
            filename = diplo.url_name(include_city, include_jurisdiction) + '.html'
            path = '../../../database-of-embassies.github.io/' + filename
            if os.path.exists(path):
                QID1 = diplo.QID
                with open(path, 'r') as file:
                    html = file.read().replace('\n', '')
                    QID2 = re.search(r'http://www.wikidata.org/entity/Q[^"]*', html).group(0)
                    print('Error: Several diplomatic representations for path ' + path + ': ' + QID1 + ' ' + QID2)
            file = open(path, 'w')
            title = diplo.title(include_city, include_jurisdiction)
            file.write('<html><head><title>' + title + '</title><meta name="viewport" content="width=device-width, initial-scale=1"></head><body>\n')
            file.write('<h1>' + title + '</h1>\n')

            file.write('<p>Operated by ' + diplo.operator + ' in ')
            if diplo.city:
                file.write(diplo.city + ', ')
            file.write(diplo.country)
            if diplo.address:
                file.write('(address:' + diplo.address + ')')
            file.write('.</p>\n')

            if diplo.address:
                file.write('<p>Address:' + diplo.address + '</p>\n')
            if diplo.latitude and diplo.longitude:
                file.write('<p>Map: \n')
                file.write('<a href="https://www.openstreetmap.org/?mlat=' + diplo.latitude + '&mlon=' + diplo.longitude + '">OpenStreetMap</a>\n')
                file.write('<a href="https://www.google.com/maps/search/?api=1&query=' + diplo.latitude + ',' + diplo.longitude + '">Google Maps</a>\n')
                file.write('<a href="geo://' + diplo.latitude + ',' + diplo.longitude + '">geo protocol</a>\n') # Does not work on desktop browsers unfortunately
                file.write('</p>\n')
            if diplo.website:
                file.write('<p><a href="' + diplo.website + '">Official website</a></p>\n')
            if diplo.facebook:
                file.write('<p><a href="https://www.facebook.com/' + diplo.facebook + '">Official Facebook account</a></p>\n')
            if diplo.twitter:
                file.write('<p><a href="https://twitter.com/' + diplo.twitter + '">Official Twitter account</a></p>\n')
            if diplo.youtube:
                file.write('<p><a href="https://www.youtube.com/channel/' + diplo.youtube + '">Official YouTube account</a></p>\n')
            if diplo.picture:
                file.write('<p><a href="' + diplo.picture + '"><img src="' + diplo.picture + '" width="300"/></a><br/>\n')
	        if diplo.pictureLicense:
                    license = diplo.pictureLicense
                    if diplo.pictureLicenseURL:
                        license = '<a href="' + diplo.pictureLicenseURL + '">' + license + '</a>'
                    file.write('License: ' + license + '&nbsp;')
                file.write('Author: ' + diplo.pictureAuthor + '</p>\n')

            # TODO only if there are any
            # file.write('<p>Other diplomatic representations of ' + diplo.operator + ' in ' + diplo.country + ':\n')
            # file.write('<ul>\n')
            # for other_diplo in country.values():
            #     if(other_diplo == diplo):
            #         continue
            #     file.write('<li><a href="' + other_diplo.filename + '>' + other_diplo.city + '</a></li>\n')
            # file.write('</ul>\n')

            file.write('<p><i>Any error or missing information? Please improve <a href="' + diplo.QID + '">this Wikidata item</a>, or let us know on the <a href="https://github.com/database-of-embassies/database-of-embassies/issues">issue tracker</a>.<br/>\n')
            file.write('Public domain. Feel free to reuse this data in any way you want. Download the <a href="https://raw.githubusercontent.com/database-of-embassies/database-of-embassies/master/database_of_embassies.csv">whole CSV data</a> or browse <a href="index.html">other diplomatic representations</a>.</i></p>\n')
            file.write('<p><a href="' + diplo.QID + '"><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Wikidata_Stamp_Rec_Light.svg/200px-Wikidata_Stamp_Rec_Light.svg.png"/></a></p>\n')
            file.write('</body></html>\n')
            file.close()

            # Add this diplomatic representation to the index page
            index_file.write('<li><a href="' + filename + '">' + title + '</a></li>\n')
    index_file.write('</ul>\n')

# TODO index footer: download CSV, license, powered by, etc
index_file.write('</body></html>\n')
index_file.close()
