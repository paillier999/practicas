edad= input("introduce tu edad: ")

while(edad.isdigit()==False):

    print("Por favor introduce un valor numérico")
    edad = input("introduce tu edad: ")

if (int(edad) < 18):
    print("No puedes pasar")
else:
    print("Puedes pasar")