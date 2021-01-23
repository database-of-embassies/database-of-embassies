#!/usr/bin/python3

import sys
import re
import time
import urllib
import urllib.request, json
from urllib.request import urlopen, Request
from SPARQLWrapper import SPARQLWrapper, JSON

user_agent = "Database of embassies/%s.%s (https://github.com/database-of-embassies)" % (sys.version_info[0], sys.version_info[1])

def sanitize(s):
    return s.replace(";", ",").replace('\n', ' ')

sanitize_author_pattern_tag = re.compile("[^>]*>(.*)</[^<]*")
def sanitize_author(s):
    s = s.replace('\n', ' ') # New lines may interfere with regex
    if 'User:' in s:
        s = re.sub(r".*User:", '', s)
        s = s.replace(' (page does not exist)', '')
        return sanitize(re.sub(r'".*', '', s))
    if 'User_talk:' in s:
        s = re.sub(r'.*User talk:', '', s)
        return sanitize(re.sub(r'".*', '', s))
    if 'flickr.com' in s:
        s = re.sub(r".*flickr.com[^>]*>", '', s)
        return sanitize(re.sub(r'<.*', '', s))
    while sanitize_author_pattern_tag.match(s):
        s = sanitize_author_pattern_tag.match(s).group(1)
    return sanitize(s)

# TODO
# http://commons.wikimedia.org/wiki/Special:FilePath/Embassy%20of%20Russia%20in%20The%20Hague%20Klepkin%20%28cropped%29.jpg
# http://commons.wikimedia.org/wiki/Special:FilePath/Embassy%20of%20Russia%20in%20Havana%20-%20Nick%20De%20Marco.jpg
# http://commons.wikimedia.org/wiki/Special:FilePath/One%20Union%20Square.jpg
# <a href="//commons.wikimedia.org/w/index.php?title=User:Cookie_Nguyen&amp;action=edit&amp;redlink=1" class="new" title="User:Cookie Nguyen (page does not exist)">Cookie Nguyen</a>
#print(sanitize_author('a;b'))
#print(sanitize_author("""a
#b"""))
#print(sanitize_author('<a href="//commons.wikimedia.org/wiki/User:Southpark" title="User:Southpark">Dirk Ingo Franke</a>'))
#print(sanitize_author('<a href="//commons.wikimedia.org/wiki/User:%E5%BA%83%E7%80%AC%E5%B7%9D" title="User:広瀬川">広瀬川</a>'))
#print(sanitize_author('<a href="https://en.wikipedia.org/wiki/User:Denghu" class="extiw" title="wikipedia:User:Denghu">Denghu</a> at <a href="https://en.wikipedia.org/wiki/" class="extiw" title="wikipedia:">English <span title="free online encyclopedia that anyone can edit">Wikipedia</span></a>'))
#print(sanitize_author('<a rel="nofollow" class="external text" href="https://www.flickr.com/people/64379474@N00">Tilemahos Efthimiadis</a> from Athens, Greece'))
#print(sanitize_author('<a rel="nofollow" class="external text" href="https://www.flickr.com/photos/10440180@N03">Marijn de Vries Hoogerwerff</a> from <a href="https://en.wikipedia.org/wiki/Amsterdam" class="extiw" title="w:Amsterdam">Amsterdam</a>, <a href="https://en.wikipedia.org/wiki/Netherlands" class="extiw" title="w:Netherlands">the Netherlands</a>.'))
#print(sanitize_author('<a href="https://en.wikipedia.org/wiki/Department_of_Foreign_Affairs_(Philippines)" class="extiw" title="en:Department of Foreign Affairs (Philippines)">Department of Foreign Affairs</a>'))
#print(sanitize_author('44penguins (Angela M. Arnold)'))
#print(sanitize_author('Josh Lim (<a href="//commons.wikimedia.org/wiki/User:Sky_Harbor" title="User:Sky Harbor">Sky Harbor</a>)'))
#print(sanitize_author("""<table style="margin: 1.5em auto
#<p>Thank you to indicate this credit line next to the image in case of reuse:
#</p>
#<center>
#<b>Credit: Polymagou - CC-BY-SA</b>
#</center>
#<p><small><i>I'd appreciate if you could send a message on my <a href="//commons.wikimedia.org/wiki/User_talk:Polymagou" title="User talk:Polymagou">user talk page</a> if you use this picture out of the Wikimedia project scope <img alt="Face-smile.svg" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Face-smile.svg/20px-Face-smile.svg.png" decoding="async" width="20" height="20" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Face-smile.svg/30px-Face-smile.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Face-smile.svg/40px-Face-smile.svg.png 2x" data-file-width="48" data-file-height="48">.</i></small>
#</p>
#</td></tr></tbody></table>
#<p><br></p>"""))
#exit()

