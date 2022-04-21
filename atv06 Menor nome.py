import string
import sys
import unicodedata

def menor_nome(names_array):
    if len(names_array) > 0:
        sizes = []
        corrected_names = []
        minimum = sys.maxsize
        index = 0

        for name in names_array:
            raw = name.replace(" ", "")
            corrected_names.append(raw)

        for name in corrected_names:
            raw = unicodedata.normalize("NFKD", name).encode("ASCII", "ignore")
            str_raw = raw.decode("ASCII")
            print(str_raw)
            sizes.append(len(str_raw))

        for i, value in enumerate(sizes):
            if value < minimum:
                minimum = value
                index = i
        return corrected_names[index].capitalize()
    else:
        return ""
