#!/bin/sh
# 
# Run a Wikidata query from command line.
# 
# Usage examples:
# 
# ./query-wikidata.sh "SELECT DISTINCT ?item WHERE {?item wdt:P31 wd:Q3917681. ?item wdt:P137 wd:Q16. ?item wdt:P131*/wdt:P17 wd:Q142.}"
# 
# OR this less convenient but more readable syntax:
# 
# echo "
#  SELECT DISTINCT
#    ?item
#  WHERE {
#    ?item wdt:P31 wd:Q3917681.
#    ?item wdt:P137 wd:Q16.
#    ?item wdt:P131*/wdt:P17 wd:Q142.
#  }
#  " |./query-wikidata.sh


# Read command-line argument
SPARQL=$1

# If no command-line argument, read from standard input
if [ -z "$SPARQL" ]
then
  SPARQL=$(cat)
fi

ONELINESPARQL=`echo $SPARQL | tr "\n" " "| sed 's/\//%2F/g'|sed 's/?/%3F/g'|sed 's/:/%3A/g'| sed 's/&/%26/g' | sed 's/=/%3D/g'`

URL="https://query.wikidata.org/sparql?query=" # Wikidata SPARQL endpoint
URL="$URL PREFIX wd: <http://www.wikidata.org/entity/>" # Prefixes
URL="$URL PREFIX wdt: <http://www.wikidata.org/prop/direct/>"
URL="$URL PREFIX p: <http://www.wikidata.org/prop/>"
URL="$URL PREFIX ps: <http://www.wikidata.org/prop/statement/>"
URL="$URL PREFIX pq: <http://www.wikidata.org/prop/qualifier/>"
#URL="$URL PREFIX wikibase: <http://wikiba.se/ontology#>" # Disabled these prefixes because they trigger a "Bad request" error from Wikidata
#URL="$URL PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>"
URL="$URL $ONELINESPARQL"

# HTMLize some possible query characters
URL=$(echo "$URL"|sed 's/(/%28/g'| sed 's/)/%29/g'| sed 's/*/%2a/g')

# Run HTTP request and send response to standard output
wget -O - "$URL"
