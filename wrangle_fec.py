from os import makedirs
from os.path import join
from csv import DictReader, DictWriter
ORIGINAL_DATA_DIR = join('tempdata', 'original')
DATA_HEADERS_FILENAME = join(ORIGINAL_DATA_DIR, 'indiv_header_file.csv')
WRANGLED_DATA_DIR = join('tempdata', 'wrangled')
YEARS = ["2004", "2008", "2012", "2016"]

# remember that each raw file has no headers, so we
# need to get them manually from DATA_HEADERS_FILENAME
headers = open(DATA_HEADERS_FILENAME).read().strip().split(',')



for year in YEARS:
    # i.e. tempdata/original/1986/itcont.txt
    orgname = join(ORIGINAL_DATA_DIR, year, 'itcont.txt')


    # make the new dir and filename
    wrangled_dir = join(WRANGLED_DATA_DIR)
    wrangled_fname = join(WRANGLED_DATA_DIR, year + '.csv')
    makedirs(wrangled_dir, exist_ok=True)

    with open(orgname, 'r', encoding='windows-1252') as r:
        print("Opening", orgname)
        # remember that the original data files come as pipe-delimited
        csvinput = DictReader(r, fieldnames=headers, delimiter='|')

        w = open(wrangled_fname, 'w')
        print("Writing to", wrangled_fname)
        csvoutput = DictWriter(w, fieldnames=headers)
        csvoutput.writeheader()
        # remember that each raw file has no headers, so
        # we need to call DictReader and set its fieldnames argument

        for row in csvinput:
            if ('TEACHER' in row['OCCUPATION']
                or 'ATTORNEY' in row['OCCUPATION']
                or 'LAWYER' in row['OCCUPATION']):
                csvoutput.writerow(row)
        w.close()


