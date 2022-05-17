git show HEAD:../../database_of_embassies.csv > /tmp/emb-original.txt
cat /tmp/emb-original.txt | tail -n +2 | sed -e "s/.*http/http/g" | sort > /tmp/emb-original-urls.txt
cat ../../database_of_embassies.csv | tail -n +2 | sed -e "s/.*http/http/g" | sort > /tmp/emb-local-urls.txt

#diff /tmp/emb-head.txt /tmp/emb-local.txt
#/Applications/Meld.app/Contents/MacOS/Meld /tmp/emb-head.txt /tmp/emb-local.txt

diff /tmp/emb-original-urls.txt /tmp/emb-local-urls.txt | grep "< " | sed -e "s/.*Q/Q/g" > /tmp/emb-removed.txt
cat /tmp/emb-removed.txt | while read QID
do
   grep $QID /tmp/emb-original.txt
done
