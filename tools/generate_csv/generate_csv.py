#!/usr/bin/python3

import sys
import re
import time
import urllib
import urllib.request, json
from urllib.request import urlopen, Request
from SPARQLWrapper import SPARQLWrapper, JSON
from concurrent.futures import ThreadPoolExecutor
from os import makedirs
from typing import List
from pathlib import Path
<<<<<<< HEAD
import xml.etree.ElementTree
=======
>>>>>>> 84564713104e9f3d6c867acef80ccd69b0c0e567

user_agent = (
    "Database of embassies/%s.%s (https://github.com/database-of-embassies)"
    % (sys.version_info[0], sys.version_info[1])
)


def sanitize(s: str) -> str:
    return s.replace(";", ",").replace("\n", " ")

<<<<<<< HEAD

sanitize_author_pattern_tag = re.compile("[^>]*>(.*)</[^<]*")


def sanitize_author(s: str) -> str:
    s = s.replace("\n", " ")  # New lines may interfere with regex
    s = s.replace("\"","")  # got case were " was present ד"ר אבישי טייכר
    if "User:" in s:
        s = re.sub(r".*User:", "", s)
        s = s.replace(" (page does not exist)", "")
        return sanitize(re.sub(r'".*', "", s))
    if "User_talk:" in s:
        s = re.sub(r".*User talk:", "", s)
        return sanitize(re.sub(r'".*', "", s))
    if "flickr.com" in s:
        s = re.sub(r".*flickr.com[^>]*>", "", s)
        return sanitize(re.sub(r"<.*", "", s))
=======
def sanitize(s: str) -> str:
    return s.replace(";", ",").replace('\n', ' ')

sanitize_author_pattern_tag = re.compile("[^>]*>(.*)</[^<]*")
def sanitize_author(s: str) -> str:
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
>>>>>>> 84564713104e9f3d6c867acef80ccd69b0c0e567
    while sanitize_author_pattern_tag.match(s):
        s = sanitize_author_pattern_tag.match(s).group(1)
    if "<" in s:
        # remove html tag if there is still some left
        s = ''.join(xml.etree.ElementTree.fromstring(s).itertext())
    return sanitize(s)


# TODO
# http://commons.wikimedia.org/wiki/Special:FilePath/Embassy%20of%20Russia%20in%20The%20Hague%20Klepkin%20%28cropped%29.jpg
# http://commons.wikimedia.org/wiki/Special:FilePath/Embassy%20of%20Russia%20in%20Havana%20-%20Nick%20De%20Marco.jpg
# http://commons.wikimedia.org/wiki/Special:FilePath/One%20Union%20Square.jpg
# <a href="//commons.wikimedia.org/w/index.php?title=User:Cookie_Nguyen&amp;action=edit&amp;redlink=1" class="new" title="User:Cookie Nguyen (page does not exist)">Cookie Nguyen</a>
# print(sanitize_author('a;b'))
# print(sanitize_author("""a
# b"""))
# print(sanitize_author('<a href="//commons.wikimedia.org/wiki/User:Southpark" title="User:Southpark">Dirk Ingo Franke</a>'))
# print(sanitize_author('<a href="//commons.wikimedia.org/wiki/User:%E5%BA%83%E7%80%AC%E5%B7%9D" title="User:広瀬川">広瀬川</a>'))
# print(sanitize_author('<a href="https://en.wikipedia.org/wiki/User:Denghu" class="extiw" title="wikipedia:User:Denghu">Denghu</a> at <a href="https://en.wikipedia.org/wiki/" class="extiw" title="wikipedia:">English <span title="free online encyclopedia that anyone can edit">Wikipedia</span></a>'))
# print(sanitize_author('<a rel="nofollow" class="external text" href="https://www.flickr.com/people/64379474@N00">Tilemahos Efthimiadis</a> from Athens, Greece'))
# print(sanitize_author('<a rel="nofollow" class="external text" href="https://www.flickr.com/photos/10440180@N03">Marijn de Vries Hoogerwerff</a> from <a href="https://en.wikipedia.org/wiki/Amsterdam" class="extiw" title="w:Amsterdam">Amsterdam</a>, <a href="https://en.wikipedia.org/wiki/Netherlands" class="extiw" title="w:Netherlands">the Netherlands</a>.'))
# print(sanitize_author('<a href="https://en.wikipedia.org/wiki/Department_of_Foreign_Affairs_(Philippines)" class="extiw" title="en:Department of Foreign Affairs (Philippines)">Department of Foreign Affairs</a>'))
# print(sanitize_author('44penguins (Angela M. Arnold)'))
# print(sanitize_author('Josh Lim (<a href="//commons.wikimedia.org/wiki/User:Sky_Harbor" title="User:Sky Harbor">Sky Harbor</a>)'))
# print(sanitize_author("""<table style="margin: 1.5em auto
# <p>Thank you to indicate this credit line next to the image in case of reuse:
# </p>
# <center>
# <b>Credit: Polymagou - CC-BY-SA</b>
# </center>
# <p><small><i>I'd appreciate if you could send a message on my <a href="//commons.wikimedia.org/wiki/User_talk:Polymagou" title="User talk:Polymagou">user talk page</a> if you use this picture out of the Wikimedia project scope <img alt="Face-smile.svg" src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Face-smile.svg/20px-Face-smile.svg.png" decoding="async" width="20" height="20" srcset="https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Face-smile.svg/30px-Face-smile.svg.png 1.5x, https://upload.wikimedia.org/wikipedia/commons/thumb/7/79/Face-smile.svg/40px-Face-smile.svg.png 2x" data-file-width="48" data-file-height="48">.</i></small>
# </p>
# </td></tr></tbody></table>
# <p><br></p>"""))
# exit()


