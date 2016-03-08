from os import makedirs
from os.path import join
from shutil import unpack_archive
ORIGINAL_DATA_DIR = join('tempdata', 'original')
YEARS = ["2004", "2008", "2012", "2016"]

for year in YEARS:
    zname = join(ORIGINAL_DATA_DIR, 'indiv' + year[2:4] + '.zip')
    # we need to unzip each zip file into its own directory
    # because the FEC has named each file itcont.txt...
    # if we put them into the same directory, they will all get overwritten

    # make a new directory for each year
    # e.g. tempdata/original/1986
    yeardirname = join(ORIGINAL_DATA_DIR, year)
    makedirs(yeardirname, exist_ok=True)
    # unpack the zip file into this directory
    print("Unzipping", zname, "into", yeardirname)
    unpack_archive(zname, extract_dir=yeardirname)
