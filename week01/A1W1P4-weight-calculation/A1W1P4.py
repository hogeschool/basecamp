# An online retailer sells two products: widgets and gizmos.
# Write a program that reads the number of widgets and the number of gizmos in an order from the user.
# Then your program should compute and display the total weight of the order.
# Criteria:

#    Each widget weighs 75 grams
#    Each gizmo weighs 112 grams

# Input example:

# Number of widgets: 10
# Number of gizmos: 1
# Output example:

# The Total Weight of the Order: 862 grams

# Input informatie en context
print("Please state the amount of widgets and gizmos in your possession.")
n_widgets = int(input("How many widgets do you have: "))
n_gizmos = int(input("How many gizmos do you have: "))

# calculation of weight
t_widgets = n_widgets * 75
t_gizmos = n_gizmos * 112
t_weight = t_widgets + t_gizmos

# output
print(f"The Total Weight of the Order: {t_weight} grams")


# ---------------------------------------------------------------
# Wat ik van deze opdracht geleerd heb
# ---------------------------------------------------------------

# 1. Elke functie geeft iets terug, print() geeft None terug.
#    Daardoor werd float(print("...")) eigenlijk float(None) en crashte het
#    met: TypeError: float() argument must be a string or a real number.

# 2. input() geeft ALTIJD een string terug, ook als je een getal typt.
#    Daarom moet je die omzetten met int() of float() voordat je ermee rekent.

# 3. int() of float() kiezen hangt van de opdracht af.
#    Widgets en gizmos zijn hele stuks, dus int(). Bij de room area opdracht
#    kon de lengte 5.5 zijn, dus daar float(). Met int() print het antwoord
#    als 862, met float() als 862.0.

# 4. Je kunt geen string en een getal aan elkaar plakken met +.
#    "Total: " + t_weight geeft:
#    TypeError: can only concatenate str (not "int") to str
#    Oplossingen:
#       print("The Total Weight of the Order:", t_weight, "grams")
#       print(f"The Total Weight of the Order: {t_weight} grams")
#    Bij komma's zet print automatisch spaties ertussen, bij een f-string
#    bepaal ik de spaties zelf tussen de { }.
