from os.path import join
from csv import DictReader
CLASSIFIED_DATA_DIR = join('tempdata', 'classified')
YEARS = ["2004", "2008", "2012", "2016"]
for year in YEARS:
    classified_fname = join(CLASSIFIED_DATA_DIR, year + '.csv')
    with open(classified_fname) as f:
        datarows = list(DictReader(f))
        genderedrows = [r for r in datarows if r['gender'] != 'NA']
        print("Total rows", len(datarows), "Gendered rows", len(genderedrows))


        print(year)
        teacherrows = [r for r in genderedrows if 'TEACHER' in r['OCCUPATION']]
        print("Teacher rows", len(teacherrows))
#        femaleteacherrows = [r for r in teacherrows if r['gender'] == 'F']
        print("TODO: get gender")

        # print( round(100 * (len(femaleteacherrows) / len(teacherrows))), "female teachers")


        lawyerrows = [r for r in genderedrows if 'LAWYER' in r['OCCUPATION'] or 'ATTORNEY' in r['OCCUPATION']]
        print("TODO: get gender")
        print("Lawyer rows", len(lawyerrows))
        # femalelawyerrows = [r for r in lawyerrows if r['gender'] == 'F']
        # print( round(100 * (len(femalelawyerrows) / len(lawyerrows))), "female attorneys")