class Picture:
    def __init__(self, url: str, qidForDebuggingOnly: str):
<<<<<<< HEAD
        self.url = url
        self.artist = ""
        self.license = ""
        self.licenseURL = ""
        if url:
            filename = url[
                len("http://commons.wikimedia.org/wiki/Special:FilePath/") :
            ]  # Remove prefix
            request = (
                "https://commons.wikimedia.org/w/api.php?action=query&prop=imageinfo&iiprop=extmetadata&titles=File%3a"
                + filename
                + "&format=json"
            )
            print("Commons request = " + request)
            with urllib.request.urlopen(
                Request(request, headers={"User-Agent": user_agent})
            ) as request_object:
                response = json.loads(request_object.read().decode())
                time.sleep(10)  # Avoid overloading the Commons server
            print("Commons response = " + str(response))
            page = list(response["query"]["pages"].keys())[0]
            print(page)
            if (
                page == "-1"
            ):  # Happens for some deleted picture, for instance File:Dubai World Trade Centre (cropped).jpeg
                print(
                    "Broken image "
                    + str(url)
                    + " used in Wikidata item "
                    + str(qidForDebuggingOnly)
                )
                self.url = ""  # Consider the QID has not having a picture
                return
            metadata = response["query"]["pages"][page]["imageinfo"][0]["extmetadata"]
            if "Artist" in metadata:
                self.artist = sanitize_author(metadata["Artist"]["value"])
            if "LicenseShortName" in metadata:
                self.license = sanitize(metadata["LicenseShortName"]["value"])
            if "LicenseUrl" in metadata:
                self.licenseURL = sanitize(metadata["LicenseUrl"]["value"])


def get_operators(sparql):
    with open("operators.sparql", "r") as file:
        query = file.read()
    return run_sparql(sparql, query)
=======
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

def get_operators(sparql):
    with open('operators.sparql', 'r') as file:
        query = file.read()
    return run_sparql(sparql,query)
>>>>>>> 84564713104e9f3d6c867acef80ccd69b0c0e567


def value(poi, key) -> str:
    if key in poi:
        return sanitize(poi.get(key).get("value"))
    else:
        return ""


def coordinates(poi):
    match = re.match(r"Point\((.*) (.*)\)", value(poi, "coordinates"))
    if not match:
        return ";"  # Empty cells.
    latitude = match.group(2)
    longitude = match.group(1)
    return latitude + ";" + longitude

