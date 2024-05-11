# Function to convert ECO codes
def simplify_eco(eco):
    if eco.startswith('A') and 2 <= int(eco[1:]) <= 3:
        return 'A02'
    if eco.startswith('A') and 4 <= int(eco[1:]) <= 9:
        return 'A04'
    if eco.startswith('A') and 10 <= int(eco[1:]) <= 39:
        return 'A10'
    if eco.startswith('A') and 40 <= int(eco[1:]) <= 41:
        return 'A40'
    if eco.startswith('A') and 43 <= int(eco[1:]) <= 44:
        return 'A43'
    if eco.startswith('A') and 45 <= int(eco[1:]) <= 46:
        return 'A45'
    if eco.startswith('A') and 48 <= int(eco[1:]) <= 49:
        return 'A48'
    if eco.startswith('A') and 51 <= int(eco[1:]) <= 52:
        return 'A51'
    if eco.startswith('A') and 53 <= int(eco[1:]) <= 55:
        return 'A53'
    if eco.startswith('A') and 57 <= int(eco[1:]) <= 59:
        return 'A57'
    if eco.startswith('A') and 60 <= int(eco[1:]) <= 79:
        return 'A60'
    if eco.startswith('A') and 80 <= int(eco[1:]) <= 99:
        return 'A80'
        
    if eco.startswith('B') and 2 <= int(eco[1:]) <= 5:
        return 'B02'
    if eco.startswith('B') and 7 <= int(eco[1:]) <= 9:
        return 'B07'
    if eco.startswith('B') and 10 <= int(eco[1:]) <= 19:
        return 'B10'
    if eco.startswith('B') and 20 <= int(eco[1:]) <= 99:
        return 'B20'
        
    if eco.startswith('C') and 00 <= int(eco[1:]) <= 19:
        return 'C00'
    if eco.startswith('C') and 21 <= int(eco[1:]) <= 22:
        return 'C21'
    if eco.startswith('C') and 23 <= int(eco[1:]) <= 24:
        return 'C23'
    if eco.startswith('C') and 25 <= int(eco[1:]) <= 29:
        return 'C25'
    if eco.startswith('C') and 30 <= int(eco[1:]) <= 39:
        return 'C30'
    if eco.startswith('C') and 42 <= int(eco[1:]) <= 43:
        return 'C42'
    if eco.startswith('C') and 47 <= int(eco[1:]) <= 49:
        return 'C47'
    if eco.startswith('C') and 51 <= int(eco[1:]) <= 52:
        return 'C51'
    if eco.startswith('C') and 53 <= int(eco[1:]) <= 54:
        return 'C53'
    if eco.startswith('C') and 55 <= int(eco[1:]) <= 59:
        return 'C55'
    if eco.startswith('C') and 60 <= int(eco[1:]) <= 99:
        return 'C60'
        
    if eco.startswith('D') and 4 <= int(eco[1:]) <= 5:
        return 'D04'
    if eco.startswith('D') and 7 <= int(eco[1:]) <= 9:
        return 'D07'
    if eco.startswith('D') and 10 <= int(eco[1:]) <= 15:
        return 'D10'
    if eco.startswith('D') and 17 <= int(eco[1:]) <= 19:
        return 'D17'
    if eco.startswith('D') and 20 <= int(eco[1:]) <= 29:
        return 'D20'
    if eco.startswith('D') and 30 <= int(eco[1:]) <= 42:
        return 'D30'
    if eco.startswith('D') and 43 <= int(eco[1:]) <= 49:
        return 'D43'
    if eco.startswith('D') and 50 <= int(eco[1:]) <= 69:
        return 'D50'
    if eco.startswith('D') and 70 <= int(eco[1:]) <= 79:
        return 'D70'
    if eco.startswith('D') and 80 <= int(eco[1:]) <= 99:
        return 'D80'
        
    if eco.startswith('E') and 1 <= int(eco[1:]) <= 9:
        return 'E01'
    if eco.startswith('E') and 12 <= int(eco[1:]) <= 19:
        return 'E12'
    if eco.startswith('E') and 20 <= int(eco[1:]) <= 59:
        return 'E20'
    if eco.startswith('E') and 60 <= int(eco[1:]) <= 99:
        return 'E60'
    return eco

