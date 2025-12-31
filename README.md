# Salary Data Analysis – Glassdoor 2024

This project uses the Glassdoor Data Science Job Listings 2024 dataset from Kaggle.  
It focuses on cleaning salary data, examining job title trends, and identifying industries with higher average pay.

The dataset contains around 1,500 job postings with information like job title, salary estimate, industry, and location.  
The dataset file is stored in the `data` folder: `data/glassdoor_jobs.csv`.

Tools used:
- Python
- pandas
- matplotlib
- Google Colab (development environment)

Work done in the project:
- Removed missing and hourly salary entries
- Extracted minimum, maximum, and average salary values
- Standardized job titles for consistency
- Analyzed job title frequency
- Grouped industries to find top-paying sectors
- Created charts for visualization

Key findings:
- Average salary: ~124K
- Most common role: Data Scientist
- Top-paying industries: Convenience Stores, Wholesale, Internet & Web Services, Video Game Publishing, Software Development

Project files:
- `data/glassdoor_jobs.csv` – original dataset
- `src/salary_analysis.py` – script for cleaning and analysis
- `outputs/salary_distribution.png` – salary distribution chart
- `outputs/top_job_titles.png` – job title frequency chart
- `outputs/top_industries_salary.png` – industry salary comparison

To run the project:
```bash
python3 src/salary_analysis.py
