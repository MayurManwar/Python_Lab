
# Visualize the daily temperature changes over time in a city and give your conclusion

import matplotlib.pyplot as plt

# Days of the month
days = list(range(1, 32))

# Daily temperature data
temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]

# Create the line plot
plt.figure(figsize=(12, 6))
plt.plot(days, temperature, marker='o', linestyle='-', color='b', alpha=0.7)

# Add titles and labels
plt.title('Daily Temperature Changes Over the Month')
plt.xlabel('Day of the Month')
plt.ylabel('Temperature (°F)')

# Show grid for better readability
plt.grid(True, linestyle='--', alpha=0.5)

# Display the plot
plt.show()
