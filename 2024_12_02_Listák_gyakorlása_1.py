import random

random_numbers = [random.randint(-60, 100) for _ in range(50)]

generalt_szamok = 1
for szam in random_numbers:
    generalt_szamok *= szam
print(f"1. A számok szorzata: {generalt_szamok}")

indices_divisible_by_5_or_7 = [i for i, szam in enumerate(random_numbers) if szam % 5 == 0 or szam % 7 == 0]
print(f"2. Indexek (5-tel vagy 7-tel osztható számok): {indices_divisible_by_5_or_7}")

indices_divisible_by_3_and_7 = [i for i, szam in enumerate(random_numbers) if szam % 3 == 0 and szam % 7 == 0]
print(f"3. Indexek (3-mal és 7-tel osztható számok): {indices_divisible_by_3_and_7}")

all_negative = all(szam < 0 for szam in random_numbers)
print(f"4. Minden szám negatív? {'Igen' if all_negative else 'Nem'}")

has_szamber_between_1_and_10 = any(1 <= szam <= 10 for szam in random_numbers)
print(f"5. Van 1 és 10 közötti szám? {'Igen' if has_szamber_between_1_and_10 else 'Nem'}")

count_divisible_by_18 = sum(1 for szam in random_numbers if szam % 18 == 0)
print(f"6. 18-cal osztható számok száma: {count_divisible_by_18}")

min_value = min(random_numbers)
index_legkisebb_szam = random_numbers.index(min_value)
print(f"7. Egyik legkisebb szám indexe: {index_legkisebb_szam}")

squares_divisible_by_17_or_18 = [szam ** 2 for szam in random_numbers if szam % 17 == 0 or szam % 18 == 0]
print(f"8. 17-tel vagy 18-cal osztható számok négyzete: {squares_divisible_by_17_or_18}")

negativ_mellett_paros = any(
    random_numbers[i] < 0 and (random_numbers[i - 1] > 0 if i > 0 else True) and (random_numbers[i + 1] > 0 if i < len(random_numbers) - 1 else True)
    for i in range(len(random_numbers))
)
print(f"9. Van negatív szám, melynek szomszédjai pozitívak? {'Igen' if negativ_mellett_paros else 'Nem'}")

is_monotonically_increasing = all(random_numbers[i] < random_numbers[i + 1] for i in range(len(random_numbers) - 1))
print(f"10. A sorozat szigorúan monoton növekvő? {'Igen' if is_monotonically_increasing else 'Nem'}")

paros = [szam for szam in random_numbers if szam % 2 == 0]
print(f"11. Páros számok: {paros}")
paratlan = [szam for szam in random_numbers if szam % 2 != 0]
print(f"11. Páratlan számok: {paratlan}")