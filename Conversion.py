def metric(length, width):
    length = int(length)
    width = int(width)

    f_squared = length * width
    m_squared = f_squared * .09290304

    return round(m_squared, 4)

def imperial(length, width):
    length = int(length)
    width = int(width)

    m_squared = length * width
    f_squared = m_squared / .09290304

    return round(f_squared, 4)
