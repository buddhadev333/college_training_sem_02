import matplotlib.pyplot as plt

x = ['A','B','C']
y = [10,20,30]

plt.bar(x,y)
plt.show()


# import matplotlib.pyplot as plt

# plt.bar(['A','B','C'], [5,15,25], color='orange')
# plt.show()


# import matplotlib.pyplot as plt

# plt.barh(['A','B','C'], [10,20,30])
# plt.show()


# import matplotlib.pyplot as plt

# plt.bar(['A','B','C'], [10,20,30])
# plt.title("Bar Chart Example")
# plt.xlabel("Categories")
# plt.ylabel("Values")
# plt.show()



# import matplotlib.pyplot as plt

# x = ['A','B','C']
# y1 = [10,20,30]
# y2 = [15,25,35]

# plt.bar(x,y1)
# plt.bar(x,y2)
# plt.show()


# import matplotlib.pyplot as plt

# plt.bar(['A','B','C'], [10,20,30], width=0.3)
# plt.show()




# import matplotlib.pyplot as plt

# plt.bar(['A','B','C'], [10,20,30])
# plt.grid(True)
# plt.show()


# import matplotlib.pyplot as plt

# colors = ['red','green','blue']
# plt.bar(['A','B','C'], [10,20,30], color=colors)
# plt.show()




# import matplotlib.pyplot as plt

# x = ['A','B','C']
# y1 = [10,20,30]
# y2 = [5,10,15]

# plt.bar(x,y1)
# plt.bar(x,y2, bottom=y1)
# plt.show()



# import matplotlib.pyplot as plt

# x = ['A','B','C']
# y = [10,20,30]

# plt.bar(x,y)

# for i in range(len(x)):
#     plt.text(i, y[i], y[i])

# plt.show()




# import matplotlib.pyplot as plt

# # Months
# months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']

# # Sales data (3 products)
# product_A = [120, 150, 170, 200, 220, 250, 270, 300, 320, 350, 370, 400]
# product_B = [100, 130, 160, 180, 210, 230, 260, 280, 300, 330, 360, 390]
# product_C = [90, 110, 140, 160, 190, 210, 240, 260, 280, 300, 320, 350]

# # Create figure
# plt.figure(figsize=(10,5))

# # Plot lines
# plt.plot(months, product_A, marker='o', label='Product A')
# plt.plot(months, product_B, marker='s', label='Product B')
# plt.plot(months, product_C, marker='^', label='Product C')

# # Title and labels
# plt.title("Monthly Sales Analysis (2025)")
# plt.xlabel("Months")
# plt.ylabel("Sales")

# # Grid & legend
# plt.grid(True)
# plt.legend()

# # Show values on top (for Product A only)
# for i in range(len(months)):
#     plt.text(i, product_A[i], product_A[i])

# # Show plot
# plt.show()