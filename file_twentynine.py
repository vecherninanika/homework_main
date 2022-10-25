from datetime import timedelta
from datetime import date


def func(notes: list, day: date):
    """Write the captain's notes and their date.

    Args:
        notes(list): captain's notes
        day(date): the first day

    """
    with open('file_2809', 'a') as file_with_notes:
        for note in notes:
            file_with_notes.write(str(day), '\n')
            day += timedelta(days=1)
            file_with_notes.write(note)


notes_inp = [
    'Es dia uno de nuestro viaje\n',
    'Ya estamos muy lejos de Daidu\n',
    'LLegamos a Koryo en dos dias\n'
]
year = 2022
month = 5
day = 18
day_inp = date(year, month, day)

func(notes_inp, day_inp)
