S = "Hello World"
output_file = "string_operations.txt"

# Состоит ли строка из символов в нижнем регистре
is_lower = S.islower()
with open(output_file, 'a') as f:
    f.write(f"S.islower() --> {is_lower}\n")

# Состоит ли строка из символов в верхнем регистре
is_upper = S.isupper()
with open(output_file, 'a') as f:
    f.write(f"S.isupper() --> {is_upper}\n")

# Начинаются ли слова в строке с заглавной буквы
is_title = S.istitle()
with open(output_file, 'a') as f:
    f.write(f"S.istitle() --> {is_title}\n")

# Преобразование строки к верхнему регистру
upper_case = S.upper()
with open(output_file, 'a') as f:
    f.write(f"S.upper() --> {upper_case}\n")

# Преобразование строки к нижнему регистру
lower_case = S.lower()
with open(output_file, 'a') as f:
    f.write(f"S.lower() --> {lower_case}\n")

# Первую букву каждого слова переводит в верх. регистр, остальные в нижний
title_case = S.title()
with open(output_file, 'a') as f:
    f.write(f"S.title() --> {title_case}\n")

# Переводит первый символ строки в верхний регистр, остальные в нижний
capitalize = S.capitalize()
with open(output_file, 'a') as f:
    f.write(f"S.capitalize() --> {capitalize}\n")
