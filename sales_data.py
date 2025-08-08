import pandas as pd
import matplotlib.pyplot as plt

# Simulated detailed sales data
data = {
    'Product': ['Laptop', 'Phone', 'Tablet', 'Watch', 'Laptop', 'Phone', 'Tablet', 'Watch'],
    'Sales': [600, 400, 300, 200, 400, 400, 300, 200]
}

# Create DataFrame
df = pd.DataFrame(data)

# Show raw data
print("Raw Sales Data:")
print(df)

# Group by product and sum sales
grouped = df.groupby('Product')['Sales'].sum()
print("\nTotal Sales by Product:")
print(grouped)

# Plot using pandas built-in plot()
grouped.plot(kind='bar', title='Total Sales by Product', color='skyblue')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()

# Pie chart using grouped data
grouped.plot(kind='pie', autopct='%1.1f%%', title='Sales Distribution by Product')
plt.ylabel('')  # Hide y-label for pie chart
plt.tight_layout()
plt.show()