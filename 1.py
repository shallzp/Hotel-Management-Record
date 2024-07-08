import pandas as pd
import numpy as np
import sqlalchemy
df = pd.DataFrame()
csv_file = r"C:\Users\lenovo\Desktop\IP\Shalini_Patel_IP_Project\HOTEL_BOOKING.csv"
df = pd.read_csv(csv_file)
engine = sqlalchemy.create_engine('mysql+pymysql://root:admin@localhost/IP_PROJECT_XII')
df.to_sql(name='hotel_booking',con=engine,index=True,if_exists='replace')
print('\n\nPlease check IP_PROJECT_XII database for hotel_booking table.....')
