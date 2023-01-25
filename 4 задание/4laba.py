with open('Астафьев_Михаил_Романович_ЗИТ_2022_vvod.txt','r') as firstfile, open('Астафьев_Михаил_Романович_ЗИТ_2022_vivod.txt','a') as secondfile:
    for line in firstfile:
        secondfile.write(line)
