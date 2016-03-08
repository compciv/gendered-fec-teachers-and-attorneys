from urllib.request import urlopen
from os.path import join, basename
from os import makedirs
ORIGINAL_DATA_DIR = join('tempdata', 'original')
makedirs(ORIGINAL_DATA_DIR, exist_ok=True)
YEARS = ["2004", "2008", "2012", "2016"]


for year in YEARS:
    # typical URL: ftp://ftp.fec.gov/FEC/2016/indiv16.zip
    url = "ftp://ftp.fec.gov/FEC/%s/indiv%s.zip "% (year, year[2:4])
    print("Downloading from", url)
    with urlopen(url) as zfile:
        zdata = zfile.read()
        # e.g. tempdata/origina/indiv16.zip
        fname = join(ORIGINAL_DATA_DIR, basename(url))
        print("Writing to", fname)
        with open(fname, 'wb') as zf:
            zf.write(zdata)


# download the headers
# via: http://www.fec.gov/finance/disclosure/metadata/DataDictionaryContributionsbyIndividuals.shtml
DATA_HEADERS_URL = 'http://www.fec.gov/finance/disclosure/metadata/indiv_header_file.csv'
DATA_HEADERS_FILENAME = join(ORIGINAL_DATA_DIR, 'indiv_header_file.csv')
headertxt = urlopen(DATA_HEADERS_URL).read()
# need to decode from bytes to str
headertxt = headertxt.decode()
# save them to the data dir for now:
with open(DATA_HEADERS_FILENAME, 'w') as f:
    f.write(headertxt)
