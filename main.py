import random
from logic import calculate_total
from visual import show_total

# Liste mit 5 zufälligen Preisen zwischen 1.00 und 50.00 €
preise = [round(random.uniform(1, 50), 2) for _ in range(5)]

print("Preise:", preise)

gesamt = calculate_total(preise)
show_total(gesamt)