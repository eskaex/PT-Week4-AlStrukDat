def sortPeserta(peserta):
    if len(peserta) <= 1:
        return peserta
    
    pivot = peserta[0]
    kiri = []
    kanan = []
    
    for p in peserta[1:]:
        if p["total"] > pivot["total"]:
            kiri.append(p)
            
        elif p["total"] == pivot["total"] and p["penonton"] > pivot["penonton"]:
            kiri.append(p)
    
        else:
            kanan.append(p)
            
    return sortPeserta(kiri) + [pivot] + sortPeserta(kanan)