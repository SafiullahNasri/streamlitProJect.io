# print("Hello aram")

# def ram(n):
#     print(n)
# ram("I love you")


# print("Hello world")
# numbers = [1,2,3,4,4,5,6,7,-7,-5,-4,-3]
# positive_numbers = 0
# for num in numbers:
#     if num>0:
#         positive_numbers+=1
# print(positive_numbers)



# 
# n = 10
# sum_even = 0
# for i in range(1, n+1):
#     if i%2==0:
#         sum_even+=1
# print(sum_even)


# n = 10 
# for i in range(1,11):
#     print(n, " X ", i, " = ", n*i)

# n = 10 
# for i in range(1,11):
#     if i==5:
#         continue
#     print(n, " X ", i, " = ", n*i)



# input_str = "Python"
# revers_str = ""

# for char in input_str:
#     # print(input_str)
#     # revers_str = revers_str+char
#     revers_str = char+revers_str
# print(revers_str)



# input_str = "teeter"
# for char in input_str:
#     # print(char)
#     if input_str.count(char)==1:
#         print(char)
#         break



# number  = 5
# factorial = 1

# while number>0:
#     factorial  = factorial*number
#     number = number-1

# print(factorial)



# while True:
#     number = int(input("Enter the nuber? "))

#     if 1<= number <=10:
#         print("wow")
#         break
#     else:
#         print("invalid ")

# # 
# number = 28
# # number = 29
# is_prime = True

# if number>1:
#     for i in range(2, number):
#         if number%i==0:
#             is_prime = False
#             break
    

# print(is_prime)


# items = ["apple", "bannaa", "orange", "apple"]

# unique_item = set()
# for item in items:
#     if item in unique_item:
#         print(item)
#         break
#     unique_item.add(item)

















# import time
# aite_time = 1
# iterate_time = 5
# attempts = 0

# while attempts<iterate_time:
#     print(attempts +1, aite_time)
#     time.sleep(aite_time)
#     aite_time*=2
#     attempts+=1


# import time
# f = open('open.py')
# print(f.readlines())

# for line in open('open.py'):
#     print(line, end=' ')



# for line in open('open.py'):
#     print(line, end=' ')

# f = open('open.py')
# while True:
#     line = f.readline()
#     if not line: break
#     print(line) 


# f  = open('open.py')
# while True:
#     line = f.readline()
#     if not line:break
#     print(line, end=' ')

# for line in open('open.py'):
    # print(line)



# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import numpy as np
# import plotly.graph_objects as go

# st.write("ProfessionalDashbord ")








# ##importar as bibliotecas 
# import streamlit as st 
# import pandas as pd
# import plotly.express as px 
# import plotly.graph_objects as go

# ##Abrir no csv
# df = pd.read_csv(r"D:\hello\NDVI__Precipitation__and_Temperature_Data.csv")

# ##Converter a primeira para
# df['Date']= pd.to_datetime(df['Date'])

# df['Year-Month']= df['Date'].dt.to_period('M')

# ##Agregar dados 
# df_monthly = df.groupby('Year-Month').agg({
#     'Precipitation (mm)':'sum',
#     'Temperature (°C)':'mean',
#     'NDVI': 'mean'  
    
# }).reset_index()

# ##Gerar nosso
# ndvi_trace = go.Scatter(x=df_monthly['Year-Month'].astype(str),
#                         y=df_monthly['NDVI'],
#                         mode='lines',
#                         name='NDVI',
#                         line=dict(color='green'))

# precipitation_trace = go.Bar(x=df_monthly['Year-Month'].astype(str),
#                         y=df_monthly['Precipitation (mm)'],
#                         name='Precipitação',
#                         yaxis='y2',
#                         opacity=0.6,
#                         marker=dict(color='blue'))


# layout =go.Layout(
#     title='NDVI e Precipitação Mensal',
#     xaxis=dict(title='Mês'),
#     yaxis=dict(title='NDVI', range=[0,1]),
#     yaxis2=dict(title='Precipitação', overlaying='y', side='right'),
#     legend=dict(x=0, y=1.1, orientation='h'),
#     barmode='overlay'
    
