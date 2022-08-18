def create_calendar_page(month = None, year = None):
    import datetime
    row = ''
    if month is None:
        month = datetime.datetime.today().month
    if year is None:
        year = datetime.datetime.today().year

    day = datetime.datetime(year, month, 01)
    start_day = day.weekday()
    result = ""
    row = 20 * '-' + '\n' + 'MO TU WE TH FR SA SU\n' + 20 * '-' + '\n'

    for ch in range(1, 36):

        try:
            day = datetime.datetime(year, month, ch-start_day)
            row += str(day.day).zfill(2)
            if day.weekday() == 6:
                row += "\n"
            else:
                row += " "
        except ValueError:
            if ch < 7:
                row += "   "

    result = row.rstrip("\n")
    result = result.rstrip()
    return result