<<<<<<< HEAD

def run_sparql(sparql, query: str):
    print(f"SPARQL query = {query}")
    sparql.setQuery(query)
    response = sparql.query().convert()
    time.sleep(60)  # Avoid overloading the SPARQL server
=======
def run_sparql(sparql,query: str):
    print(f"SPARQL query = {query}")
    sparql.setQuery(query)
    response = sparql.query().convert()
    time.sleep(60) # Avoid overloading the SPARQL server
>>>>>>> 84564713104e9f3d6c867acef80ccd69b0c0e567
    print(f"SPARQL response = {response}")
    return response["results"]["bindings"]


def simplify(country, country_qid):
    """For brevity and usability, use common names of the countries, rather than their full name"""
    """Note: Malta and the Sovereign Military Order of Malta are two different things, the first is a country and the second is a sovereign religious order with no territory."""
    if country_qid.endswith("Q31354462"):
        return "Abkhazia"
    if country_qid.endswith("Q843186"):
        return "Japan"
    if country_qid.endswith("Q29999"):
        return "Netherlands"
    if country_qid.endswith("Q219060"):
        return "Palestine"
    if country_qid.endswith("Q705141"):
        return "Taiwan"
    if country_qid.endswith("Q5589404"):
        return "Taiwan"
    if country_qid.endswith("Q237"):
        return "Vatican"
    if country_qid.endswith("Q159583"):
        return "Vatican"
    return country

<<<<<<< HEAD

def get_pois_for_operator(sparql, operator_label: str, operator_qid) -> str:
    """Get embassies/etc for a given operator (usually a  country), example operator_qid: "http://www.wikidata.org/entity/Q17"."""
    query = query_template.replace("[OPERATOR]", "<" + operator_qid + ">")
    results = run_sparql(sparql, query)
    csv = ""
    for poi in results:
        print("poi = " + str(poi))
=======
def get_pois_for_operator(sparql, operator_label: str, operator_qid) -> str:
    """Get embassies/etc for a given operator (usually a  country), example operator_qid: "http://www.wikidata.org/entity/Q17"."""
    query = query_template.replace("[OPERATOR]", "<" + operator_qid + ">")
    results = run_sparql(sparql,query)
    csv = ""
    for poi in results:
        print('poi = ' + str(poi))
>>>>>>> 84564713104e9f3d6c867acef80ccd69b0c0e567
        csv += f"{simplify(sanitize(operator_label), operator_qid)};"
        csv += f"{operator_qid};"
        csv += f"{value(poi, 'jurisdictions')};"
        csv += f"{value(poi, 'jurisdictionQIDs')};"
        csv += f"{simplify(value(poi, 'country'), value(poi, 'countryQID'))};"
        csv += f"{value(poi, 'countryQID')};"
<<<<<<< HEAD
        csv += f"{value(poi, 'city').replace(';','')};"  # need to replace for some case example Washington ;D.C.
=======
        csv += f"{value(poi, 'city')};"
>>>>>>> 84564713104e9f3d6c867acef80ccd69b0c0e567
        csv += f"{value(poi, 'cityQID')};"
        csv += f"{coordinates(poi)};"
        csv += f"{value(poi, 'phone')};"
        csv += f"{value(poi, 'email')};"
        csv += f"{value(poi, 'website')};"
        csv += f"{value(poi, 'facebook')};"
        csv += f"{value(poi, 'twitter')};"
        csv += f"{value(poi, 'youtube')};"
        qid = value(poi, "QID")
        picture = Picture(value(poi, "image"), qid)
        csv += f"{picture.url};"
<<<<<<< HEAD
        csv += f"{picture.artist};" 
=======
        csv += f"{picture.artist};"
>>>>>>> 84564713104e9f3d6c867acef80ccd69b0c0e567
        csv += f"{picture.license};"
        csv += f"{picture.licenseURL};"
        csv += f"{value(poi, 'type')};"
        csv += f"{value(poi, 'typeQID')};"
        csv += f"{value(poi, 'inception')};"
        csv += qid
        csv += "\n"
    return csv


