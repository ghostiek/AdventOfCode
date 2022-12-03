def split_mid(txt):
    return txt[:int(len(txt)/2)], txt[int(len(txt)/2):]


def find_dupe(fh, sh):
    # we know there's only going to be 1
    return list(set(fh) & set(sh))[0]


def find_dupe2(comp1, comp2, comp3):
    # we know there's only going to be 1
    return list(set(comp1) & set(comp2) & set(comp3))[0]


def get_score(same_char):
    return ord(same_char) - 38 if same_char.isupper() else ord(same_char) - 96
