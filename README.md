# xlsum-fi

Finnish machine-translated version of the xlsum dataset.

`raw-data`: obtained from the xlsum HF dataset repository, not replicated in this github repo
`xlsum-doc-in`: obtained by running json2doc on the files in `raw-data`, not replicated in this github repo
`xlsum-doc-out`: output of the MT system on `xlsum-doc-in`

Files called `xlsum-0-to-10...` have their full-text to summary ratio in the interval [0,10], i.e. the full text is max 10x the length of the summary

# HuggingFace dataset

You can grab the .jsonl data from the corresponding HuggingFace dataset here: https://huggingface.co/datasets/TurkuNLP/xlsum-fi/tree/main/data

# License and Disclaimer

**This data must not be used for any machine-translation related work** so as to comply with the Terms and Conditions of the DeepL machine translation system. The data is released under the **non-commercial** CC-BY-NC-SA-4.0 license.

