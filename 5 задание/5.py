a = int(input("Введите номер зачётки: "))
if a == 12:
    my_file = open("result.txt", "w")
    my_file.write("Dismas379.json")
    my_file.close()
    with open('Dismas379.json', 'r') as file:
        read_file = file.read()
    print(read_file)
else:
    print("Данный номер зачетки отсутсвует в базе.")
