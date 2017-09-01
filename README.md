# pysyncr

Upload, download or sync photos and videos to flickr.

## Install

Download pysyncr

```sh
> git clone https://github.com/antocuni/pysyncr
```

Create your own personal Flickr API keys:
```sh
> https://www.flickr.com/services/apps/create/apply
```

Add api_key and api_secret to pysyncr/pysyncr/config.py:
```sh
  api_key = u'<API_KEY>'
  api_secret = u'<API_SECRET>'
```

Run the install script:
```sh
> python setup.py install
```

## Example Usage

Upload all photos and vidoes in current folder and all sub-folders:
```sh
> pysyncr
```

## Acknowledgments

pysyncr is based on
[flickrsmartsync_oauth](https://github.com/inspector2211/flickrsmartsync_oauth),
which is itself derived from
[flickrsmartsync](https://github.com/faisalraja/flickrsmartsync) written by
Faisal Raja.  


## License

MIT
