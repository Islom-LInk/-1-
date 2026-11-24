# # индексы

# it = "python"
#     # 123456
# print(it[4])
# print(it[0:10])
# print(it[2:3])
# print(it[0] + it[1] + it[5])
# print(it[0:2] + it[2:5])

# p = (90, 90.09, "kk")
# print(type(p))


# ckear = ["RT", 99, 00.99]
# print(type(ckear))

# python = [1, "1", True, 1.1]
# print(type(python))

# как отличайтса списик от кортожа списипк [], кортож (),  список можна изминит а кортож нет 
namis = ['islom', 'bigzot', 'suka']
# print(namis)
# namis.append("asil") # добавлайэть элементь в концу списка
# print(namis)
# namis.append("beka") # добавлайть элемень в конце списпка 
# print(namis)
# namis.remove("beka") удалать по названия
# print(namis)
# namis.pop(1) удалйать по индеккис
# print(namis)
# namis.insert(1, 'ooo') добавлайть по индекис
# print(namis)
# namis[1] = 'pp' # изминайть элемен по индекист
# print(namis)

# cities = ["Bishkek", "Osh", "Narin", "Talas"]
# # print(cities[0:1])
# print(cities[::-1])#ВВывид в обратным поратке
# cities.sort()#сортируйть по алфавит 
# print(cities)
# cities.reverse()#ВВывид в обратным поратке
# print(cities)

# nombir = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# del nombir[0:5:1]
# print(nombir)
# print(max(nombir))#выдалайт самы болшой число 
# print(min(nombir))#выдалайть самы малиннки чисоло
# print(sum(nombir))#добавлайт все число 
# print(nombir.count(70))#считать сколка есть как он 

# contakt = ["islom"]
# nami = input("Введите имя: ").title()

# if nami in contakt:
#     print(nami, "есть")
# else:
#     print(nami, "нет в списке")

contacts = []
while True:
    opirator = input("1 - посмотред контак, 2 - добавить контакть, "
    "3 - удалить контакт, 4 - обнавить контакть")

    if opirator == "1":
        print(contacts)
    elif opirator == "2":
        add_vr = input("Кого хотите добавить: ").title()
        if add_vr in contacts:
            print("контакть ужи добавлень")
        else:
            contacts.append(add_vr)
            print("успешна добавлень контакть")
    elif opirator == "3":
        add_vr = input("пишиты названия кого хотит удалить: ").title()
        if add_vr in contacts:
            contacts.remove(add_vr)
            print("успешна удалон")
        else:
            print("не найдин")
    elif contacts == "4":
        up = input("кого хотите обнавить: ")
        if up in contacts:
            now = input("новы имя: ").title()
            contacts[contacts.index(up)] = now
            print("контакть успешна добавлень")
        else:
            print("не найдин контакть")

       