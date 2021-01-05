find ../../../database-of-embassies.github.io -name "*.html" -print0 | xargs -0 rm
python generate_webpages.py
