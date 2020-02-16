import git
import pandas as pd
import glob
import os

git_url = 'git://github.com/CSSEGISandData/COVID-19.git'
repo_dir = os.getcwd()
git.Git(repo_dir).clone(git_url)

path = './COVID-19/csse_covid_19_data/csse_covid_19_daily_reports' 
all_csvs = glob.glob(path + "/*.csv")

li = []

for filename in all_csvs:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

merged_df = pd.concat(li, axis=0, ignore_index=True)
merged_df['Last Update']= pd.to_datetime(merged_df['Last Update']) 

outname = 'nCovid.csv'
outdir = './data'
if not os.path.exists(outdir):
    os.mkdir(outdir)

data_path = os.path.join(outdir, outname)

merged_df.to_csv(data_path, index = None, header = True)