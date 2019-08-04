
### Steps to run Server

```
virtualenv crawler_env
source ./crawler_env/bin/activate
pip install -r requirements.txt
python3 server.py
```

#### Curl cli

```
curl http://127.0.0.1:5000/crawl -X POST -d "url=https://www.rust-lang.org/&depth=2"
```
