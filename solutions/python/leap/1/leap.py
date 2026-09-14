def leap_year(year):
    """ Determin wether a given year is a leap year
    parameters:
        year (int):the year to check
        
    Returns:
        bool: True if the year is leap year otherwise, False 
    """
    divisible_by_four = year%4==0
    divisible_by_hundred = year%100==0
    divisible_by_four_hundred = year%400==0

    return (divisible_by_four and not divisible_by_hundred) or divisible_by_four_hundred
    
