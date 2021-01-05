import os
import sys

def safe_for_url(string):
    return string.lower().replace(' ', '_').replace("'", '_')

class DiplomaticRepresentation:
    def __init__(self, csv_row):
        cells = csv_row.rstrip().split(';') # rstrip removes the trainling \n character.
        self.operator = cells[0]
        self.operatorQID = cells[1]
        self.jurisdictions = cells[2] # TODO split into array
        self.jurisdictionQIDs = cells[3] # TODO
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
        self.type = cells[18]
        self.typeQID = cells[19]
        self.creation = cells[20]
        self.QID = cells[21]

    def url_name(self, include_city, include_jurisdiction):
        if (include_city):
            name = safe_for_url(self.operator) + '_in_' + safe_for_url(self.city) + '_' + safe_for_url(self.country)
        else:
            name = safe_for_url(self.operator) + '_in_' + safe_for_url(self.country)
        if (include_jurisdiction):
            name += ' for ' + self.jurisdiction
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
index_file.write('<html><head><title>Database of embassies and consulates</title></head><body>\n')
index_file.write('<h1>Database of embassies and consulates</h1>\n')

# Output webpage of each diplomatic representation
for operator in world.operators.values():
    index_file.write('<h2>Diplomatic representations operated by ' + operator.name + '</h2>\n')
    index_file.write('<ul>\n')
    #print('operator: ' + str(operator))
    for country in operator.countries.values():
        #print('country: ' + str(country))
        for diplo in country.values():
            #print('diplo: ' + str(diplo))
            include_city = len(country) > 1
            include_jurisdiction = len(diplo.jurisdiction) > 1 and diplo.jurisdictionQID != diplo.countryQID
            filename = diplo.url_name(include_city, include_jurisdiction) + '.html'
            path = '../../../database-of-embassies.github.io/' + filename
            if (os.path.exists(path)):
                print('Error: Several diplomatic representations for path ' + path) # TODO output both QIDs, one by parsing the HTML file
            file = open(path, 'w')
            title = diplo.type + ' of ' + diplo.operator + ' in ' + diplo.country
            file.write('<html><title>' + title + '</title><body>\n')
            file.write('<h1>' + title + '</h1>\n')

            file.write('<p>Operated by ' + diplo.operator + ' in ')
            if (diplo.city):
                file.write(diplo.city + ', ')
            file.write(diplo.country)
            if (diplo.address):
                file.write('(address:' + diplo.address + ')')
            file.write('.</p>\n')

            # TODO only if there are any
            # file.write('<p>Other diplomatic representations of ' + diplo.operator + ' in ' + diplo.country + ':\n')
            # file.write('<ul>\n')
            # for other_diplo in country.values():
            #     if(other_diplo == diplo):
            #         continue
            #     file.write('<li><a href="' + other_diplo.filename + '>' + other_diplo.city + '</a></li>\n')
            # file.write('</ul>\n')

            if diplo.website:
                file.write('<p><a href="' + diplo.website + '">Official website</a></p>\n')

            file.write('<p><i>Any error or missing information? Please improve <a href="' + diplo.QID + '">this Wikidata item</a>, or let us know on the <a href="https://github.com/database-of-embassies/database-of-embassies/issues">issue tracker</a>.<br/>\n')
            file.write('Public domain. Feel free to reuse this data in any way you want. Download the <a href="https://raw.githubusercontent.com/database-of-embassies/database-of-embassies/master/database_of_embassies.csv">whole CSV data</a> or browse <a href="index.html">other diplomatic representations</a>.</i></p>\n')
            file.write('<p><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Wikidata_Stamp_Rec_Light.svg/200px-Wikidata_Stamp_Rec_Light.svg.png"/></p>\n')
            file.write('</body></html>\n')
            file.close()

            # Add this diplomatic representation to the index page
            index_file.write('<li><a href="' + filename + '">' + title + '</a></li>\n')
    index_file.write('</ul>\n')

# TODO index footer: download CSV, license, powered by, etc
index_file.write('</body></html>\n')
index_file.close()
