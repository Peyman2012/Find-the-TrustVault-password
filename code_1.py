import random
import mysql.connector as msql
import pandas as pd
from mysql.connector import Error
# fixMnemonics  = ["s1", "s2", "s3","code4"]
# Mnemonics     = [ "code5", "code6", "code7", "code8", "code9", "code10" , "code11","code12"]
# fixMnemonics_2  = ["s1", "s2", "s3","code5"]
# Mnemonics_2     = [ "code4", "code6", "code7", "code8", "code9", "code10" , "code11","code12"]
# fixMnemonics_3  = ["s1", "s2", "s3","code6"]
# Mnemonics_3     = [ "code4", "code5", "code7", "code8", "code9", "code10" , "code11","code12"]
# fixMnemonics_4  = ["s1", "s2", "s3","code7"]
# Mnemonics_4     = [ "code4", "code5", "code6", "code8", "code9", "code10" , "code11","code12"]
# fixMnemonics_5  = ["s1", "s2", "s3","code8"]
# Mnemonics_5     = [ "code4", "code5", "code6", "code7", "code9", "code10" , "code11","code12"]
# fixMnemonics_6  = ["s1", "s2", "s3","code9"]
# Mnemonics_6     = [ "code4", "code5", "code6", "code7", "code8", "code10" , "code11","code12"]
# fixMnemonics_7  = ["s1", "s2", "s3","code10"]
# Mnemonics_7     = [ "code4", "code5", "code6", "code7", "code8", "code9" , "code11","code12"]
# fixMnemonics_8  = ["s1", "s2", "s3","code11"]
# Mnemonics_8     = [ "code4", "code5", "code6", "code7", "code8", "code9" , "code10","code12"]
# fixMnemonics_9  = ["s1", "s2", "s3","code11"]
# Mnemonics_9     = [ "code4", "code5", "code6", "code7", "code8", "code9" , "code10","code11"]
# fixMnemonics_10  = ["s1", "s2", "s3"]
# Mnemonics_10     = [ "code4","code5", "code6", "code7", "code8", "code9", "code10" , "code11","code12"]
#
# out = []
# out_2 = []
# out_3 = []
# out_4 = []
# out_5 = []
# out_6 = []
# out_7 = []
# out_8 = []
# out_9 = []
# out_10 = []
# i = 4
# q = 0
# randMnemonics = []
# randMnemonics_2 = []
# randMnemonics_3 = []
# randMnemonics_4 = []
# randMnemonics_5 = []
# randMnemonics_6 = []
# randMnemonics_7 = []
# randMnemonics_8 = []
# randMnemonics_9 = []
# randMnemonics_10 = []
#
# while q <= 90000:
#     randMnemonics.clear()
#     randMnemonics = Mnemonics.copy()
#     random.shuffle(randMnemonics)
#     outMnemonics = fixMnemonics + randMnemonics
#
#     out.append(outMnemonics)
#     randMnemonics_2.clear()
#     randMnemonics_2 = Mnemonics_2.copy()
#     random.shuffle(randMnemonics_2)
#     outMnemonics_2 = fixMnemonics_2 + randMnemonics_2
#     out_2.append(outMnemonics_2)
#
#     randMnemonics_3.clear()
#     randMnemonics_3 = Mnemonics_3.copy()
#     random.shuffle(randMnemonics_3)
#     outMnemonics_3 = fixMnemonics_3 + randMnemonics_3
#     out_3.append(outMnemonics_3)
#
#     randMnemonics_4.clear()
#     randMnemonics_4 = Mnemonics_4.copy()
#     random.shuffle(randMnemonics_4)
#     outMnemonics_4 = fixMnemonics_4 + randMnemonics_4
#     out_4.append(outMnemonics_4)
#
#     randMnemonics_5.clear()
#     randMnemonics_5 = Mnemonics_5.copy()
#     random.shuffle(randMnemonics_5)
#     outMnemonics_5 = fixMnemonics_5 + randMnemonics_5
#     out_5.append(outMnemonics_5)
#
#     randMnemonics_6.clear()
#     randMnemonics_6 = Mnemonics_6.copy()
#     random.shuffle(randMnemonics_6)
#     outMnemonics_6 = fixMnemonics_6 + randMnemonics_6
#     out_6.append(outMnemonics_6)
#
#     randMnemonics_7.clear()
#     randMnemonics_7 = Mnemonics_7.copy()
#     random.shuffle(randMnemonics_7)
#     outMnemonics_7 = fixMnemonics_7 + randMnemonics_7
#     out_7.append(outMnemonics_7)
#
#     randMnemonics_8.clear()
#     randMnemonics_8 = Mnemonics_8.copy()
#     random.shuffle(randMnemonics_8)
#     outMnemonics_8 = fixMnemonics_8 + randMnemonics_8
#     out_8.append(outMnemonics_8)
#
#     randMnemonics_9.clear()
#     randMnemonics_9 = Mnemonics_9.copy()
#     random.shuffle(randMnemonics_9)
#     outMnemonics_9 = fixMnemonics_9 + randMnemonics_9
#     out_9.append(outMnemonics_9)
#
#     randMnemonics_10.clear()
#     randMnemonics_10 = Mnemonics_10.copy()
#     random.shuffle(randMnemonics_10)
#     outMnemonics_10 = fixMnemonics_10 + randMnemonics_10
#     out_10.append(outMnemonics_10)
#     #print(outMnemonics)
#     q = q + 1
# list_1=[]
# list_2 = []
# list_3 = []
# list_4 = []
# list_5 = []
# list_6 = []
# list_7 = []
# list_8 = []
# list_9 = []
# list_10 = []
# for i in range(len(out)):
#     for j in range(len(out[i])):
#         list_1.append(out[i][j])
#
# for i in range(len(out_2)):
#     for j in range(len(out_2[i])):
#         list_2.append(out_2[i][j])
#
# for i in range(len(out_3)):
#     for j in range(len(out_3[i])):
#         list_3.append(out_3[i][j])
#
# for i in range(len(out_4)):
#     for j in range(len(out_4[i])):
#         list_4.append(out_4[i][j])
#
# for i in range(len(out_5)):
#     for j in range(len(out_5[i])):
#         list_5.append(out_5[i][j])
#
# for i in range(len(out_6)):
#     for j in range(len(out_6[i])):
#         list_6.append(out_6[i][j])
#
# for i in range(len(out_7)):
#     for j in range(len(out_7[i])):
#         list_7.append(out_7[i][j])
#
# for i in range(len(out_8)):
#     for j in range(len(out_8[i])):
#         list_8.append(out_8[i][j])
#
# for i in range(len(out_9)):
#     for j in range(len(out_9[i])):
#         list_9.append(out_9[i][j])
#
# for i in range(len(out_10)):
#     for j in range(len(out_10[i])):
#         list_10.append(out_10[i][j])
#
# values_1 = [list([item]) for item in list_1]
# values_2 = [list([item]) for item in list_2]
# values_3 = [list([item]) for item in list_3]
# values_4 = [list([item]) for item in list_4]
# values_5 = [list([item]) for item in list_5]
# values_6 = [list([item]) for item in list_6]
# values_7 = [list([item]) for item in list_7]
# values_8 = [list([item]) for item in list_8]
# values_9 = [list([item]) for item in list_9]
# values_10 = [list([item]) for item in list_10]
#
# va_1=[]
# va_2=[]
# va_3=[]
# va_4=[]
# va_5=[]
# va_6=[]
# va_7=[]
# va_8=[]
# va_9=[]
# va_10=[]
#
# # print(values_1)
#
# for i in range(len(values_1)):
#     for j in range(len(values_1[i])):
#         va_1.append(values_1[i][j])
#
# for i in range(len(values_2)):
#     for j in range(len(values_2[i])):
#         va_2.append(values_2[i][j])
#
# for i in range(len(values_3)):
#     for j in range(len(values_3[i])):
#         va_3.append(values_3[i][j])
#
# for i in range(len(values_4)):
#     for j in range(len(values_4[i])):
#         va_4.append(values_4[i][j])
#
# for i in range(len(values_5)):
#     for j in range(len(values_5[i])):
#         va_5.append(values_5[i][j])
#
# for i in range(len(values_6)):
#     for j in range(len(values_6[i])):
#         va_6.append(values_6[i][j])
#
# for i in range(len(values_7)):
#     for j in range(len(values_7[i])):
#         va_7.append(values_7[i][j])
#
# for i in range(len(values_8)):
#     for j in range(len(values_8[i])):
#         va_8.append(values_8[i][j])
#
# for i in range(len(values_9)):
#     for j in range(len(values_9[i])):
#         va_9.append(values_9[i][j])
#
# for i in range(len(values_10)):
#     for j in range(len(values_10[i])):
#         va_10.append(values_10[i][j])
#
# # print(va_5)
# #
# dic={'code_1':va_1,'code_2':va_2,'code_3':va_3,'code_4':va_4,'code_5':va_5,'code_6':va_6,'code_7':va_7,'code_8':va_8,'code_9':va_9,'code_10':va_10}
# df=pd.DataFrame(dic)
# df.to_csv('password_wallet_find_code.csv',index=False)
# print(df)

