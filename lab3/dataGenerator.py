import pandas as pd
import numpy as np

# Згенерувати уявні дані
dates = pd.date_range(start='2023-01-01', end='2023-12-31', freq='B')
stocks = ['AAPL', 'GOOGL', 'MSFT']
prices = np.random.randint(low=50, high=200, size=len(dates))

# Створити DataFrame
data = pd.DataFrame({'Date': dates, 'Stock': np.random.choice(stocks, len(dates)), 'Price': prices})

# Зберегти у CSV
data.to_csv('stocks.csv', index=False)