# )

# fig1 = go.Figure(data=[ndvi_trace,precipitation_trace], layout=layout)

# ###Definir a figura 2 
# # Gráfico de heatmap para Temperatura
# heatmap_data = df_monthly.pivot_table(index=df_monthly['Year-Month'].dt.year, columns=df_monthly['Year-Month'].dt.month, values='Temperature (°C)')

# fig2= px.imshow(
#     heatmap_data,
#     labels=dict(x= 'Month',y ='Year', color='Temperature (°C)'),
#     x=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
#     title="Temperature Heatmap Over 24 Months",
#     color_continuous_scale="RdYlGn"
# )

# ##Set configuração da pagina
# st.set_page_config(layout='wide',
#                    initial_sidebar_state='expanded')

# st.sidebar.write('Pro App criado para apresentação dos resultados de NDVI, Precipitação e Temperatura da Fazenda Youtube')
# st.sidebar.image(r'D:\hello\ndvi.png')

# ##Criar um titulo
# st.title('PRO, Precipitação e Temperatura Dashboard')

# st.dataframe(df_monthly, width=1200, height=400)

# ##Colunas 
# col1, col2 = st.columns([0.5,0.5])

# with col1:
#     st.subheader('NDVI e Precipitação')
#     st.plotly_chart(fig1)
    
# with col2:
#     st.subheader('Temperatura')
#     st.plotly_chart(fig2)











# print("Hello world")
# cal = 24;
# units = "hourse"

# def day(no_days):
#     if no_days>0:

#         return f"{no_days} are {cal*no_days} {units}"
#     else:
#         print("you entered the negative numbers")
# define = day(-10)
# print(define)



a  = 1
b = '1'
c = "1"
d = 1.0
print(a)
print(b)
print(c)
print(d)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
x = "Python"
y = 'OneShot'
print(x)
print(y)
print(id(a))
python = 1
py_thon = 1
_python = 1
Python = 1
PYTHON = 1
python1 = 1
# if = 1        # invalid resevred wrd
# 1python = 1   # invalid vairabl ename
# py$thon = 1
# pyth@thon = 1    # invalid also

variable1, variable2, vairalble3 = '1', '2', '3'
variable1 = variable2=vairalble3=5
print(variable1)
print(variable2)
print(vairalble3)

# comments:
'''
This is an example fo the comment multiline ones
'''
print('commnets')

# dtypes:
d1 = 5
d2 = "safiullah"
d3 = 5.0
d4 = True
d5 = 5j
d6 = [1,2,3,4,5]
d7 = {1,2,3,9}
d8 = (91,2,4,5)
d9 = {"naam": 'love', 'kamal': 'jamal'}
d10 = None
print(type(d1))
print(type(d2))
print(type(d3))
print(type(d4))
print(type(d5))
print(type(d6))
print(type(d7))
print(type(d8))
print(type(d9))
print(type(d10))

A = '''Hello and welcome dosto 
to 5 minutese engineering,
aaj ka video bada kamal ka hone wala hai'''
print(A)


B = """Hello and welcome dosto 
to 5 minutese engineering,
aaj ka video bada kamal ka hone wala hai"""
print(B)

C = 'SafiullahNasri'
print(C[0])
print(C[1])
print(C[2])
print(C[4])
print(C[5])
print(C[6])
print(C[7])
print(C[8])
print(C[9])
print(C[10])

print(len(A))
print(len(B))
print(len(C))



# type conversion
intt = 5
flt = 5.0
add = intt+flt
print(type(add))
add


# intt = 5
# strr = '5'
# adddd = intt+strr
# print(type(intt+strr))
# adddd


intt = 5
strr = '5'
adddd = intt+int(strr)
print(type(adddd))
adddd





# operators in the python

x = 2
y = 5
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)
print(x**y)


# Comparison operators

print(x==y)
print(x!=y)
print(x<y)
print(x>y)
print(x<=y)
print(x>=y)
# print(x==y)

# Assignments operators

