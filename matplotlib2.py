import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv(r"C:\Users\user pc\Desktop\FIP\Week 1 Deliverable\company_sales_data.csv")

# Bathing soap
plt.subplot(2, 1, 1)
plt.plot(data["month_number"], data["bathingsoap"])
plt.title("Bathing Soap Sales")

# Facewash
plt.subplot(2, 1, 2)
plt.plot(data["month_number"], data["facewash"])
plt.title("Facewash Sales")

# Show the graphs
plt.tight_layout()
plt.show()

