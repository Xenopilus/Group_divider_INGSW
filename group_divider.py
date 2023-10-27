from abc import ABC
import pandas as pd
from itertools import combinations


'''
Classe che una volta caricato un CSV mette a disposizione dei metodi per la divisione in gruppi
'''
class group_divider(ABC):
    
    __partecipanti = [] # conterrà tutti i partecipanti
    __matrice = [] # contiene la matrice
    
    '''
    Carica il file CSV per l'utilizzo nella classe, modificando lo stato interno
    
    @param file -> path del file da aprire
    @modify partecipanti e matrice, definendo i loro valori in base al file caricato
    '''
    def carica_csv(self, file):
        df = pd.read_csv(file,index_col=0)
        self.__partecipanti = list(df.columns)
        self.__matrice = df
    
    
    '''
    Stampa la matrice
    '''
    def stampa_matrice(self):
        print(self.__matrice)


    '''
    Genera le combinazioni e ricerca in brute-force la combinazione che ha la media più alta.
    
    @return team_a
    @return team_b
    @return media_migliore -> la media più alta trovata
    '''
    def dividi_in_due_gruppi_media(self):
        if(self.__partecipanti): # Truth value testing
            combinazioni = self.__gen_combinazioni(int(len(self.__partecipanti)/2))

            # calcola i due valori
            media_migliore = 0
            team_a = []
            team_b = []
            for a in combinazioni:
                punteggio_a = self.__punti_gruppo(a)
                b = [x for x in self.__partecipanti if x not in a]
                punteggio_b = self.__punti_gruppo(b)
                
                
                med_a = punteggio_a / len(a)
                med_b = punteggio_b / len(b)
                
                media = (med_a + med_b) / 2
                
                if media > media_migliore:
                    media_migliore = media
                    team_a = a
                    team_b = b
            
            return team_a, team_b, media_migliore
            
        else:
            print("Inserire csv prima di eseguire le funzioni")
            return None, None, None
    
    
    '''
    Genera tutte le combinazioni di gruppi possibili di N partecipanti e li ritorna come una lista.
    
    @param num_membrs -> numero di persone per gruppo
    @return lista -> una lista di liste, dove le liste interne rappresentano i gruppi
    '''
    def __gen_combinazioni(self,num_mebers) -> list:
        return [list(c) for c in combinations(self.__partecipanti,num_mebers)]
    
    
    '''
    Somma tutte le celle della matrice generata dai partecipanti del gruppo e ne ritorna il risultato. Non modifica lo stato interno
    
    @param gruppo -> lista dei partecipanti che formano un gruppo
    @return sum -> somma dei valori della matrice
    '''
    def __punti_gruppo(self,gruppo) -> int:
        # creazione della matrice
        offerte = self.__matrice.loc[gruppo]
        offerte_gruppo = offerte[gruppo]

        sum = 0
        for i in range(len(offerte_gruppo.axes[1])):
            for j in range(len(offerte_gruppo.axes[1])):
                tmp = offerte_gruppo.iloc[i,j]
                if isinstance(tmp, str) and tmp.isnumeric(): # in pandas NaN = float
                    sum = sum + int(tmp)
        return sum