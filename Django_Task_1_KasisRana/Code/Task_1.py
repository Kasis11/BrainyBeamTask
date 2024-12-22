from datetime import date, timedelta

def get_tuesdays_and_fridays(year, month):
    """
    Returns all the Tuesdays and Fridays for a given month and year.
    """
    first_day = date(year, month, 1)
    result = []
    
    while first_day.month == month:
        if first_day.weekday() in [1, 4]:  # Tuesday = 1, Friday = 4
            result.append(first_day.strftime('%Y-%m-%d'))
        first_day += timedelta(days=1)
    
    return result

# Example usage
print(get_tuesdays_and_fridays(2024, 12))
