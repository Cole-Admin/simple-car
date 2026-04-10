
def prosecna_potrosnja(cena_koju_sam_ulozio, cena_po_litri):
    # === PROBA ===
    return float(cena_koju_sam_ulozio) / cena_po_litri

def racunanje_registracije(snaga_motora):
    if snaga_motora < 100:
        return f" 150 EUR " 
    elif snaga_motora <= 175:
        return f" 250 EUR " 
    elif snaga_motora <= 250:
        return f" 300 EUR " 
    elif snaga_motora <= 425:
        return f" 500 EUR "
    elif snaga_motora <= 700:
        return f" 1200 EUR "
    elif snaga_motora <= 250:
        return f" 2000 EUR "



    