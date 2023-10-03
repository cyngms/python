# with open("resultados-del-test.csv") as fil:
#     i = 0
#     for line in fil.readlines():
#         print(line)
#         i += 1
#         if i == 10:
#             break

import pandas
datos = pandas.read_csv("resultados-del-test.csv")
print(datos.edad.tail())
pass
