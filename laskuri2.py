while True:
    matka_syote = input("Anna matka metreissä (tai 'end' lopettaaksesi): ")

    if matka_syote.lower() == "end":
        print("Ohjelma lopetettu.")
        break

    try:
        matka = float(matka_syote)

        minuutit = int(input("Anna aika minuutteina: "))
        sekunnit = int(input("Anna aika sekunteina: "))

        kokonaisaika_sek = minuutit * 60 + sekunnit
        matka_km = matka / 1000

        if matka_km > 0 and kokonaisaika_sek > 0:
            keskivauhti_sek_per_km = kokonaisaika_sek / matka_km

            vauhti_min = int(keskivauhti_sek_per_km // 60)
            vauhti_sek = round(keskivauhti_sek_per_km % 60)

            print(f"\nMatka: {matka} m ({matka_km:.2f} km)")
            print(f"Aika: {minuutit} min {sekunnit} s ({kokonaisaika_sek} s)")
            print(f"Keskivauhti: {vauhti_min} min {vauhti_sek} s / km\n")
        else:
            print("Matkan ja ajan täytyy olla suurempia kuin 0.\n")

    except ValueError:
        print("Syötteiden täytyy olla numeroita.\n")