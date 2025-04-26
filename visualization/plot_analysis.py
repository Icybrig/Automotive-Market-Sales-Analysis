import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

car_data = pd.read_csv('data/cleaned/cleaned_car_data.csv')
consumer_data = pd.read_csv('data/cleaned/cleaned_consumer_data.csv')

plot_data = pd.merge(
    consumer_data, 
    car_data[['model', 'production_year', 'engine_type']], 
    left_on=['model', 'year'], 
    right_on=['model', 'production_year'],
    how='left'
)

sales_summary = plot_data.groupby(['year', 'engine_type'])['sales_volume'].sum().reset_index()
volume_summary = plot_data.groupby(['engine_type'])['sales_volume'].sum().reset_index()

# Plotting the diagram to compare Thermal and Electrical in Volume
plt.figure(figsize=(10,6))
sns.barplot(data=volume_summary, x='engine_type', y='sales_volume')
plt.title('Thermal vs Electric in Volume')
plt.xlabel('Engine Type')
plt.ylabel('Volume')
plt.grid(True)
plt.savefig('outputs/figures/Thermal vs Electric in Volume.png')
plt.close()

# Plotting the diagram to compare the total sales between Thermal and Electrical yearly
plt.figure(figsize=(10,6))
sns.lineplot(data=sales_summary, x='year', y='sales_volume', hue='engine_type', marker = 'o')
plt.title('Total Sales Thermal vs Electrical Yearly')
plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.grid(True)
plt.savefig('outputs/figures/Total Sales Thermal vs Electrical Yearly.png')
plt.close()

print(f'figures has been printed')