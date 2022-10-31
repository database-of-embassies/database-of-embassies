#!/usr/bin/env bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR
docker build -t dboe .
docker run -v $(pwd):/app -w /app -it --rm --name dboe dboe
mv -f database_of_embassies.csv ../../
case "$OSTYPE" in
  darwin*)  osascript -e 'display notification "dboe: done"' ;;
  linux*)   notify-send 'database embassy' 'csv generation done' ;;
  bsd*)     notify-send 'database embassy' 'csv generation done' ;;
  *)        echo "done" ;;
esac
