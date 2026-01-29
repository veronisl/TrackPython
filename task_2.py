objem = 1.44  # объем в Мб на дискете
listov = 100 #кол-во страниц в одной книге
stroki = 50 # число строк на странице
simbols = 25 # кол-во символов в строке
bukva = 4 # место для хранения одного символ/байт

objem_perevod = objem * (1024 ** 2) # из Мб в байты
weight_book = bukva * simbols * stroki * listov # вес одной книги в байтах
books_together = round(objem_perevod // weight_book) # итого поместится

print("Количество книг, помещающихся на дискету:", books_together)