from pandas import DataFrame
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

row_numbers = range(0,60)
ages = [row + 15 for row in row_numbers]
age_data = list(zip(row_numbers, ages))

df = pd.DataFrame(data = age_data, columns=['Row', 'Age'])
df.set_index('Row')

# Important:
rate_of_return = .04
yearly_savings = 1000


prev_total = 0
for row in row_numbers:

    year_start_money = prev_total
    investment_returns = round( (year_start_money+yearly_savings) * rate_of_return,0)
    year_ending_money = year_start_money + yearly_savings + investment_returns

    df.loc[row,'YearStartingMoney'] = year_start_money
    df.loc[row,'YearlySaving'] = yearly_savings
    df.loc[row,'InvestmentReturn'] = investment_returns
    df.loc[row,'YearEndingMoney'] = year_ending_money

    prev_total = year_ending_money

print(df)

