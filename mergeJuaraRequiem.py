def sortPeserta(peserta):
    if len(peserta) <= 1:
        return peserta
    
    mid = len(peserta) // 2
    left_half = peserta[:mid]
    right_half = peserta[mid:]
    
    left_sorted = sortPeserta(left_half)
    right_sorted = sortPeserta(right_half)
    
    sorted_peserta = []
    i = j = 0
    
    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i]["total"] > right_sorted[j]["total"]:
            sorted_peserta.append(left_sorted[i])
            i += 1
            
        elif left_sorted[i]["total"] == right_sorted[j]["total"]:
            if left_sorted[i]["penonton"] >= right_sorted[j]["penonton"]:
                sorted_peserta.append(left_sorted[i])
                i += 1
            else:
                sorted_peserta.append(right_sorted[j])
                j += 1
    
        else:
            sorted_peserta.append(right_sorted[j])
            j += 1
            
    sorted_peserta.extend(left_sorted[i:])
    sorted_peserta.extend(right_sorted[j:])
    
    return sorted_peserta