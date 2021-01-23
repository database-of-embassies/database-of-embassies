#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR
docker build -t dboe .
docker run -v $(pwd):/app -w /app -it --rm --name dboe dboe
mv database_of_embassies.csv ../../
osascript -e 'display notification "dboe: done"'
