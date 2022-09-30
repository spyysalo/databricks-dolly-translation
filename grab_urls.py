import sys
import json

id2url={}
for line in sys.stdin:
    d=json.loads(line)
    assert d["id"] not in id2url
    id2url[d["id"]]=d["url"]
json.dump(id2url,open("xlsum-doc-in/id2url.json","wt"))

    