def write_tmp_csv(thread_id, operators):
<<<<<<< HEAD
    csv_file = open(f"tmp/database_of_embassies_{thread_id}.csv", "w")
=======
    csv_file = open(f"tmp/database_of_embassies_{thread_id}.csv", 'w')
>>>>>>> 84564713104e9f3d6c867acef80ccd69b0c0e567
    for operator in operators:
        print("=== operator ===")
        print(operator)
        operator_label = operator.get("operatorLabel").get("value")
        print("=== operator_label ===")
        print(operator_label)
        operator_qid = operator.get("operator").get("value")
        print("=== operator_qid ===")
        print(operator_qid)
        csv_file.write(get_pois_for_operator(sparql, operator_label, operator_qid))

<<<<<<< HEAD

def get_sublists(lst: List[str], n: int) -> List[List]:
    subListLength = len(lst) // n
    return [lst[i : i + subListLength] for i in range(0, len(lst), subListLength)]


if __name__ == "__main__":
=======
def get_sublists(lst: List[str],n: int) -> List[List]:
    subListLength = len(lst) // n 
    return [lst[i:i + subListLength] for i in range(0, len(lst), subListLength)]

if __name__ == "__main__":
    makedirs("tmp", exist_ok=True)
>>>>>>> 84564713104e9f3d6c867acef80ccd69b0c0e567
    sparql_endpoint_url = "https://query.wikidata.org/sparql"
    sparql = SPARQLWrapper(sparql_endpoint_url, agent=user_agent)
    sparql.setReturnFormat(JSON)

<<<<<<< HEAD
    with open("pois_for_operator.sparql", "r") as file:
        query_template = file.read()

    csv_file = open("database_of_embassies.csv", "w")
    columns_name = [
        "operator",
        "operatorQID",
        "jurisdictions",
        "jurisdictionQIDs",
        "country",
        "countryQID",
        "city",
        "cityQID",
        "latitude",
        "longitude",
        "phone",
        "email",
        "website",
        "facebook",
        "twitter",
        "youtube",
        "picture",
        "pictureAuthor",
        "pictureLicense",
        "pictureLicenseURL",
        "type",
        "typeQID",
        "creation",
        "QID",
    ]
    csv_file.write(f"{';'.join(columns_name)}\n")

    # print(get_pois_for_operator("http://www.wikidata.org/entity/Q242"))
    operators = get_operators(sparql)
    number_of_thread = 20
    makedirs("tmp", exist_ok=True)
=======
    with open('pois_for_operator.sparql', 'r') as file:
        query_template = file.read()
    
    csv_file = open('database_of_embassies.csv', 'w')
    columns_name = ["operator", "operatorQID","jurisdictions", "jurisdictionQIDs", "country", "countryQID", "city", "cityQID", "address", "latitude", "longitude","phone","email", "website", "facebook","twitter","youtube","picture","pictureAuthor","pictureLicenseURL","type", "typeQID","creation", "QID"]
    csv_file.write(f"{';'.join(columns_name)}\n")

    #print(get_pois_for_operator("http://www.wikidata.org/entity/Q242"))
    operators = get_operators(sparql)
    number_of_thread = 100
>>>>>>> 84564713104e9f3d6c867acef80ccd69b0c0e567
    with ThreadPoolExecutor(number_of_thread) as exe:
        # submit tasks to generate files
        for i, operators_batch in enumerate(get_sublists(operators, number_of_thread)):
            _ = [exe.submit(write_tmp_csv, i, operators_batch)]
<<<<<<< HEAD

    for tmp_file in list(Path("tmp").glob("*.csv")):
        csv_file.write(tmp_file.read_text())
        tmp_file.unlink()  # delete file now that they are concatened
=======
    
    for tmp_file in list(Path('tmp').glob('*.csv')):
        csv_file.write(tmp_file.read_text())
        tmp_file.unlink() # delete file now that they are concatened
>>>>>>> 84564713104e9f3d6c867acef80ccd69b0c0e567
