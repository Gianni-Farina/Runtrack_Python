def arrondir_notes(notas):
    notes_arrondies = []

    for note in notas:
        if note < 40:
            notes_arrondies.append(note)
        else:
            prochain_multiple_de_5 = ((note // 5) + 1) * 5
            if prochain_multiple_de_5 - note < 3:
                notes_arrondies.append(prochain_multiple_de_5)
            else:
                notes_arrondies.append(note)

    return notes_arrondies

while True:
    notes = input("Veuillez entrer les notes: ")
    if ',' in notes:
        break
    else:
        print("Veuillez entrer les notes séparées par des virgules.")

notes_list = [int(note.strip()) for note in notes.split(',')]
notes_modifiees = arrondir_notes(notes_list)

print("Notes arrondies :", notes_modifiees)