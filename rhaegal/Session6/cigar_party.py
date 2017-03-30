def cigar_party(cigars, is_weekend):
    if cigars>39:
        if cigars<61 or is_weekend:
            return True
    return False

cigar_party(2,False)