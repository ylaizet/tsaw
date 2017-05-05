TSAW
====

TSAW Torrent Server API Wrapper.

More information about the api at http://ion-torrent-sdk.readthedocs.io/en/latest/

---

Installation
------------

    pip install tsaw

---

Usage example
-------------

Get the 10 last results for plugin with id 42
    
```python
from tsaw import TorrentServerApi

#Adapt the following line with your server address and credentials
ts = TorrentServerApi("http://myserver/rundb/api/v1/", "ION_TS_USERNAME", "ION_TS_PASSWORD")
pluginresults = ts.pluginresult(params={"format": "json", "limit": 10, "order_by": "-id", "plugin": "42"})

#Do whatever you want with your pluginresults["objects"]
```
