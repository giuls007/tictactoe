import random
def verifica_vittoria(tabellone: list[list[str]]) -> bool:
    for riga in tabellone:
        if riga[0] == riga[1] == riga[2] != " ":
            return True
    for colonna in range(3):
        if tabellone[0][colonna] == tabellone[1][colonna] == tabellone[2][colonna] != " ":
            return True
    if tabellone[0][0] == tabellone[1][1] == tabellone[2][2] != " ":
        return True
    if tabellone[0][2] == tabellone[1][1] == tabellone[2][0] != " ":
        return True
    return False

def mostra_tabellone(tabellone: list[list[str]]) -> None:
    for i, riga in enumerate(tabellone):
        print(" | ".join(riga))
        if i < 2:
            print("-" * 9)
def inizializza_tabellone() -> list[list[str]]:
    return [[" " for _ in range(3)] for _ in range(3)]
def aggiorna_punteggio(giocatori: dict, simbolo: str) -> None:
    if simbolo == 'X':
        giocatori['X']['punteggio'] += 1
    elif simbolo == 'O':
        giocatori['O']['punteggio'] += 1
def mossa_bot(tabellone: list[list[str]]) -> tuple[int, int]:
    mosse_possibili = [(riga, colonna) for riga in range(3) for colonna in range(3) if tabellone[riga][colonna] == " "]
    for riga, colonna in mosse_possibili:
        tabellone[riga][colonna] = 'O'
        if verifica_vittoria(tabellone):
            tabellone[riga][colonna] = " "
            return riga, colonna
        tabellone[riga][colonna] = " "
    return random.choice(mosse_possibili)
def gioca_turno(tabellone: list[list[str]], giocatore: dict, is_bot: bool) -> None:
    if is_bot:
        print(f"Turno del bot ({giocatore['nome']})")
        riga, colonna = mossa_bot(tabellone)
    else:
        while True:
            try:
                riga = int(input(f"{giocatore['nome']}, inserisci il numero della riga (1-3): ")) - 1
                colonna = int(input(f"{giocatore['nome']}, inserisci il numero della colonna (1-3): ")) - 1
                if riga < 0 or riga > 2 or colonna < 0 or colonna > 2:
                    print("Posizione non valida, riprova!")
                elif tabellone[riga][colonna] != " ":
                    print("Quella cella è già occupata, riprova!")
                else:
                    break
            except ValueError:
                print("Per favore, inserisci un numero valido.")
    tabellone[riga][colonna] = giocatore['simbolo']
def partita(giocatori: dict) -> None:
    tabellone = inizializza_tabellone()
    turno = 0
    while True:
        giocatore = giocatori['X'] if turno % 2 == 0 else giocatori['O']
        is_bot = giocatore['nome'] == 'Bot'
        mostra_tabellone(tabellone)
        gioca_turno(tabellone, giocatore, is_bot)

        if verifica_vittoria(tabellone):
            mostra_tabellone(tabellone)
            print(f"{giocatore['nome']} ha vinto questo turno!")
            aggiorna_punteggio(giocatori, giocatore['simbolo'])
            break

        if all(tabellone[i][j] != " " for i in range(3) for j in range(3)):
            mostra_tabellone(tabellone)
            print("La partita è finita in pareggio!")
            break

        turno += 1
def main() -> None:
    nome_1 = input("Nome del giocatore (X): ")
    giocatori = {
        'X': {'nome': nome_1, 'simbolo': 'X', 'punteggio': 0},
        'O': {'nome': 'Bot', 'simbolo': 'O', 'punteggio': 0}
    }

    while giocatori['X']['punteggio'] < 2 and giocatori['O']['punteggio'] < 2:
        print(f"\nPartita {giocatori['X']['punteggio']} - {giocatori['O']['punteggio']}")
        partita(giocatori)

    if giocatori['X']['punteggio'] == 2:
        print(f"\n{giocatori['X']['nome']} ha vinto la sfida al meglio dei tre!")
    else:
        print(f"\n{giocatori['O']['nome']} ha vinto la sfida al meglio dei tre!")

if __name__ == "__main__":
    main()
