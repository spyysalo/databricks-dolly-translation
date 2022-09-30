import docx
import sys
import argparse
import json
import tqdm

def yield_translations(fnames):
    for fname in tqdm.tqdm(fnames):
        d=docx.Document(fname)

        curr_doc=None
        for p in d.paragraphs:
            if p.runs[0].bold and p.text.lower().startswith("asiakirja"):
                if curr_doc:
                    yield curr_doc
                curr_doc={"title":None,"text":None,"id":None,"url":""}
            elif p.runs[0].bold and p.text.lower().startswith("yhteenveto"):
                #we moved into summary
                curr_doc["summary"]=None
            else:
                if not curr_doc["title"]: #that one comes first
                    curr_doc["title"]=p.text
                elif "summary" in curr_doc:
                    #moved into summary already
                    curr_doc["summary"]=p.text
                else:
                    assert not curr_doc["text"] #if this fails it means a document with several paragraphs
                    curr_doc["text"]=p.text
        else:
            yield curr_doc
                    
                

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--url-data', help='Json with id2url mapping')
    parser.add_argument('--meta-data', help='Json with metadata created by jsonl2docx')
    parser.add_argument('DOCXS', nargs="+", help='All translated docx files in their correct order')

    args = parser.parse_args()

    id2url=json.load(open(args.url_data))
    meta=json.load(open(args.meta_data))
    
    all_d=list(yield_translations(args.DOCXS))
    assert len(all_d)==len(meta)

    train_f,val_f,test_f=open("jsonl-fi/finnish_train.jsonl","wt"),open("jsonl-fi/finnish_val.jsonl","wt"),open("jsonl-fi/finnish_test.jsonl","wt")
    
    for (orig_f,origid),d in zip(meta,all_d):
        d["id"]=origid
        d["url"]=id2url[origid]
        line=json.dumps(d,ensure_ascii=False,sort_keys=True)
        if "train" in orig_f:
            f=train_f
        elif "val" in orig_f:
            f=val_f
        elif "test" in orig_f:
            f=test_f
        else:
            assert False
        print(line,file=f)
        