empdata = pd.read_csv('C:\\Users\\peyman\\Desktop\\trust wallet\\password_wallet_find_code.csv')
# print(empdata.head())
try:
    con = msql.connect(host='127.0.0.1',user='root',password='peiman2012')
    if con.is_connected():
        cursor = con.cursor()
        cursor.execute("create database FindCodePasswordWallet")
        print("Databases is created....")

except Error as e :
    print("Error while connecting to MYSQL",e)

try:
    con = msql.connect(host='127.0.0.1',
                       user='root',
                       password='peiman2012',
                       database='FindCodePasswordWallet'
                       )
    if con.is_connected():
        cursor=con.cursor()
        cursor.execute("select database();")
        record=cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('drop table if exists WalletFindCode;')
        print('Creating table....')
        cursor.execute("create table WalletFindCode ( code_1 char(30), code_2 char(30),code_3 char(30),code_4 char(30),code_5 char(30),code_6 char(30),code_7 char(30),code_8 char(30),code_9 char(30),code_10 char(30))")
        print("Table is created....")
        x=0

        for i,row in empdata.iterrows():
            sql="INSERT INTO WalletFindCode VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql,tuple(row))
            x+=1
            print(x)
            print("Record inserted")
            con.commit()
except Error as e :
    print("Error while connecting to MYSQL",e)

sql = "SELECT * FROM WalletFindCode "
cursor.execute(sql)
# Fetch all the records
result = cursor.fetchall()
for i in result:
    print(i)
con.close()
