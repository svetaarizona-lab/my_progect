#Ваше завдання — написати програму, яка переводить число у формат часу у читальному вигляді.
#Користувач повинен ввести число більше або дорівнює 0 і менше ніж 8640000.

sec = int(input("Please: enter the sec :  (0 ≤ число < 8640000): "))

if 0 <= sec < 8640000:
    days = sec // 86400
    sec %= 86400

    hours = sec // 3600
    sec %= 3600

    minutes = sec // 60
    sec %= 60

    if days % 10 == 1 and days % 100 != 11:
        day = "день"
    elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
        day = "дні"
    else:
        day = "днів"
    h = str(hours).zfill(2)
    m = str(minutes).zfill(2)
    s = str(sec).zfill(2)

    print(f"{days} {day}, {hours:02d}:{minutes:02d}:{sec:02d}")
else:
    print("ERROR")