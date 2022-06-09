def preys_and_predators(r, a, b, m, p0, d0, max_length):
    
    def p(t, h):
        if (t==0):
            return p0
        else:
            result = p(t) + h * p_aux(t)
            return result

    def d(t, h):
        if (t==0):
            return d0
        else:
            result = d(t) + h * d_aux(t)
            return result

    def p_aux(t):
        result = r*p(t)-a*p(t)*d(t)
        return result

    def d_aux(t):
        result = b*p(t)*d(t)-m*d(t)
        return result