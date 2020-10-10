docker build -t dboe .
docker run -v $(pwd):/app -w /app -it --rm --name my-running-app dboe
mv database_of_embassies.csv ../../
osascript -e 'display notification "dboe: done"'
