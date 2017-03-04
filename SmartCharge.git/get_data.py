import urllib.parse
import urllib.request
import zlib
from io import StringIO

url = 'http://www.ree.es/sites/default/files/simel/demd/DEMD_20170303.gz'

request = urllib.request.Request(url)
result = urllib.request.urlopen(request)
decompressed_data=zlib.decompress(result.read(), 16+zlib.MAX_WBITS)
print(decompressed_data)
