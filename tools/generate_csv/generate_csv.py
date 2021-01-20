#!/usr/bin/python3

import sys
import re
import time
import urllib
import urllib.request, json
from SPARQLWrapper import SPARQLWrapper, JSON

class Picture:
    def __init__(self, url):
         self.url = url
         self.artist = ''
         self.license = ''
         self.licenseURL = ''
         if url:
             filename = url[len('http://commons.wikimedia.org/wiki/Special:FilePath/'):] # Remove prefix
             request = 'https://commons.wikimedia.org/w/api.php?action=query&prop=imageinfo&iiprop=extmetadata&titles=File%3a' + filename + '&format=json'
             print('Commons request = ' + request)
             with urllib.request.urlopen(request) as request_object:
                 response = json.loads(request_object.read().decode())
                 time.sleep(10) # Avoid overloading the Commons server
             print('Commons response = ' + str(response))
             page = list(response['query']['pages'].keys())[0]
             #print('page = ' + str(page))
             metadata = response['query']['pages'][page]['imageinfo'][0]['extmetadata']
             if 'Artist' in metadata:
                 self.artist = metadata['Artist']['value']
             if 'LicenseShortName' in metadata:
                 self.license = metadata['LicenseShortName']['value']
             if 'LicenseUrl' in metadata:
                 self.licenseURL = metadata['LicenseUrl']['value']

#picture = Picture('Sign%20of%20the%20embassy%20of%20Afghanistan%20in%20the%20Hague%202016.jpg')
#print(picture.artist)
#print(picture.license)
#print(picture.licenseUrl)
#exit()

sparql_endpoint_url = "https://query.wikidata.org/sparql"
user_agent = "Database of embassies/%s.%s (https://github.com/database-of-embassies)" % (sys.version_info[0], sys.version_info[1])
sparql = SPARQLWrapper(sparql_endpoint_url, agent=user_agent)
sparql.setReturnFormat(JSON)

with open('pois_for_operator.sparql', 'r') as file:
    query_template = file.read()

def get_operators():
    with open('operators.sparql', 'r') as file:
        query = file.read()
    return run_sparql(query)

def sanitize(s):
    return s.replace(";", ",")

def value(poi, key):
    if key in poi:
        return sanitize(poi.get(key).get("value"))
    else:
        return ""

def coordinates(poi):
    match = re.match(r"Point\((.*) (.*)\)", value(poi, "coordinates"))
    if not match:
        return ";" # Empty cells.
    latitude = match.group(2)
    longitude = match.group(1)
    return latitude + ";" + longitude

def run_sparql(query):
    print('SPARQL query = ' + query)
    sparql.setQuery(query)
    response = sparql.query().convert()
    time.sleep(60) # Avoid overloading the SPARQL server
    print('SPARQL response = ' + response)
    return response["results"]["bindings"]

def simplify(country, country_qid):
    """For brevity and usability, use common names of the countries, rather than their full name"""
    if country_qid.endswith("Q31354462"): return "Abkhazia"
    if country_qid.endswith("Q843186"): return "Japan"
    if country_qid.endswith("Q190353"): return "Malta"
    if country_qid.endswith("Q29999"): return "Netherlands"
    if country_qid.endswith("Q219060"): return "Palestine"
    if country_qid.endswith("Q705141"): return "Taiwan"
    if country_qid.endswith("Q5589404"): return "Taiwan"
    if country_qid.endswith("Q237"): return "Vatican"
    if country_qid.endswith("Q159583"): return "Vatican"
    return country

def get_pois_for_operator(operator_label, operator_qid):
    """Get embassies/etc for a given operator (usually a  country), example operator_qid: "http://www.wikidata.org/entity/Q17"."""
    query = query_template.replace("[OPERATOR]", "<" + operator_qid + ">")
    results = run_sparql(query)
    csv = ""
    for poi in results:
        print('poi = ' + poi)
        csv += simplify(sanitize(operator_label), operator_qid) + ";"
        csv += operator_qid + ";"
        csv += value(poi, "jurisdictions") + ";"
        csv += value(poi, "jurisdictionQIDs") + ";"
        csv += simplify(value(poi, "country"), value(poi, "countryQID")) + ";"
        csv += value(poi, "countryQID") + ";"
        csv += value(poi, "city") + ";"
        csv += value(poi, "cityQID") + ";"
        csv += value(poi, "address") + ";"
        csv += coordinates(poi) + ";"
        csv += value(poi, "phone") + ";"
        csv += value(poi, "email") + ";"
        csv += value(poi, "website") + ";"
        csv += value(poi, "facebook") + ";"
        csv += value(poi, "twitter") + ";"
        csv += value(poi, "youtube") + ";"
        picture = Picture(value(poi, "image"))
        csv += picture.url + ";"
        csv += picture.artist + ";"
        csv += picture.license + ";"
        csv += picture.licenseURL + ";"
        csv += value(poi, "type") + ";"
        csv += value(poi, "typeQID") + ";"
        csv += value(poi, "inception") + ";"
        csv += value(poi, "QID")
        csv += "\n"
    return csv

csv_file = open('database_of_embassies.csv', 'w')
csv_file.write("operator;")
csv_file.write("operatorQID;")
csv_file.write("jurisdictions;")
csv_file.write("jurisdictionQIDs;")
csv_file.write("country;")
csv_file.write("countryQID;")
csv_file.write("city;")
csv_file.write("cityQID;")
csv_file.write("address;")
csv_file.write("latitude;")
csv_file.write("longitude;")
csv_file.write("phone;")
csv_file.write("email;")
csv_file.write("website;")
csv_file.write("facebook;")
csv_file.write("twitter;")
csv_file.write("youtube;")
csv_file.write("picture;")
csv_file.write("pictureAuthor;")
csv_file.write("pictureLicense;")
csv_file.write("pictureLicenseURL;")
csv_file.write("type;")
csv_file.write("typeQID;")
csv_file.write("creation;")
csv_file.write("QID;")
csv_file.write("\n")

#print(get_pois_for_operator("http://www.wikidata.org/entity/Q242"))
operators = get_operators()
for operator in operators:
    print("=== operator ===")
    print(operator)
    operator_label = operator.get("operatorLabel").get("value")
    print("=== operator_label ===")
    print(operator_label)
    operator_qid = operator.get("operator").get("value")
    print("=== operator_qid ===")
    print(operator_qid)
    csv_file.write(get_pois_for_operator(operator_label, operator_qid))
