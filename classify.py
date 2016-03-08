
from os import makedirs
from os.path import join
from shutil import unpack_archive
from csv import DictReader, DictWriter
from gender import detect_gender

ORIGINAL_DATA_DIR = join('tempdata', 'original')
WRANGLED_DATA_DIR = join('tempdata', 'wrangled')
CLASSIFIED_DATA_DIR = join('tempdata', 'classified')
makedirs(CLASSIFIED_DATA_DIR, exist_ok=True)
DATA_HEADERS_FILENAME = join(ORIGINAL_DATA_DIR, 'indiv_header_file.csv')


def extract_usable_name(namestr):
    # split into two pieces, at most
    nameparts = namestr.split(', ', 1)
    for nx in nameparts[-1].split(' '):
        if '.' not in nx:
            return nx  # returns the first thing that has no period
    # if we get to this point...then...just return nothing
    return ""





original_headers = open(DATA_HEADERS_FILENAME).read().strip().split(',')
# the classified headers are just the original headers, with 'gender', 'ratio', and 'total'
classified_headers = original_headers + ['gender', 'ratio', 'total']

YEARS = ["2004", "2008", "2012", "2016"]

for year in YEARS:
    wrangled_fname = join(WRANGLED_DATA_DIR, year + '.csv')
    print("Classifying", wrangled_fname)
    classified_fname = join(CLASSIFIED_DATA_DIR, year + '.csv')
    print("Writing to", classified_fname)

    infile = open(wrangled_fname, 'r')
    incsv = DictReader(infile)
    outfile = open(classified_fname, 'w')
    outcsv = DictWriter(outfile, fieldnames=classified_headers)
    outcsv.writeheader()

    rowcount = 0
    for row in DictReader(infile):
        usable_name = extract_usable_name(row['NAME'])
        xresult = detect_gender(usable_name)
        row['gender'] = xresult['gender']
        row['ratio'] = xresult['ratio']
        row['total'] = xresult['total']
        outcsv.writerow(row)
        rowcount += 1
        print("Row:", rowcount, "Name:", usable_name, row['gender'], row['ratio'])
