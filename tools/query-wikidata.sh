#!/bin/sh

SPARQL=$1
ONELINESPARQL=`echo $SPARQL | tr "\n" " "`

URL="https://query.wikidata.org/sparql?query=" # Wikidata SPARQL endpoint
URL="$URL PREFIX wd: <http://www.wikidata.org/entity/>" # Prefixes
URL="$URL PREFIX wdt: <http://www.wikidata.org/prop/direct/>"
URL="$URL $ONELINESPARQL"

OUT=/tmp/sparql
wget -O $OUT "$URL"

cat $OUT
