import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
# df = pd.DataFrame({
#     'id': [1, 2, 3],
#     'name': ["张三", "李四", "王五"],
#     'age': [20, 25, 30]
# })
#
# df = df.set_index("id")
# print(df)
# df.to_excel("F:/Python/excelHandel/people.xlsx")
# print("Done!")

# people = pd.read_excel("./people.xlsx")
# people.sort_values(by="age", inplace=True, ascending=False)
# print(people.name)
# plt.bar(people.name, people.age, color="orange")
# plt.title("People Age", fontsize=16)
# plt.xlabel("姓名")
# plt.ylabel("Age")
#
# plt.xticks(people.name, rotation='90')
# plt.tight_layout()
# plt.show()

people = pd.read_excel("./people.xlsx")
people['total'] = people['age'] + people['score']
people.sort_values(by="total", inplace=True)

people.plot.bar(x='name', y=['age', 'score'], stacked=True)
plt.tight_layout()
plt.show()
