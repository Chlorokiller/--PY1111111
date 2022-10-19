src = not False and True or False and not True
# result = True or False and False # сначала по правилам устраняем отрицания
# result = True or False # согласно правилам, далее идёт лог. умножение
# result = True # в конце идёт логическое сложение

result = True

print(src == result)
