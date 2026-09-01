---
title: "Batch file downloads"
source: https://gtidocs.virustotal.com/docs/batch-file-downloads
slug: batch-file-downloads
section: guides
group: "IOC Investigation"
updatedAt: 2025-09-25T02:38:43.000Z
retrieved: 2026-09-01
---

[gtidocs](../../../README.md) › [Guides](../../README.md) › [IOC Investigation](../README.md) › [Intelligence / Web searching](../intelligence.md) › Batch file downloads

---

# batch-file-downloads

Google Threat Intelligence's web interface allows you to download packages of files matching the first 25, 50 or 100 results of a given query. If you wish to download any other custom number, including more than 100 files, you should use one of the examples of [vt-py](https://github.com/VirusTotal/vt-py) the official Python client library for Google Threat Intelligence.

**This library requires Python 3.6.0+, Python 2.x is not supported. This is because vt-py makes use of the new[async/await](https://snarky.ca/how-the-heck-does-async-await-work-in-python-3-5/) syntax for implementing asynchronous coroutines.**

The easiest and recommended way of installing vt-py is using pip:

```
$ pip install vt-py
```

Alternatively, you can get the source code directly from the GitHub and run setup.py. For getting the code you can either clone the public repository:

```
$ git clone git://github.com/VirusTotal/vt-py.git  
$ cd vt-py
```

Or, download the tarball for the latest release and uncompress it:

```
$ tar -zxvf vt-py-X.Y.Z.tar.gz  
$ cd vt-py-X.Y.Z
```

Once you have the code you can install it with:

```
$ sudo python3 setup.py install
```

After installing the library, you can use the [search\_and\_download\_topn\_files.py](https://github.com/VirusTotal/vt-py/blob/master/examples/search_and_download_topn_files.py) script:

```
user@machine:~/$ python3 search\_and\_download\_topn\_files.py --help  
usage: usage: prog [options] <intelligence\_query/local\_file\_with\_hashes>  
  
Allows you to download the top-n files returned by a given Google Threat Intelligence  
Intelligence search. Example: python %prog type:"peexe" positives:5+ -n 10  
--apikey=<your api key>

positional arguments:  
  query a Google Threat Intelligence Intelligence search query.
  
optional arguments:  
  -h, --help show this help message and exit  
  -n NUMFILES, --numfiles NUMFILES  
                        Number of files to download  
  --apikey APIKEY Your Google Threat Intelligence API key  
  -o OUTPUT_PATH, --output-path OUTPUT_PATH  
                        The path where you want to put the files in  
  -w WORKERS, --workers WORKERS  
                        Concurrent workers for downloading files

```

Hence, if you wish to download the top 500 files matching the query *type:"peexe"* you would just have to type:

```
python3 search\_and\_download\_topn\_files.py -n 500 'type:"peexe"' --apikey $VT\_API\_KEY
```

---

← [Content search (Grep)](content-search-grep.md) · [up](../README.md) · [Full list of Google Threat Intelligence tag modifier](full-list-of-google-threat-intelligence-tag-modifier.md) →

*Archived from <https://gtidocs.virustotal.com/docs/batch-file-downloads>.*
