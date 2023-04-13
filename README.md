# Finnish Dolly dataset

Finnish version of the `databricks-dolly-15k` instruction dataset
(<https://github.com/databrickslabs/dolly/tree/master/data>), machine
translated using DeepL (<https://www.deepl.com/>).

## Process

Convert original data from JSONL to DOCX files

```
python3 jsonl2doc.py original-data/databricks-dolly-15k.jsonl
```

Translate DOCX files from `dolly-doc-in/` using DeepL
(<https://www.deepl.com/>) and save outputs in `dolly-doc-out/`.

Convert back to JSONL

```
python3 doc2jsonl.py \
    original-data/databricks-dolly-15k.jsonl \
    dolly-doc-out/dolly-000*.docx \
    > dolly-15k-fi.jsonl
```

## License

This dataset is licensed under the [Creative Commons Attribution-ShareAlike 3.0 Unported License](https://creativecommons.org/licenses/by-sa/3.0/legalcode) (CC BY-SA).

Note that under the [DeepL terms and conditions](https://www.deepl.com/en/pro-license), this data may not be used to develop, market or train a machine
translation algorithm.
