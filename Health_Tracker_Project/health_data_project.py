import os
import shutil


PATH = '/Users/cianikaingram/Documents/BizProcess/data/raw/'
UPDATED = '/Users/cianikaingram/Documents/BizProcess/data/updated/'
LANDING = '/Users/cianikaingram/Documents/BizProcess/data/landing/'
PROCESSED = '/Users/cianikaingram/Documents/BizProcess/data/processed/'



# add type and date to filename
def rename_files(category):
    for root, dirs, files in os.walk(PATH+category):
        prefix = os.path.basename(root)
        for f in files:
            os.rename(os.path.join(root, f), os.path.join(root, "{}_{}_{}".format(prefix, category, f)))
  

def move_to_landing(date):
        bmi_file = f'{UPDATED}/{date}_{bmi}_daily.json'
        heartrate_file = f'{UPDATED}/{date}_{heartrate}_hourly.json'
        vo2_file = f'{UPDATED}/{date}_{vo2}_daily.json'
        files = [bmi_file, heartrate_file, vo2_file]
        for file in files:
             shutil.move(file, LANDING)


if __name__ == '__main__':
    # move_to_landing(date)
    app()
