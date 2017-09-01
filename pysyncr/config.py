import sys
import os.path
import ConfigParser
import textwrap
import logging
import appdirs

logger = logging.getLogger("pysyncr")

FILENAME = os.path.join(appdirs.user_config_dir(), 'pysyncr.conf')

def write_default():
    content = textwrap.dedent("""
    # Create your own API keys here, and fill the values:
    # https://www.flickr.com/services/apps/create/apply
    [pysyncr]
    api_key =
    api_secret =
    """)
    with open(FILENAME, 'w') as f:
        f.write(content)

def load():
    if not os.path.exists(FILENAME):
        write_default()
    #
    config = ConfigParser.ConfigParser()
    config.read(FILENAME)
    api_key = config.get('pysyncr', 'api_key')
    api_secret = config.get('pysyncr', 'api_secret')
    if not (api_key and api_secret):
        logger.error('Please configure API keys in %s' % FILENAME)
        sys.exit(1)
    return api_key, api_secret
