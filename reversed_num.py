def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    sign = -1 if x < 0 else 1
    val_str = str(abs(x))
    rev_str = int(val_str[::-1])*sign
    return rev_str

print(reverse(-135))