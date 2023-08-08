#Eingabe
Zahl1 = int(input("Gib eine Zahl ein: "))
overlay = input ("(+) Addition , (-) Subtraktion , (*) Multiplikation , (/) Division: ")
Zahl2 = int(input("Gib deine zweite Zahl ein: "))

# Addition
if overlay == "+":
    print("Dein Ergebnis lautet: " + str(Zahl1 + Zahl2))

# Subtraktion
elif overlay == "-":
    print("Dein Ergebnis lautet: " + str(Zahl1 - Zahl2))

# Multiplikation
elif overlay == "*":
    print("Dein Ergebnis lautet: " + str(Zahl1 * Zahl2))

# Division
elif overlay == "/":
    print("Dein Ergebnis lautet: " + str(Zahl1 / Zahl2))
# Wenn kein Rechenoperator verwendet wird
else:
    print("Deine Eingabe ist ungültig")

input("Beliebige Taste drücken zum beenden.")