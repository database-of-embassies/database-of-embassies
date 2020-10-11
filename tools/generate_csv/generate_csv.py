#!/usr/bin/python3

import sys
import re
import time
from SPARQLWrapper import SPARQLWrapper, JSON

endpoint_url = "https://query.wikidata.org/sparql"
user_agent = "Database of embassies/%s.%s (https://github.com/database-of-embassies)" % (sys.version_info[0], sys.version_info[1])
sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
sparql.setReturnFormat(JSON)

with open('pois_for_operator.sparql', 'r') as file:
    query_template = file.read()

def get_operators():
    with open('operators.sparql', 'r') as file:
        query = file.read()
    return get_results(query)

def sanitize(s):
    return s.replace(";", ",")

def value(poi, key):
    if key in poi:
        return sanitize(poi.get(key).get("value"))
    else:
        return ""

def coordinates(poi):
    print("=== coordinates ===")
    print(poi)
    match = re.match(r"Point\((.*) (.*)\)", value(poi, "coordinates"))
    if not match:
        return ";" # Empty cells.
    latitude = match.group(2)
    longitude = match.group(1)
    return latitude + ";" + longitude

def get_results(query):
    print(query)
    sparql.setQuery(query)
    response = sparql.query().convert()
    time.sleep(60) # Avoid overloading the SPARQL server
    print(response)
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
    results = get_results(query)
    csv = ""
    for poi in results:
        csv += simplify(sanitize(operator_label), operator_qid) + ";"
        csv += operator_qid + ";"
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
        csv += value(poi, "image") + ";"
        csv += value(poi, "type") + ";"
        csv += value(poi, "typeQID") + ";"
        csv += value(poi, "inception") + ";"
        csv += value(poi, "QID")
        csv += "\n"
    return csv

csv_file = open('database_of_embassies.csv', 'w')
csv_file.write("operator;")
csv_file.write("operatorQID;")
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
