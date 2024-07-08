# Hotel Booking Database System

import pandas as pd  
import numpy as np
#import sqlalchemy
import matplotlib.pyplot as plt  #Data Visualization

df = pd.DataFrame()
csv_file = #path of csv file

def read_csv_file():
    df = pd.read_csv(csv_file)
    print(df)
        
def clear():
    for x in range(5):
        print()

def data_analysis_menu():
    df = pd.read_csv(csv_file)
    while True:
        clear()
        print('\n\nData Analysis MENU')
        print('_'*100)
        print('1.  Show Whole DataFrame\n')
        print('2.  Show Columns\n')
        print('3.  Show Top Rows\n')
        print('4.  Show Bottom Rows\n')
        print('5.  Show specific Column\n')
        print('6.  Add a New Customer Record\n')
        print('7.  Add a New Column\n')
        print('8.  Delete a Column\n')
        print('9.  Delete a Customer Record\n')
        print('10. Data Summary\n')
        print('11. Exit(Back to MAIN MENU)\n')
        ch = int(input('Enter your choice:'))

        if ch==1:
            print(df)
            print('\n\n Press any key to continue....')
            wait = input()

        elif ch==2:       
            print(df.columns)
            print('\n\n Press any key to continue....')
            wait = input()

        elif ch==3:       
            n = int(input('Enter total top rows you want to show :'))
            print(df.head(n))
            print('\n\n Press any key to continue....')
            wait = input()

        elif ch==4:       
            n = int(input('Enter total bottom rows you want to show :'))
            print(df.tail(n))
            print('\n\n Press any key to continue....')
            wait = input()

        elif ch==5:
            print(df.columns)
            col_name = input('Enter Column Name that you want to print :')
            print(df[col_name])
            print('\n\n Press any key to continue....')
            wait = input()

        elif ch==6:
            a = input('C_ID :')
            b = input('NAME :')
            c = input('PHONE_NO :')
            d = input('ADDRESS :')
            e = input('AGE :')
            f = input('COUNTRY :')
            g = input('MONTH :')
            h = input('YEAR :')
            i = input('NO_OF_PERSON :')
            j = int(input('NO_OF_DAYS :'))
            k = input('HOTEL_PREFERENCE :')
            print()
            print('-x'*50)
            print('WE HAVE THE FOLLOWING ROOMS FOR YOU :')
            print('1.  Budget Room Rs 1000')
            print('2.  Elite Room Rs 3000')
            print('3.  Royal Room Rs 4000')
            print('4.  Ultra Royal Room Rs 6000')
            print('-x'*50)
            l = input('\nROOM_PREFERENCE :')
            x = int(input('ROOM_PRICE :'))
            y = print('ROOM_RENT :',(x*j))
            m = x*j
            print()
            print('-x'*50)
            print('WE HAVE THE FOLLOWING FOOD PREFERENCE FOR YOU :')
            print('1.  Italian Rs 3000')
            print('2.  Chinese Rs 2500')
            print('3.  Japanese Rs 2500')
            print('4.  Indian Rs 2500')
            print('5.  Mexican Rs 3000')
            print('-x'*50)
            n = input('\nFOOD_PREFERENCE :')
            o = int(input('FOOD_BILL :'))
            p = input('CANCELLED/NOT_CANCELLED :')
            q = input('MODE_OF_PAYMENT :')
            r = input('NO_OF_BOOKING :')
            s = m+o
            t = print('TOTAL_BILL :',m+o)
            df.loc[len(df)]=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s]   #72    0-71
            print(df)
            print('\n\n Press any key to continue....')
            wait = input()

        elif ch==7:
            col_name = input('Enter new column name :')
            col_value = input('Enter default column value :')
            df[col_name] = col_value
            print(df)
            print('\n\n Press any key to continue....')
            wait = input()

        elif ch==8:
            print(df.columns)
            col_name = input('Enter column name to delete :')
            del df[col_name]
            print(df)
            print('\n\n Press any key to continue....')
            wait = input()

        elif ch==9:
            print('Choose row index from 0 to ',len(df)-1)
            index_no = int(input('Enter the index number that you want to delete :'))
            df = df.drop(df.index[index_no])
            print(df)
            print('\n\n Press any key to continue....')
            wait = input()

        elif ch==10:
            print(df.info())
            print('\n\n Press any key to continue....') 
            wait = input()
            
        elif ch==11:
            break