def eco_decode(eco):
    if eco == 'A00': return "Polish (Sokolsky) opening"
    if eco == 'A01': return "Nimzovich-Larsen attack"
    if eco == 'A02': return "Bird's opening"
    if eco == 'A04': return "Reti opening"
    if eco == 'A10': return "English opening"
    if eco == 'A40': return "Queen's pawn"
    if eco == 'A42': return "Modern defence, Averbakh system"
    if eco == 'A43': return "Old Benoni defence"
    if eco == 'A45': return "Queen's pawn game"
    if eco == 'A47': return "Queen's Indian defence"
    if eco == 'A48': return "King's Indian, East Indian defence"
    if eco == 'A50': return "Queen's pawn game"
    if eco == 'A51': return "Budapest defence"
    if eco == 'A53': return "Old Indian defence"
    if eco == 'A56': return "Benoni defence"
    if eco == 'A57': return "Benko gambit"
    if eco == 'A60': return "Benoni defence"
    if eco == 'A80': return "Dutch"

    if eco == 'B00': return "King's pawn opening"
    if eco == 'B01': return "Scandinavian (centre counter) defence"
    if eco == 'B02': return "Alekhine's defence"
    if eco == 'B06': return "Robatsch (modern) defence"
    if eco == 'B07': return "Pirc defence"
    if eco == 'B10': return "Caro-Kann defence"
    if eco == 'B20': return "Sicilian defence"
        
    if eco == 'C00': return "French defence"
    if eco == 'C20': return "King's pawn game"
    if eco == 'C21': return "Centre game"
    if eco == 'C23': return "Bishop's opening"
    if eco == 'C25': return "Vienna game"
    if eco == 'C30': return "King's gambit"
    if eco == 'C40': return "King's knight opening"
    if eco == 'C41': return "Philidor's defence"
    if eco == 'C42': return "Petrov's defence"
    if eco == 'C44': return "King's pawn game"
    if eco == 'C45': return "Scotch game"
    if eco == 'C46': return "Three knights game"
    if eco == 'C47': return "Four knights, Scotch variation"
    if eco == 'C50': return "Italian Game"
    if eco == 'C51': return "Evans gambit"
    if eco == 'C53': return "Giuoco Piano"
    if eco == 'C55': return "Two knights defence"
    if eco == 'C60': return "Ruy Lopez (Spanish opening)"

    if eco == 'D00': return "Queen's pawn game"
    if eco == 'D01': return "Richter-Veresov attack"
    if eco == 'D02': return "Queen's pawn game"
    if eco == 'D03': return "Torre attack (Tartakower variation)"
    if eco == 'D04': return "Queen's pawn game"
    if eco == 'D06': return "Queen's Gambit"
    if eco == 'D07': return "Queen's Gambit Declined, Chigorin defence"
    if eco == 'D10': return "Queen's Gambit Declined Slav defence"
    if eco == 'D16': return "Queen's Gambit Declined Slav accepted, Alapin variation"
    if eco == 'D17': return "Queen's Gambit Declined Slav, Czech defence"
    if eco == 'D20': return "Queen's gambit accepted"
    if eco == 'D30': return "Queen's gambit declined"
    if eco == 'D43': return "Queen's Gambit Declined semi-Slav"
    if eco == 'D50': return "Queen's Gambit Declined"
    if eco == 'D70': return "Neo-Gruenfeld defence"
    if eco == 'D80': return "Gruenfeld defence"

    if eco == 'E00': return "Queen's pawn game"
    if eco == 'E01': return "Catalan, closed"
    if eco == 'E10': return "Queen's pawn game"
    if eco == 'E11': return "Bogo-Indian defence"
    if eco == 'E12': return "Queen's Indian defence"
    if eco == 'E20': return "Nimzo-Indian defence"
    if eco == 'E60': return "King's Indian defence"

    return eco

        