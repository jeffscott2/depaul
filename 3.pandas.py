from pandas import DataFrame
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# Important:
age_you_start_saving_at = 15
life_expectancy = 80
rate_of_return = .04
yearly_savings = 1000


ages = list(range(1, life_expectancy + 1))
df = pd.DataFrame(data = ages, columns=['Age'])


prev_total = 0
for i in range(0, len(ages)):

    age = df.loc[i,'Age']

    if age < age_you_start_saving_at:
        actual_yearly_savings = 0
    else:
        actual_yearly_savings = yearly_savings

    year_start_money = prev_total
    investment_returns = round( year_start_money * rate_of_return,0)
    year_ending_money = year_start_money + actual_yearly_savings + investment_returns

    df.loc[i,'YearStartingMoney'] = year_start_money
    df.loc[i,'InvestmentReturn'] = investment_returns
    df.loc[i,'YearlySaving'] = actual_yearly_savings
    df.loc[i,'YearEndingMoney'] = year_ending_money

    prev_total = year_ending_money

print(df)

