from os.path import join
import json
WRANGLED_DATA_FILENAME = join('tempdata', 'babynames', 'wrangledbabynames.json')
# boy this is bad practice...but it's fast...
NAMES_DATA_ROWS = json.load(open(WRANGLED_DATA_FILENAME))

def detect_gender(name):
    # prepare an empty result just in case the given name is not found in our database
    result = { 'name': name, 'gender': 'NA', 'ratio': None, 'males': None, 'females': None, 'total': 0 }
    for row in NAMES_DATA_ROWS:
        # find first row...
        if name.lower() == row['name'].lower():
            # this should be the match
            result = row
            # since each name only shows up once in our list
            # we can break early rather than iterating through the rest of NAMES_DATA_ROWS
            break
    # if no match was found, result is what it was at the beginning
    return result


def get_usable_name(namestr):
    # split into two pieces, at most
    nameparts = namestr.split(', ', 1)
    for nx in nameparts[-1].split(' '):
        if '.' not in nx:
            return nx  # returns the first thing that has no period
    # if we get to this point...then...just return nothing
    return ""




from os import makedirs
from os.path import join
from shutil import unpack_archive
from csv import DictReader, DictWriter
ORIGINAL_DATA_DIR = join('tempdata', 'original')
WRANGLED_DATA_DIR = join('tempdata', 'wrangled')
CLASSIFIED_DATA_DIR = join('tempdata', 'classified')
makedirs(CLASSIFIED_DATA_DIR, exist_ok=True)
DATA_HEADERS_FILENAME = join(ORIGINAL_DATA_DIR, 'indiv_header_file.csv')
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
        usable_name = get_usable_name(row['NAME'])
        xresult = detect_gender(usable_name)
        row['gender'] = xresult['gender']
        row['ratio'] = xresult['ratio']
        row['total'] = xresult['total']
        outcsv.writerow(row)
        rowcount += 1
        print("Row:", rowcount, "Name:", usable_name, row['gender'], row['ratio'])
