import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\user pc\Desktop\FIP\Week 1 Deliverable\company_sales_data.csv")

plt.plot(data["month_number"], data["total_profit"])

plt.xlabel("Month Number")
plt.ylabel("Total Profit")
plt.title("Total Profit of All Months")

plt.show()
