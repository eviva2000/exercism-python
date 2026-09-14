def square(number):
    """"Return the number of grains on a given chessboard square
    
        Parameters(int):
            number of square
        Returns(int):
            number of grains on that square
        Raises:
        ValueError, if teh number is out of the range 1 to 64
        
    """
    is_in_range = 1<=number<=64
    if not is_in_range:
        raise ValueError("square must be between 1 and 64")
    return 2**(number-1)


def total():
    """" Returns the total number of grains on a chessboard
    """
    total_number=0
    for i in range(1,65):
       total_number+= square(i)

    return total_number