# datetime-Paket
from datetime import datetime, timedelta, date


# 1 Aktuelles Datum und Uhrzeit ausgeben:
def aktuelles_datum_und_uhrzeit():
    now = datetime.now()
    print("Aktuelles datum und uhrzeit : ", now)
    d_u_inf = now.strftime("%d.%m.%Y %H:%M:%S")
    print("Datum und Uhrezeit im Format : ", d_u_inf)


# 2 Differenz bis zum Jahresende berechnen:
def tage_bis_jahresende():
    heute = date.today()
    end_of_year = date(date.today.year(), 12, 31)
    delta = end_of_year - heute

    # print(type(heute), heute)
    # print(type(end_of_year), end_of_year)
    print(f"noch {delta.days} tage bis 31. Dezember.")


# 3 Benutzerdefiniertes Datum:


# def tage_bis_datum():
#     end_tag = datetime(2024, 12, 31)
#     input_date_str = input("Pleace enter a Date (YYYY.MM.DD): ")
#     input_date = datetime.strptime(input_date_str, "%Y.%m.%d")
#     # print(type(input_date), input_date)
#     # print(type(end_tag), end_tag)
#     if input_date <= end_tag:
#         diff_tags = end_tag - input_date
#         print(diff_tags)
#     elif input_date > end_tag:
#         diff_tags = end_tag - input_date
#         print(f"{abs(diff_tags)}")
#         return tage_bis_datum()
#     else:
#         print("error")
#         return tage_bis_datum()


def tage_bis_datum():
    while True:
        try:
            # user input datum
            datum_str = input("Bitte geben Sie ein Datum im Format TT.MM.JJJJ ein: ")

            # stringer to datum
            datum = datetime.strptime(datum_str, "%d.%m.%Y").date()

            # today
            heute = datetime.today().date()
            print(f"{type (heute)}", heute)

            # rechnen
            differenz = (datum - heute).days
            print(f"{type (differenz)}", differenz)

            # output
            print(f"Es sind {abs(differenz.days)} Tage von heute bis zum {datum_str}.")
            break
        except ValueError:
            print("Ungültiges Datum. Bitte versuchen Sie es erneut.")


# 4 Wochentag berechnen:
def wochentag_berechnen():
    ruls = {
        0: "Montag",
        1: "Dienstag",
        2: "Mittwoch",
        3: "Donnerstag",
        4: "Freitag",
        5: "Samstag",
        6: "Sonntag",
    }
    input_date_str = input("Pleace enter a Date (YYYY.MM.DD): ")
    input_date = datetime.strptime(input_date_str, "%Y.%m.%d")
    wochentag_num = input_date.weekday()

    print(f"{input_date} ist {ruls[wochentag_num]}")


# 5 Zeitverschiebung berechnen:
def zeit_in_zukunft():
    while True:
        now = datetime.now()
        eingabe = input(
            "Bitte geben Sie die Zeit an (z.B. '3d' für 3 Tage, '2h' für 2 Stunden, '45m' für 45 Minuten): "
        )

        if eingabe.endswith("d"):
            try:
                tage = int(eingabe[:-1])
                future_time = now + timedelta(days=tage)
                print(f"Sie haben {tage} Tage eingegeben.")
                print(
                    f"Zukünftiges Datum und Zeit: {future_time.strftime('%d.%m.%Y %H:%M:%S')}"
                )
                return
            except ValueError:
                print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")

        elif eingabe.endswith("h"):
            try:
                stunden = int(eingabe[:-1])
                future_time = now + timedelta(hours=stunden)
                print(f"Sie haben {stunden} Stunden eingegeben.")
                print(
                    f"Zukünftiges Datum und Zeit: {future_time.strftime('%d.%m.%Y %H:%M:%S')}"
                )
                return
            except ValueError:
                print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")

        elif eingabe.endswith("m"):
            try:
                minuten = int(eingabe[:-1])
                future_time = now + timedelta(minutes=minuten)
                print(f"Sie haben {minuten} Minuten eingegeben.")
                print(
                    f"Zukünftiges Datum und Zeit: {future_time.strftime('%d.%m.%Y %H:%M:%S')}"
                )
                return
            except ValueError:
                print("Ungültige Eingabe. Bitte versuchen Sie es erneut.")

        else:
            print(
                "Ungültige Eingabe. Bitte geben Sie die Zeit in der Form 'Xd', 'Yh' oder 'Zm' ein."
            )


# Main
# aktuelles_datum_und_uhrzeit()
# tage_bis_jahresende()
# tage_bis_datum()
wochentag_berechnen()
# zeit_in_zukunft()
