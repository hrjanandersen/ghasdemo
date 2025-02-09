from datetime import datetime

def compare_dates(specified_date_str):
    # Get today's date
    today = datetime.today().date()
    
    # Convert the specified date string to a date object
    specified_date = datetime.strptime(specified_date_str, '%Y-%m-%d').date()
    
    # Compare the dates
    if today > specified_date:
        print(f"Today's date ({today}) is after the specified date ({specified_date}).")
    elif today < specified_date:
        print(f"Today's date ({today}) is before the specified date ({specified_date}).")
    else:
        print(f"Today's date ({today}) is the same as the specified date ({specified_date}).")

# Example usage
specified_date_str = '2025-02-10'
compare_dates(specified_date_str)
