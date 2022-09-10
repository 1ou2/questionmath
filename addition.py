import random
import argparse
import time

def getop():
    vals = [1,2,3,4,6,7,8,9]
    table = [6,7,8,9]
    op1 = random.choice(vals)
    op2 = random.choice(table)
    return op1,op2

CHALLENGE_TIME = 60

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ton entraîneur aux calculs")
    parser.add_argument("-c","--challenge",action='store_true',help="tu as une minute pour faire le maximum de calcul")
    args = parser.parse_args()
    stats = {}
    stats["total"] = 0
    stats["correct"] = 0
    if args.challenge:
        tstart = time.time()

    while True:
        op1,op2 = getop()
        if args.challenge:
            tnow = time.time()
            if tnow - tstart > CHALLENGE_TIME:
                print("C’est fini")
                break
        print(f"{op1} + {op2} = ",end='')
        proposition = input()
        stats["total"] = stats["total"] +1
        if proposition.isnumeric():
            val = int(proposition)
            if op1 + op2 == val:
                print("OK")
                stats["correct"] = stats["correct"] +1
            else:
                print("Erreur")
        else:
            if args.challenge:
                print("Erreur")
            # exit program if a non numeric value is provided
            else:
                # do not count last question as we are exiting
                stats["total"] = stats["total"] -1
                break

    print(f"Résultats : {stats['correct']} / {stats['total']}")
    