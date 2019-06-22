# --------------
import pandas as pd 

# Read the data using pandas module.
df = pd.read_csv(path)
# Find the list of unique cities where matches were played
cities = pd.unique(df.city)
print('List of unique cities where matches were played',cities)
# Find the columns which contains null values if any ?
df.columns[df.isna().any()].tolist()
# List down top 5 most played venues
df1 = df[['match_code','venue']].drop_duplicates()
df1 = df1.venue.value_counts().sort_values(ascending=False).head(5)
print('Top 5 most played venues are :',df1.index.tolist())
# Make a runs count frequency table
df.runs.value_counts().sort_index(ascending=True)
# How many seasons were played and in which year they were played 
df['year']= df.date.str.slice(start=0,stop=4)
print('Number of seasons played :',df['year'].drop_duplicates().size)
print('IPL seasons were played in :',df['year'].drop_duplicates().tolist())
# No. of matches played per season

df1 = df[['match_code','year']].drop_duplicates()
df1 = df1.year.value_counts().sort_index(ascending=True)
print('No. of matches played per season: \n')
for items in df1.iteritems(): 
    print(items) 

# Total runs across the seasons
print('Total runs across the seasons:',df.groupby('year')[['runs']].sum().sort_values(by='year',ascending=True))

# Teams who have scored more than 200+ runs. Show the top 10 results
df1 = df.groupby(['match_code','batting_team'],as_index= False)[['runs']].sum().sort_values(by='runs',ascending=False)
print('Top 10 teams who have scored more than 200 runs:',df1[['batting_team','runs']].head(10).values)
# What are the chances of chasing 200+ target
df1 = df.groupby(['match_code','inning','win_type'],as_index= False)[['runs']].sum().sort_values(by='runs',ascending=False)
x = df1[(df1['runs'] >= 200) & (df1['inning'] == 1)].match_code.count()
print('Total number of matches a team scored 200 above in 1st inning: ',x)

y = df1[(df1['runs'] >= 200) & (df1['inning'] == 2) & (df1['win_type'] == 'wickets')].match_code.count()

print('Total number of matches a team chased 200 above in 2nd inning: ',y)
print('Chances of chasing 200+ target :',y/x)
# Which team has the highest win count in their respective seasons ?

df1 = df[['year','match_code','winner']].drop_duplicates()
df1.groupby(['year','winner'],as_index= False)['match_code'].count()
print('Teams with highest win count per season',df1.groupby('year').apply(lambda x: x.winner[x.match_code.idxmax()]))




