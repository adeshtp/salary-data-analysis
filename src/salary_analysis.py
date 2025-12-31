import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/glassdoor_jobs.csv")
df.head()

df.info()

df.columns = df.columns.str.lower().str.replace(" ", "_")
df.head()

df['salary_estimate'] = df['salary_estimate'].str.replace('$','').str.replace('K','').str.replace('(Glassdoor est.)','', regex=False)
df['salary_estimate'].head()

df = df[df['salary_estimate'] != '-1']

df['salary_estimate'] = (
    df['salary_estimate']
    .str.replace('Employer Provided Salary:', '', regex=False)
    .str.replace('$', '', regex=False)
    .str.replace('K', '', regex=False)
    .str.replace('()', '', regex=False)
)

df['salary_estimate'].head()

df[df['salary_estimate'].str.contains('Per Hour', na=False)].head()

df = df[~df['salary_estimate'].str.contains('Per Hour', na=False)]

df['salary_estimate'] = df['salary_estimate'].str.strip()

salary_split = df['salary_estimate'].str.split('-', expand=True)

df['min_salary'] = salary_split[0].astype(float)
df['max_salary'] = salary_split[1].astype(float)

df[['salary_estimate', 'min_salary', 'max_salary']].head()

df['avg_salary'] = (df['min_salary'] + df['max_salary']) / 2
df['avg_salary'].head()

overall_avg_salary = df['avg_salary'].mean()
overall_avg_salary

df['job_title_clean'] = df['job_title'].str.lower().str.strip()

df['job_title_clean'] = df['job_title_clean'].replace({
    'sr. data scientist': 'senior data scientist',
    'sr data scientist': 'senior data scientist',
    'data scientist i': 'data scientist',
    'data scientist ii': 'data scientist',
    'data scientist iii': 'data scientist',
    'lead data scientist': 'senior data scientist',
    'principal data scientist': 'senior data scientist',
    'college graduate - data science (bs/ms)': 'entry level data scientist',
    'data science intern': 'entry level data scientist',
    'data science associate': 'entry level data scientist'
})

df['job_title'].value_counts().head(5)

df.groupby('industry')['avg_salary'].mean().sort_values(ascending=False).head(5)

top_jobs = df['job_title_clean'].value_counts().head(5)

plt.figure(figsize=(10, 6))
plt.hist(df['avg_salary'], bins=20, color='skyblue', edgecolor='black')
plt.axvline(overall_avg_salary, color='red', linestyle='--', linewidth=2, label=f'Overall Avg: ${overall_avg_salary:.0f}K')
plt.title(f'Average Salary Distribution (Overall Avg: ${overall_avg_salary:.0f}K)')
plt.xlabel('Average Salary (in thousands)')
plt.ylabel('Number of Jobs')
plt.legend()
plt.tight_layout()
plt.savefig('outputs/salary_distribution.png', dpi=200)
plt.show()

plt.figure(figsize=(10, 6))
top_jobs.plot(kind='bar')
plt.title('Top 5 Job Titles')
plt.xlabel('Job Title')
plt.ylabel('Number of Listings')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('outputs/top_job_titles.png', dpi=200)
plt.show()

top_industries = (
    df.groupby('industry')['avg_salary']
    .mean()
    .sort_values(ascending=False)
    .head(5)
)

plt.figure(figsize=(10, 6))
top_industries.plot(kind='bar')
plt.title('Top 5 Highest Paying Industries')
plt.xlabel('Industry')
plt.ylabel('Average Salary (in thousands)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('outputs/top_industries_salary.png', dpi=200)
plt.show()