class Picture:
    def __init__(self, url, qidForDebuggingOnly):
         self.url = url
         self.artist = ''
         self.license = ''
         self.licenseURL = ''
         if url:
             filename = url[len('http://commons.wikimedia.org/wiki/Special:FilePath/'):] # Remove prefix
             request = 'https://commons.wikimedia.org/w/api.php?action=query&prop=imageinfo&iiprop=extmetadata&titles=File%3a' + filename + '&format=json'
             print('Commons request = ' + request)
             with urllib.request.urlopen(Request(request, headers={'User-Agent': user_agent})) as request_object:
                 response = json.loads(request_object.read().decode())
                 time.sleep(10) # Avoid overloading the Commons server
             print('Commons response = ' + str(response))
             page = list(response['query']['pages'].keys())[0]
             print(page)
             if page == '-1': # Happens for some deleted picture, for instance File:Dubai World Trade Centre (cropped).jpeg
                 print('Broken image ' + str(url) + ' used in Wikidata item ' + str(qidForDebuggingOnly))
                 self.url = '' # Consider the QID has not having a picture
                 return
             metadata = response['query']['pages'][page]['imageinfo'][0]['extmetadata']
             if 'Artist' in metadata:
                 self.artist = sanitize_author(metadata['Artist']['value'])
             if 'LicenseShortName' in metadata:
                 self.license = sanitize(metadata['LicenseShortName']['value'])
             if 'LicenseUrl' in metadata:
                 self.licenseURL = sanitize(metadata['LicenseUrl']['value'])

#picture = Picture('http://commons.wikimedia.org/wiki/Special:FilePath/Sign%20of%20the%20embassy%20of%20Afghanistan%20in%20the%20Hague%202016.jpg', 'Q12345')
#print(picture.artist)
#print(picture.license)
#print(picture.licenseURL)
#picture = Picture('http://commons.wikimedia.org/wiki/Special:FilePath/Dubai%20World%20Trade%20Centre%20(cropped).jpeg', 'Q12345')
#print(picture.artist)
#print(picture.license)
#print(picture.licenseURL)
#exit()


sparql_endpoint_url = "https://query.wikidata.org/sparql"
sparql = SPARQLWrapper(sparql_endpoint_url, agent=user_agent)
sparql.setReturnFormat(JSON)

with open('pois_for_operator.sparql', 'r') as file:
    query_template = file.read()

def get_operators():
    with open('operators.sparql', 'r') as file:
        query = file.read()
    return run_sparql(query)


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
    print('SPARQL response = ' + str(response))
    return response["results"]["bindings"]

def simplify(country, country_qid):
    """For brevity and usability, use common names of the countries, rather than their full name"""
    """Note: Malta and the Sovereign Military Order of Malta are two different things, the first is a country and the second is a sovereign religious order with no territory."""
    if country_qid.endswith("Q31354462"): return "Abkhazia"
    if country_qid.endswith("Q843186"): return "Japan"
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
        print('poi = ' + str(poi))
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
        qid = value(poi, "QID")
        picture = Picture(value(poi, "image"), qid)
        csv += picture.url + ";"
        csv += picture.artist + ";"
        csv += picture.license + ";"
        csv += picture.licenseURL + ";"
        csv += value(poi, "type") + ";"
        csv += value(poi, "typeQID") + ";"
        csv += value(poi, "inception") + ";"
        csv += qid
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
