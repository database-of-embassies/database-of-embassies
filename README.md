# Database of embassies and consulates

Download [database_of_embassies.csv](https://raw.githubusercontent.com/database-of-embassies/database-of-embassies/master/database_of_embassies.csv) or [browse the data online](https://database-of-embassies.github.io).

![Powered by Wikidata](https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Wikidata_Stamp_Rec_Light.svg/200px-Wikidata_Stamp_Rec_Light.svg.png)

# Help needed

**Non-developers:** The database is not complete, we need your help to improve it. To add/modify/remove information, please edit the relevant item in [Wikidata](http://wikidata.org) ([example](https://www.wikidata.org/wiki/Q2841718)). If no item is available on Wikidata, please create it. Also, go check physically whether each embassy still exists or not, and if not please [tell us here](https://github.com/nicolas-raoul/database-of-embassies/issues/new). Thanks!

- [Add an "operator" to embassies that lack one](https://query.wikidata.org/#%23%20Diplomatic%20missions%20with%20no%20operator.%0ASELECT%20DISTINCT%0A%09%3FQID%20%28SAMPLE%28COALESCE%28%3Fen_label%2C%20%3Fitem_label%29%29%20as%20%3Flabel%29%0A%09%28SAMPLE%28%3Ftype_label%29%20as%20%3Ftype%29%0A%09%28SAMPLE%28%3Fcountry_label%29%20as%20%3Fcountry%29%09%0AWHERE%20%7B%0A%09%23%20Any%20type%20of%20embassy%20or%20consulate%0A%09%7B%3FQID%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279%2a%20wd%3AQ3917681%7D%0A%09UNION%20%7B%3FQID%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279%2a%20wd%3AQ5244910%7D%0A%09UNION%20%7B%3FQID%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279%2a%20wd%3AQ7843791%7D%0A%09UNION%20%7B%3FQID%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279%2a%20wd%3AQ61881945%7D%0A%09UNION%20%7B%3FQID%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279%2a%20wd%3AQ18414273%7D%0A%09UNION%20%7B%3FQID%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279%2a%20wd%3AQ73088858%7D%0A%20%20%0A%20%20%09%23%20Exclude%20places%20that%20are%20not%20in%20operation%20anymore%0A%09MINUS%20%7B%3FQID%20wdt%3AP582%20%3Fendtime%7D%0A%09MINUS%20%7B%3FQID%20wdt%3AP576%20%3FdissolvedOrAbolished%7D%0A%09MINUS%20%7B%3FQID%20p%3AP31%20%3FinstanceStatement.%20%3FinstanceStatement%20pq%3AP582%20%3FendtimeQualifier%7D%0A%09%0A%20%20%20%20%23%20No%20operator%0A%20%20%20%20MINUS%7B%0A%20%20%20%20%20%20%7B%3FQID%20wdt%3AP137%20%3FoperatorId.%7D%0A%20%20%20%20%20%20UNION%0A%20%20%20%20%20%20%7B%3FQID%20p%3AP31%2Fps%3AP31%20%3Fnunciature.%20%3Fnunciature%20wdt%3AP137%20%3FoperatorId.%7D%0A%20%20%20%20%7D%0A%20%20%0A%20%20%23%20Label%0A%09OPTIONAL%20%7B%3FQID%20rdfs%3Alabel%20%3Fen_label%20.%20FILTER%28LANG%28%3Fen_label%29%20%3D%20%22en%22%29%7D%0A%20%20%20%20OPTIONAL%20%7B%3FQID%20rdfs%3Alabel%20%3Fitem_label%7D%0A%7D%20GROUP%20BY%20%3FQID)
- [Add a "located in the administrative territorial entity" to embassies that lack one](https://query.wikidata.org/#%23Embassies%2Fconsulates%20with%20no%20location%0ASELECT%20%3FQID%20%28SAMPLE%28COALESCE%28%3Fen_label%2C%20%3Fitem_label%29%29%20as%20%3Flabel%29%0AWHERE%0A%7B%0A%09%23%20Any%20type%20of%20embassy%20or%20consulate%0A%09%7B%3FQID%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279%2a%20wd%3AQ3917681%7D%0A%09UNION%20%7B%3FQID%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279%2a%20wd%3AQ5244910%7D%0A%09UNION%20%7B%3FQID%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279%2a%20wd%3AQ7843791%7D%0A%09UNION%20%7B%3FQID%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279%2a%20wd%3AQ61881945%7D%0A%09UNION%20%7B%3FQID%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279%2a%20wd%3AQ18414273%7D%0A%09UNION%20%7B%3FQID%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279%2a%20wd%3AQ73088858%7D%0A%20%20%0A%20%20%09%23%20Exclude%20places%20that%20are%20not%20in%20operation%20anymore%0A%09MINUS%20%7B%3FQID%20wdt%3AP582%20%3Fendtime%7D%0A%09MINUS%20%7B%3FQID%20wdt%3AP576%20%3FdissolvedOrAbolished%7D%0A%09MINUS%20%7B%3FQID%20p%3AP31%20%3FinstanceStatement.%20%3FinstanceStatement%20pq%3AP582%20%3FendtimeQualifier%7D%0A%0A%20%20%20%20%23%20No%20country%0A%09MINUS%20%7B%3FQID%20wdt%3AP131%2a%2Fwdt%3AP17%20%3FcountryId.%7D%0A%20%20%0A%20%20%20%20%23%20Label%0A%09OPTIONAL%20%7B%3FQID%20rdfs%3Alabel%20%3Fen_label%20.%20FILTER%28LANG%28%3Fen_label%29%20%3D%20%22en%22%29%7D%0A%20%20%20%20OPTIONAL%20%7B%3FQID%20rdfs%3Alabel%20%3Fitem_label%7D%0A%7D%20%0AGROUP%20BY%20%3FQID)
- [Add a jurisdiction (area that the embassy covers) to embassies that lack one](https://query.wikidata.org/#%23%20Embassies%2Fconsulates%20with%20no%20jurisdiction%0A%23%20This%20can%20be%20tricky%20to%20find%2C%20please%20add%20solid%20references%20%28ideally%20the%20embassy%2Fetc%27s%20website%29%0ASELECT%20%3FQID%20%28SAMPLE%28COALESCE%28%3Fen_label%2C%20%3Fitem_label%29%29%20as%20%3Flabel%29%0AWHERE%0A%7B%0A%09%23%20Any%20type%20of%20embassy%20or%20consulate%0A%09%7B%3FQID%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279%2a%20wd%3AQ3917681%7D%0A%09UNION%20%7B%3FQID%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279%2a%20wd%3AQ5244910%7D%0A%09UNION%20%7B%3FQID%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279%2a%20wd%3AQ7843791%7D%0A%09UNION%20%7B%3FQID%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279%2a%20wd%3AQ61881945%7D%0A%09UNION%20%7B%3FQID%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279%2a%20wd%3AQ18414273%7D%0A%09UNION%20%7B%3FQID%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279%2a%20wd%3AQ73088858%7D%0A%20%20%0A%20%20%09%23%20Exclude%20places%20that%20are%20not%20in%20operation%20anymore%0A%09MINUS%20%7B%3FQID%20wdt%3AP582%20%3Fendtime%7D%0A%09MINUS%20%7B%3FQID%20wdt%3AP576%20%3FdissolvedOrAbolished%7D%0A%09MINUS%20%7B%3FQID%20p%3AP31%20%3FinstanceStatement.%20%3FinstanceStatement%20pq%3AP582%20%3FendtimeQualifier%7D%0A%0A%20%20%20%20%23%20No%20jurisdiction%0A%09MINUS%20%7B%3FQID%20wdt%3AP1001%20%3FjurisdictionQID.%7D%0A%20%20%0A%20%20%20%20%23%20Label%0A%09OPTIONAL%20%7B%3FQID%20rdfs%3Alabel%20%3Fen_label%20.%20FILTER%28LANG%28%3Fen_label%29%20%3D%20%22en%22%29%7D%0A%20%20%20%20OPTIONAL%20%7B%3FQID%20rdfs%3Alabel%20%3Fitem_label%7D%0A%7D%20%0AGROUP%20BY%20%3FQID)
- [Add a picture to embassies lacking one](https://fist.toolforge.org/wdfist/?depth=3&language=en&project=wikipedia&sparql=SELECT%20DISTINCT%20?QID%20WHERE%20{%20{%20?QID%20p:P31/ps:P31/wdt:P279*%20wd:Q3917681}%20UNION%20{%20?QID%20wdt:P31%20wd:Q7843791}%20UNION%20{?QID%20p:P31/ps:P31/wdt:P279*%20wd:Q7843791}%20UNION%20{?QID%20p:P31/ps:P31/wdt:P279*%20wd:Q61881945}%20UNION%20{?QID%20p:P31/ps:P31/wdt:P279*%20wd:Q18414273}%20UNION%20{?QID%20p:P31/ps:P31/wdt:P279*%20wd:Q73088858}%20MINUS%20{?QID%20wdt:P18%20?image}%20}%20&no_images_only=1&prefilled=1)
- [Go photograph embassies that do not have a picture in Wikimedia Commons](https://tools.wmflabs.org/wikishootme/#lat=0&lng=0&zoom=1&layers=wikidata_no_image&worldwide=1&sparql_filter=%7B%3Fq%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279*%20wd%3AQ3917681%7DUNION%7B%3Fq%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279*%20wd%3AQ7843791%7D%3Fq%20wdt%3AP625%20%3Flocation.MINUS%7B%3Fq%20wdt%3AP18%20%3Fimage%7DMINUS%20%7B%3Fq%20wdt%3AP582%20%3Fendtime%7DMINUS%7B%3Fq%20wdt%3AP582%20%3FdissolvedOrAbolished%7DMINUS%7B%3Fq%20p%3AP31%20%3FinstanceStatement.%3FinstanceStatement%20pq%3AP582%20%3FendtimeQualifier%7DFILTER%20NOT%20EXISTS%7B%3Fq%20p%3AP131%2F(ps%3AP131%2Fp%3AP131)*%20%3Fstatement.%3Fstatement%20ps%3AP131%20%3Farea.%3Fq%20p%3AP131%2F(ps%3AP131%2Fp%3AP131)*%20%3FintermediateStatement.%3FintermediateStatement%20(ps%3AP131%2Fp%3AP131)*%20%3Fstatement.%3FintermediateStatement%20pq%3AP582%20%3FendTime%7D) (takes a minute to load)
- [Tidy up operator/country](https://query.wikidata.org/#%23Embassies%2Fconsulates%20with%20the%20same%20QID%20for%20operator%20and%20country.%20It%20should%20never%20be%20the%20same.%0ASELECT%20%3FQID%20%28SAMPLE%28COALESCE%28%3Fen_label%2C%20%3FQID_label%29%29%20as%20%3Flabel%29%0AWHERE%0A%7B%0A%09%23%20Any%20type%20of%20embassy%20or%20consulate%0A%09%7B%3FQID%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279%2a%20wd%3AQ3917681%7D%0A%09UNION%20%7B%3FQID%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279%2a%20wd%3AQ5244910%7D%0A%09UNION%20%7B%3FQID%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279%2a%20wd%3AQ7843791%7D%0A%09UNION%20%7B%3FQID%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279%2a%20wd%3AQ61881945%7D%0A%09UNION%20%7B%3FQID%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279%2a%20wd%3AQ18414273%7D%0A%09UNION%20%7B%3FQID%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279%2a%20wd%3AQ73088858%7D%0A%20%0A%20%7B%3FQID%20wdt%3AP137%20%3Foperator%7D%0A%20UNION%0A%20%7B%3FQID%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279%2a%20%3Fparent.%20%3Fparent%20wdt%3AP137%20%3Foperator.%7D%20%23%20Case%20of%20apostolic%20nunciatures%0A%20%0A%20%3FQID%20wdt%3AP131%2a%2Fwdt%3AP17%20%3Foperator.%20%23%20Country%20same%20as%20operator%0A%20%0A%09OPTIONAL%20%7B%3FQID%20rdfs%3Alabel%20%3Fen_label%20.%20FILTER%28LANG%28%3Fen_label%29%20%3D%20%22en%22%29%7D%0A%20OPTIONAL%20%7B%3FQID%20rdfs%3Alabel%20%3FQID_label%7D%0A%7D%0AGROUP%20BY%20%3FQID)
- [Merge potentially duplicate embassies (same operator in same country)](https://query.wikidata.org/#SELECT%20DISTINCT%0A%09%3FcountryId%20%3FoperatorId%20%3Fitem1%20%3Fitem2%20%3Flabel1%20%3Flabel2%0AWHERE%20%7B%0A%20%20%20%20%23%20Embassies...%0A%09%3Fitem1%20wdt%3AP31%20wd%3AQ3917681.%20%3Fitem1%20rdfs%3Alabel%20%3Flabel1.%20FILTER%20%28lang%28%3Flabel1%29%20%3D%20%22en%22%29.%0A%09%3Fitem2%20wdt%3AP31%20wd%3AQ3917681.%20%3Fitem2%20rdfs%3Alabel%20%3Flabel2.%20FILTER%20%28lang%28%3Flabel2%29%20%3D%20%22en%22%29.%0A%20%20%0A%20%20%20%20%23%20in%20the%20same%20country...%0A%09%3Fitem1%20wdt%3AP17%20%3FcountryId.%0A%09%3Fitem2%20wdt%3AP17%20%3FcountryId.%0A%09%0A%20%20%20%20%23%20by%20the%20same%20operator.%0A%09%3Fitem1%20wdt%3AP137%20%3FoperatorId.%0A%09%3Fitem2%20wdt%3AP137%20%3FoperatorId.%0A%0A%20%20%20%20%23%20Ignore%20embassies%20that%20are%20marked%20as%20ended.%0A%20%20%20%20MINUS%20%7B%3Fitem1%20wdt%3AP582%20%3Fendtime1.%7D%09%20%20%20%20MINUS%20%7B%3Fitem1%20wdt%3AP576%20%3FdissolvedOrAbolished1.%7D%0A%09MINUS%20%7B%3FinstanceStatement1%20pq%3AP582%20%3FendtimeQualifier1.%7D%09%3Fitem1%20p%3AP31%20%3FinstanceStatement1.%0A%20%20%20%20MINUS%20%7B%3Fitem2%20wdt%3AP582%20%3Fendtime2.%7D%09%20%20%20%20MINUS%20%7B%3Fitem2%20wdt%3AP576%20%3FdissolvedOrAbolished2.%7D%0A%09MINUS%20%7B%3FinstanceStatement2%20pq%3AP582%20%3FendtimeQualifier2.%7D%09%3Fitem2%20p%3AP31%20%3FinstanceStatement2.%0A%20%20%0A%09FILTER%20%28%3Fitem1%20%21%3D%20%3Fitem2%29.%0A%7D)
- [Find potential embassies](https://query.wikidata.org/#%23%20Items%20that%20have%20%22embassy%22%20in%20the%20label%20but%20are%20not%20an%20instance%20of%20embassy.%0A%23%20Most%20of%20them%20are%20really%20not%20embassies%2C%20but%20some%20might%20be%20actual%20embassies%2C%20so%20it%20is%20worth%20checking.%0ASELECT%20DISTINCT%0A%09%3Fitem%20%3FitemLabel%0AWHERE%20%7B%0A%20%20%20%20hint%3AQuery%20hint%3Aoptimizer%20%22None%22.%0A%20%20%20%20SERVICE%20wikibase%3Amwapi%20%7B%0A%20%20%20%20%20%20%20%20bd%3AserviceParam%20wikibase%3Aapi%20%22Search%22%3B%0A%20%20%20%20%20%20%20%20wikibase%3Aendpoint%20%22www.wikidata.org%22%3B%0A%20%20%20%20%20%20%20%20mwapi%3Asrsearch%20%22Embassy%22.%0A%20%20%20%20%20%20%20%20%3Ftitle%20wikibase%3AapiOutput%20mwapi%3Atitle.%0A%20%20%20%20%7D%0A%20%20%20%20BIND%28IRI%28CONCAT%28STR%28wd%3A%29%2C%20%3Ftitle%29%29%20AS%20%3Fitem%29%0A%20%20%20%20%3Fitem%20rdfs%3Alabel%20%3FitemLabel%20.%20filter%28lang%28%3FitemLabel%29%3D%22en%22%29%0A%20%20%20%20FILTER%28regex%28%3FitemLabel%2C%22Embassy.%2B%22%29%29%0A%20%20%0A%20%20%09%23%20Not%20an%20embassy%0A%09MINUS%20%7B%3Fitem%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279%2a%20wd%3AQ3917681%7D%0A%20%20%20%20%23%20Not%20a%20defunct%20diplomatic%20mission%0A%20%20%20%20MINUS%20%7B%3Fitem%20p%3AP279%20wd%3AQ80905563%7D%0A%20%20%20%20%23%20Does%20not%20have%20an%20occupant%20%28cases%20where%20the%20building%20and%20the%20embassy%20have%20separate%20Wikidata%20items%29%0A%09MINUS%20%7B%3Fitem%20p%3AP466%20%3Foccupant%7D%0A%20%20%20%20%23%20Not%20a%20disambiguation%20page%20%28which%20lists%20all%20embassies%20of%20a%20country%29%0A%20%20%20%20MINUS%20%7B%3Fitem%20p%3AP31%20wd%3AQ4167410%7D%0A%20%20%20%20MINUS%20%7B%3Fitem%20p%3A31%20wd%3AQ13406463%7D%0A%7D)
- [Fill in the blanks using TABernacle](https://goo.gl/Umwpgz)
<!-- - [Add an image to embassies that have a Commons category but no image](https://query.wikidata.org/#SELECT%20DISTINCT%0A%09%3Fwikidata%20%3Fcommons%0AWHERE%20%7B%0A%09%7B%20%3Fwikidata%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279%2a%20wd%3AQ3917681.%20%7D%20UNION%20%7B%20%3Fwikidata%20wdt%3AP31%20wd%3AQ7843791.%20%7D%20%23%20Embassy%20or%20consulate%0A%09%3Fwikidata%20wdt%3AP373%20%3Fcommons%0A%09MINUS%20%7B%3Fwikidata%20wdt%3AP18%20%3Fimage.%7D%0A%7D) -->

**Developers:** Take 10 minutes to familiarize yourself with [SPARQL](https://www.wikidata.org/wiki/Wikidata:SPARQL_query_service/queries) then [pick any issue](https://github.com/nicolas-raoul/database-of-embassies/issues) you like :-) Don't hesitate to create other issues to document any problem with the data, or send pull requests to add your custom scripts. Convenient tools: [QuickStatements](https://tools.wmflabs.org/wikidata-todo/quick_statements.php), [Harvest Templates](https://tools.wmflabs.org/pltools/harvesttemplates/).

# Visualizations
- Map of [consulates and embassies around the world](https://query.wikidata.org/#%23Embassies%20and%20consulates%0A%23defaultView%3AMap%0ASELECT%20DISTINCT%0A%09%28SAMPLE%28%3Fcountry_label%29%20as%20%3Fcountry%29%20%20%20%28SAMPLE%28%3Fcity_label%29%20as%20%3Fcity%29%20%20%20%28SAMPLE%28%3Faddress%29%20as%20%3Faddress%29%20%28SAMPLE%28%3Fcoordinates%29%20as%20%3Fcoordinates%29%0A%09%28SAMPLE%28%3Foperator_label%29%20as%20%3Flayer%29%20%28SAMPLE%28%3Ftype_label%29%20as%20%3Ftype%29%20%20%20%28SAMPLE%28%3Fphone%29%20as%20%3Fphone%29%20%20%20%20%20%28SAMPLE%28%3Femail%29%20as%20%3Femail%29%0A%09%28SAMPLE%28%3Fwebsite%29%20as%20%3Fwebsite%29%20%20%20%20%20%20%20%20%20%28SAMPLE%28%3Fimage%29%20as%20%3Fimage%29%20%20%20%20%20%20%20%3Fwikidata%0A%09%23%28SAMPLE%28%3Ffacebook%29%20as%20%3Ffacebook%29%20%28SAMPLE%28%3Ftwitter%29%20as%20%3Ftwitter%29%20%28SAMPLE%28%3Fyoutube%29%20as%20%3Fyoutube%29%20%28SAMPLE%28%3Finception%29%20as%20%3Finception%29%20%28SAMPLE%28%3FdissolvedOrAbolished%29%20as%20%3FdissolvedOrAbolished%29%0AWHERE%20%7B%0A%09%7B%20%3Fwikidata%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279%2a%20wd%3AQ3917681.%20%7D%20UNION%20%7B%20%3Fwikidata%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279%2a%20wd%3AQ7843791.%20%7D%20%23%20Embassy%20or%20consulate%0A%09%3Fwikidata%20p%3AP31%2Fps%3AP31%20%3FtypeId.%20%3FtypeId%20rdfs%3Alabel%20%3Ftype_label.%20filter%20%28lang%28%3Ftype_label%29%20%3D%20%22en%22%29.%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP131%2a%2Fwdt%3AP17%20%3FcountryId.%20%3FcountryId%20rdfs%3Alabel%20%3Fcountry_label.%20filter%20%28lang%28%3Fcountry_label%29%20%3D%20%22en%22%29.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP131%20%3FcityId.%20%3FcityId%20rdfs%3Alabel%20%3Fcity_label.%20filter%20%28lang%28%3Fcity_label%29%20%3D%20%22en%22%29.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP969%20%3Faddress.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP625%20%3Fcoordinates.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP137%20%3FoperatorId.%20%3FoperatorId%20rdfs%3Alabel%20%3Foperator_label.%20filter%20%28lang%28%3Foperator_label%29%20%3D%20%22en%22%29.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP1329%20%3Fphone.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP968%20%3Femail.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP856%20%3Fwebsite.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP2013%20%3Ffacebook.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP2002%20%3Ftwitter.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP2397%20%3Fyoutube.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP18%20%3Fimage.%7D%0A%20%20%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP571%20%3Finception.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP576%20%3FdissolvedOrAbolished.%7D%0A%7D%20GROUP%20BY%20%3Fwikidata%20ORDER%20BY%20ASC%28%3Fcountry%29%20ASC%28%3Fcity%29%20ASC%28%3Foperator%29%20DESC%28%3Ftype%29)
- Visualize [what countries have a diplomatic representation in what countries](https://query.wikidata.org/#%23defaultView%3ADimensions%0ASELECT%20DISTINCT%0A%09%28SAMPLE%28%3Foperator_label%29%20as%20%3Foperator%29%20%28SAMPLE%28%3Fcountry_label%29%20as%20%3Fcountry%29%0AWHERE%20%7B%0A%09%7B%20%3Fwikidata%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279%2a%20wd%3AQ3917681.%20%7D%20UNION%20%7B%20%3Fwikidata%20wdt%3AP31%20wd%3AQ7843791.%20%7D%20%23%20Embassy%20or%20consulate%0A%09%3Fwikidata%20p%3AP31%2Fps%3AP31%20%3FtypeId.%20%3FtypeId%20rdfs%3Alabel%20%3Ftype_label.%20filter%20%28lang%28%3Ftype_label%29%20%3D%20%22en%22%29.%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP131%2a%2Fwdt%3AP17%20%3FcountryId.%20%3FcountryId%20rdfs%3Alabel%20%3Fcountry_label.%20filter%20%28lang%28%3Fcountry_label%29%20%3D%20%22en%22%29.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP137%20%3FoperatorId.%20%3FoperatorId%20rdfs%3Alabel%20%3Foperator_label.%20filter%20%28lang%28%3Foperator_label%29%20%3D%20%22en%22%29.%7D%0A%7D%20GROUP%20BY%20%3Fwikidata)
- Gallery of [pictures of diplomatic buildings](https://query.wikidata.org/#%23Embassies%20and%20consulates%0A%23defaultView%3AImageGrid%0ASELECT%20DISTINCT%0A%09%28SAMPLE%28%3Fcountry_label%29%20as%20%3Fcountry%29%20%20%20%28SAMPLE%28%3Fcity_label%29%20as%20%3Fcity%29%20%20%20%28SAMPLE%28%3Faddress%29%20as%20%3Faddress%29%20%28SAMPLE%28%3Fcoordinates%29%20as%20%3Fcoordinates%29%0A%09%28SAMPLE%28%3Foperator_label%29%20as%20%3Foperator%29%20%28SAMPLE%28%3Ftype_label%29%20as%20%3Ftype%29%20%20%20%28SAMPLE%28%3Fphone%29%20as%20%3Fphone%29%20%20%20%20%20%28SAMPLE%28%3Femail%29%20as%20%3Femail%29%0A%09%28SAMPLE%28%3Fwebsite%29%20as%20%3Fwebsite%29%20%20%20%20%20%20%20%20%20%28SAMPLE%28%3Fimage%29%20as%20%3Fimage%29%20%20%20%20%20%20%20%3Fwikidata%0A%09%28SAMPLE%28%3Ffacebook%29%20as%20%3Ffacebook%29%20%28SAMPLE%28%3Ftwitter%29%20as%20%3Ftwitter%29%20%28SAMPLE%28%3Fyoutube%29%20as%20%3Fyoutube%29%20%28SAMPLE%28%3Finception%29%20as%20%3Finception%29%20%28SAMPLE%28%3FdissolvedOrAbolished%29%20as%20%3FdissolvedOrAbolished%29%0AWHERE%20%7B%0A%09%7B%20%3Fwikidata%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279%2a%20wd%3AQ3917681.%20%7D%20UNION%20%7B%20%3Fwikidata%20wdt%3AP31%20wd%3AQ7843791.%20%7D%20%23%20Embassy%20or%20consulate%0A%09%3Fwikidata%20p%3AP31%2Fps%3AP31%20%3FtypeId.%20%3FtypeId%20rdfs%3Alabel%20%3Ftype_label.%20filter%20%28lang%28%3Ftype_label%29%20%3D%20%22en%22%29.%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP131%2a%2Fwdt%3AP17%20%3FcountryId.%20%3FcountryId%20rdfs%3Alabel%20%3Fcountry_label.%20filter%20%28lang%28%3Fcountry_label%29%20%3D%20%22en%22%29.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP131%20%3FcityId.%20%3FcityId%20rdfs%3Alabel%20%3Fcity_label.%20filter%20%28lang%28%3Fcity_label%29%20%3D%20%22en%22%29.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP969%20%3Faddress.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP625%20%3Fcoordinates.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP137%20%3FoperatorId.%20%3FoperatorId%20rdfs%3Alabel%20%3Foperator_label.%20filter%20%28lang%28%3Foperator_label%29%20%3D%20%22en%22%29.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP1329%20%3Fphone.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP968%20%3Femail.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP856%20%3Fwebsite.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP2013%20%3Ffacebook.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP2002%20%3Ftwitter.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP2397%20%3Fyoutube.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP18%20%3Fimage.%7D%0A%20%20%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP571%20%3Finception.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP576%20%3FdissolvedOrAbolished.%7D%0A%7D%20GROUP%20BY%20%3Fwikidata%20ORDER%20BY%20ASC%28%3Fcountry%29%20ASC%28%3Fcity%29%20ASC%28%3Foperator%29%20DESC%28%3Ftype%29)
- Timeline of the [inception and dissolution](https://query.wikidata.org/#%23Embassies%20and%20consulates%0A%23defaultView%3ATimeline%0ASELECT%20DISTINCT%0A%09%28SAMPLE%28%3Fcountry_label%29%20as%20%3Fcountry%29%20%20%20%28SAMPLE%28%3Fcity_label%29%20as%20%3Fcity%29%20%20%20%28SAMPLE%28%3Faddress%29%20as%20%3Faddress%29%20%28SAMPLE%28%3Fcoordinates%29%20as%20%3Fcoordinates%29%0A%09%28SAMPLE%28%3Foperator_label%29%20as%20%3Foperator%29%20%28SAMPLE%28%3Ftype_label%29%20as%20%3Ftype%29%20%20%20%28SAMPLE%28%3Fphone%29%20as%20%3Fphone%29%20%20%20%20%20%28SAMPLE%28%3Femail%29%20as%20%3Femail%29%0A%09%28SAMPLE%28%3Fwebsite%29%20as%20%3Fwebsite%29%20%20%20%20%20%20%20%20%20%28SAMPLE%28%3Fimage%29%20as%20%3Fimage%29%20%20%20%20%20%20%20%3Fwikidata%0A%09%28SAMPLE%28%3Ffacebook%29%20as%20%3Ffacebook%29%20%28SAMPLE%28%3Ftwitter%29%20as%20%3Ftwitter%29%20%28SAMPLE%28%3Fyoutube%29%20as%20%3Fyoutube%29%20%28SAMPLE%28%3Finception%29%20as%20%3Finception%29%20%28SAMPLE%28%3FdissolvedOrAbolished%29%20as%20%3FdissolvedOrAbolished%29%0AWHERE%20%7B%0A%09%7B%20%3Fwikidata%20p%3AP31%2Fps%3AP31%2Fwdt%3AP279%2a%20wd%3AQ3917681.%20%7D%20UNION%20%7B%20%3Fwikidata%20wdt%3AP31%20wd%3AQ7843791.%20%7D%20%23%20Embassy%20or%20consulate%0A%09%3Fwikidata%20p%3AP31%2Fps%3AP31%20%3FtypeId.%20%3FtypeId%20rdfs%3Alabel%20%3Ftype_label.%20filter%20%28lang%28%3Ftype_label%29%20%3D%20%22en%22%29.%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP131%2a%2Fwdt%3AP17%20%3FcountryId.%20%3FcountryId%20rdfs%3Alabel%20%3Fcountry_label.%20filter%20%28lang%28%3Fcountry_label%29%20%3D%20%22en%22%29.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP131%20%3FcityId.%20%3FcityId%20rdfs%3Alabel%20%3Fcity_label.%20filter%20%28lang%28%3Fcity_label%29%20%3D%20%22en%22%29.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP969%20%3Faddress.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP625%20%3Fcoordinates.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP137%20%3FoperatorId.%20%3FoperatorId%20rdfs%3Alabel%20%3Foperator_label.%20filter%20%28lang%28%3Foperator_label%29%20%3D%20%22en%22%29.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP1329%20%3Fphone.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP968%20%3Femail.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP856%20%3Fwebsite.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP2013%20%3Ffacebook.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP2002%20%3Ftwitter.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP2397%20%3Fyoutube.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP18%20%3Fimage.%7D%0A%20%20%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP571%20%3Finception.%7D%0A%09OPTIONAL%20%7B%3Fwikidata%20wdt%3AP576%20%3FdissolvedOrAbolished.%7D%0A%7D%20GROUP%20BY%20%3Fwikidata%20ORDER%20BY%20ASC%28%3Fcountry%29%20ASC%28%3Fcity%29%20ASC%28%3Foperator%29%20DESC%28%3Ftype%29) of some embassies

Many embassies and consulates are still missing from the database, please see the paragraph above to help fill the gaps, many thanks!
