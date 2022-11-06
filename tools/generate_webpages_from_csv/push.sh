if [[ $# -eq 0 ]] ; then
    echo 'Enter commit message as argument'
    exit 0
fi

MSG=$1

git add generate_webpages.py
git commit -m "$MSG"
git push

cd ../../../database-of-embassies.github.io/
git add "*.html"
git commit -m "$MSG"
git push
