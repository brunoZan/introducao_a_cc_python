input_seconds = int(input("Por favor, entre com o número de segundos que deseja converter: "))


dias = input_seconds // 86400

seg_restantes_pra_hras = input_seconds % 86400

horas = seg_restantes_pra_hras // 3600

seg_restantes_pra_min = seg_restantes_pra_hras % 3600

minutos = seg_restantes_pra_min // 60

segundos =  seg_restantes_pra_min % 60

print(dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")