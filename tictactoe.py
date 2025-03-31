def inizializza_tabellone() -> list[list[str]]:
    return [[" " for _ in range(3)] for _ in range(3)]


def mostra_tabellone(tabellone: list[list[str]]) -> None:
    print("-------------")
    for riga in tabellone:
        print("|", " | ".join(riga), "|")
        print("-------------")


def gioca_turno(tabellone: list[list[str]], giocatore: dict) -> None:
    while True:
        try:
            riga = int(input(f"{giocatore['nome']}, inserisci il numero della riga (1-3): ")) - 1
            colonna = int(input(f"{giocatore['nome']}, inserisci il numero della colonna (1-3): ")) - 1
            if riga < 0 or riga > 2 or colonna < 0 or colonna > 2:
                print("Posizione non valida, riprova!")
            elif tabellone[riga][colonna] != " ":
                print("Quella cella è già occupata, riprova!")
            else:
                tabellone[riga][colonna] = giocatore['simbolo']
                break
        except ValueError:
            print("Per favore, inserisci un numero valido.")


def verifica_vittoria(tabellone: list[list[str]]) -> bool:
    for i in range(3):
        if tabellone[i][0] == tabellone[i][1] == tabellone[i][2] != " ":
            return True
        if tabellone[0][i] == tabellone[1][i] == tabellone[2][i] != " ":
            return True

    # Diagonali
    if tabellone[0][0] == tabellone[1][1] == tabellone[2][2] != " ":
        return True
    if tabellone[0][2] == tabellone[1][1] == tabellone[2][0] != " ":
        return True

    return False


def aggiorna_punteggio(giocatori: dict, vincitore: str) -> None:
    giocatori[vincitore]['punteggio'] += 1


def partita(giocatori: dict) -> None:
    tabellone = inizializza_tabellone()
    turno = 0
    while True:
        giocatore = giocatori['X'] if turno % 2 == 0 else giocatori['O']
        mostra_tabellone(tabellone)
        gioca_turno(tabellone, giocatore)

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
    # Inizializza i giocatori
    nome_1 = input("Nome del primo giocatore (X): ")
    nome_2 = input("Nome del secondo giocatore (O): ")

    giocatori = {
        'X': {'nome': nome_1, 'simbolo': 'X', 'punteggio': 0},
        'O': {'nome': nome_2, 'simbolo': 'O', 'punteggio': 0}
    }

    while giocatori['X']['punteggio'] < 2 and giocatori['O']['punteggio'] < 2:
        print(f"\n Partita {giocatori['X']['punteggio']} - {giocatori['O']['punteggio']} ")
        partita(giocatori)

    if giocatori['X']['punteggio'] == 2:
        print(f"\n{giocatori['X']['nome']} ha vinto la sfida al meglio dei tre!")
    else:
        print(f"\n{giocatori['O']['nome']} ha vinto la sfida al meglio dei tre!")


if __name__ == "__main__":
    main()
