# Sync Wars
> A simple two-way application to synchronise directories across systems. It uses [Dropbox API](https://www.dropbox.com/developers) to upload the data from one directory and download it to all the other systems.

## Setup
```shell
git clone https://github.com/prabhakar267/sync-wars.git && cd sync-wars
```

```shell
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

```shell
[sudo] pip install -r requirements.txt
```

+ Edit [config.py.sample](config.py.sample) and add Dropbox API keys ([dropbox.com/developers](https://www.dropbox.com/developers)) and change the **directories** accordingly.
+ Save the updated file as **config.py**

```shell
python upload.py &
```


```shell
python download.py
```
