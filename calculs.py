def filtration(m0, x0, y0, xeau):
    m1 = m0 - m0 * x0                 # débit après filtration
    y1 = (m0 * y0) / m1               # fraction de soluble
    xeau1 = (m0 * xeau) / m1          # fraction d'eau
    return m1, y1, xeau1

def chauffage(m1, cp, t1, t2):
    q_kj_h = m1 * cp * (t2 - t1)      # kJ/h
    q_kw = q_kj_h / 3600              # kW
    return q_kj_h, q_kw