def graph():
    df = pd.read_csv(csv_file)
    while True:
        clear()
        print('\n\nGRAPH MENU ')
        print('_'*100)
        print()
        print('1.  Line Graph displaying Monthly Hotel Booking Trend\n')
        print('2.  Line Graph dislaying Food Preferences\n')
        print('3.  Bar Graph displaying Yearwise Comparision\n')
        print('4.  Bar Graph displaying Countrywise Booking Comparision\n')
        print('5.  Bar Graph displaying Comparision between City Hotel and Resort Hotel\n')
        print('6.  Bar Graph displaying Payment Method\n')
        print('7.  Bar Graph displaying Comparision of Cancellation Status\n')
        print('8.  Histogram displaying Billing Trend\n')
        print('9. Exit(Back to MAIN MENU)\n')
        ch = int(input('Enter your Choice : '))

        if ch==1:
            g = df.groupby('MONTH')
            x = df['MONTH'].unique()
            x.sort()
            y = g['C_ID'].count()
            plt.xlabel('Months')
            plt.ylabel('No. of Booking')
            plt.title('Monthly Hotel Booking Trend')
            plt.grid(True)
            plt.plot(x,y,'r',linestyle='-.',marker='o',markeredgecolor='g')
            plt.show()
            print('\n\n Press any key to continue....')

        elif ch==2:
            g = df.groupby('FOOD_PREFERENCE')
            x = df['FOOD_PREFERENCE'].unique()
            x.sort()
            y = g['C_ID'].count()
            plt.xlabel('Menu')
            plt.ylabel('No. of customer')
            plt.title('Food Preferences')
            plt.grid(True)
            plt.plot(x,y,'y',linestyle='--',marker='2',markersize=10,markeredgecolor='black')
            plt.show()
            print('\n\n Press any key to continue....')
            
        elif ch==3:
            g = df.groupby('YEAR')
            x = df['YEAR'].unique()
            x.sort()
            y = g['C_ID'].count()
            plt.xlabel('Years')
            plt.ylabel('No. of Booking')
            plt.title('Yearwise Comparision')
            plt.bar(x,y,color='grey')
            plt.show()
            print('\n\n Press any key to continue....')
            
        elif ch==4:
            g = df.groupby('COUNTRY')
            x = df['COUNTRY'].unique()
            x.sort()
            y = g['C_ID'].count()
            plt.xlabel('Countries')
            plt.ylabel('No. of Customer')
            plt.title('Countrywise Booking Comparision')
            plt.bar(x,y,color='m')
            plt.show()
            print('\n\n Press any key to continue....')
            
        elif ch==5:
            g = df.groupby('HOTEL_PREFERENCE')
            x = df['HOTEL_PREFERENCE'].unique()
            x.sort()
            y = g['C_ID'].count()
            plt.xlabel('City Hotel or Resort Hotel')
            plt.ylabel('No. of Customer')
            plt.title('Comparision between City Hotel and Resort Hotel')
            plt.bar(x,y,color='pink')
            plt.show()
            print('\n\n Press any key to continue....')
            
        elif ch==6:
            g = df.groupby('MODE_OF_PAYMENT')
            x = df['MODE_OF_PAYMENT'].unique()
            y = g['C_ID'].count()
            plt.xlabel('Cash/Cheque/DD')
            plt.ylabel('No. of Customer')
            plt.title('Payment Method')
            plt.bar(x,y,color='olive')
            plt.show()
            print('\n\n Press any key to continue....')

        elif ch==7:
            g = df.groupby('IS_CANCELLED')
            x = df['IS_CANCELLED'].unique()
            x.sort()
            y = g['C_ID'].count()
            plt.xlabel('Booking Cancelled')
            plt.ylabel('No. of Customer')
            plt.title('Comparision of Cancellation Status')
            plt.bar(x,y,color='b')
            plt.show()
            print('\n\n Press any key to continue....')

        elif ch==8:
            x=df['TOTAL_BILL']
            plt.hist(x,bins=5,edgecolor='k',color='silver',linestyle='--',hatch='\\')
            plt.title("Billing Trend")
            plt.show()
            print('\n\n Press any key to continue....')

        elif ch==9:
            break

def export_menu():
    df = pd.read_csv(csv_file)
    while True:
        clear()
        print('\n\nEXPORT MENU ')
        print('_'*100)
        print()
        print('1.  CSV File\n')
        print('2.  MySQL Table\n')
        print('3.  Exit (Back to MAIN MENU)')
        ch = int(input('Enter your Choice : '))

        if ch==1:
            df.to_csv(r'C:\Users\lenovo\Desktop\IP\Shalini_Patel_IP_Project\newHOTEL_BOOKING.csv')
            print('\n\nCheck your new file "NEW_HOTEL_BOOKING.csv" on C: Drive.....')
            wait = input()
            
        elif ch==2:
            engine = sqlalchemy.create_engine('mysql+pymysql://root:admin@localhost/IP_PROJECT_XII')
            df.to_sql(name='hotel_booking',con=engine,index=False,if_exists='replace')
            print('\n\nPlease check IP_PROJECT_XII database for hotel_booking table.....')
            wait = input()

        elif ch==3:
            break
    
def main_menu():
    while True:
        clear()
        print('MAIN MENU ')
        print('_'*100)
        print()
        print('1.  Read CSV File\n')
        print('2.  Data Analysis Menu\n')
        print('3.  Graph Menu\n')
        print('4.  Export Data\n')
        print('5.  Exit\n')
        choice = int(input('Enter your choice :'))

        if choice==1:
            read_csv_file()
            print('\n\n Press any key to continue....')
            wait = input()

        elif choice==2:
            data_analysis_menu()
            print('\n\n Press any key to continue....')
            wait = input()

        elif choice==3:
            graph()
            print('\n\n Press any key to continue....')
            wait = input()

        elif choice==4:
            break

main_menu()
