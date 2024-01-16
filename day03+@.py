subjects = {'python':'kim', 'c++':'sung', 'database':'kang', 'linux':'lee'}
print("{0[python]} {0[c++]}".format(subjects))
print(list(subjects.values())[1])
for i in subjects:
    print(i)
    print(i.index)
    print(f"key : {i}, value : {subjects[i]}")