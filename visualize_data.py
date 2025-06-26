import pandas as pd
import matplotlib.pyplot as plt

# Specify the full path to CSV file
file_path = r"C:\Users\Asus.ASUS\OneDrive\Documents\.vscode\BIT_4th_sem_proffesional\pandas\weather_classification_data.csv"

# Read the CSV file into a DataFrame
weather_df = pd.read_csv(file_path)

# Display some basic statistics about the DataFrame
print("Basic Statistics of the DataFrame:")
print(weather_df.describe())

# Print the column names to verify
print("\nColumn Names:")
print(weather_df.columns)

# Plotting Temperature by Season
plt.figure(figsize=(10, 6))
plt.plot(weather_df['Season'], weather_df['Temperature'], marker='o', linestyle='-', label='Temperature')
plt.xlabel('Season')
plt.ylabel('Temperature')
plt.title('Temperature by Season')
plt.legend()
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('temperature_by_season.png')  # Save the plot as a file
plt.show()

# Plotting Temperature vs. Humidity
plt.figure(figsize=(10, 6))
plt.scatter(weather_df['Humidity'], weather_df['Temperature'], label='Temperature vs Humidity', color='r')
plt.xlabel('Humidity')
plt.ylabel('Temperature')
plt.title('Temperature vs. Humidity')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('temperature_vs_humidity.png')  # Save the plot as a file
plt.show()

# Plotting Temperature vs. Wind Speed
plt.figure(figsize=(10, 6))
plt.scatter(weather_df['Wind Speed'], weather_df['Temperature'], label='Temperature vs Wind Speed', color='g')
plt.xlabel('Wind Speed')
plt.ylabel('Temperature')
plt.title('Temperature vs. Wind Speed')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('temperature_vs_wind_speed.png')  # Save the plot as a file
plt.show()

# Plotting Temperature vs. UV Index
plt.figure(figsize=(10, 6))
plt.scatter(weather_df['UV Index'], weather_df['Temperature'], label='Temperature vs UV Index', color='b')
plt.xlabel('UV Index')
plt.ylabel('Temperature')
plt.title('Temperature vs. UV Index')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('temperature_vs_uv_index.png')  # Save the plot as a file
plt.show()

# Print the sum of missing values in each column
print("\nSum of Missing Values in Each Column:")
print(weather_df.isnull().sum())
