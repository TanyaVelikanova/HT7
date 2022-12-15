def find_result(result, spisok):
    spisok_contact = []
    for i in range(0, len(spisok)):
        if result in spisok[i]:
            spisok_contact.append(spisok[i]) 
    return spisok_contact