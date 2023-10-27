from group_divider import group_divider

file1 = 'test_classe.csv'
file2 = 'test_1.csv'
file3 = 'test_2.csv'

# Crezione della classe e setup con il file
grd = group_divider()
grd.carica_csv(file1)
#grd.carica_csv(file2)
#grd.carica_csv(file3)
grd.stampa_matrice()

# Calcolo della media dei due gruppi
a, b, med = grd.dividi_in_due_gruppi_media()
if [a,b,med]:
    print("\nI gruppi:\n",a," e ", b, "\nCon una media di ", med)
else:
    print("Il file non è stato caricato correttamente")