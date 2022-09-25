import math

x1 = float(input("primeira condenadaX: "))
y1 = float(input("primeiro condenadaY: "))
x2 = float(input("segunda condenadaX: "))
y2 = float(input("segunda condenadaY: "))

distandia = math.sqrt(((x2 - x1)**2) + ((y2 - y1)**2))

if distandia >= 10:
	print("longe")
else:
	print("perto")