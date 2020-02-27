import pandas as pd
import numpy as np
import argparse


def scoring(args): 
    # correct = pd.read_excel(args.correct)
    # answer = pd.read_excel(args.answer).drop_duplicates()
    correct = pd.read_csv(args.correct)
    answer = pd.read_csv(args.answer).drop_duplicates()
    l_correct, l_answer = len(correct), len(answer)

    score = pd.concat([correct, answer]).duplicated(keep=False)

    # true positive == correct && answer
    tp = pd.DataFrame(columns = ['source ip', 'destination ip', 'source port', 'destination port', 'attack type'])

    # false positive == !correct && answer
    fp = pd.DataFrame(columns = ['source ip', 'destination ip', 'source port', 'destination port', 'attack type'])

    # false negative == correct && !answer
    fn = pd.DataFrame(columns = ['source ip', 'destination ip', 'source port', 'destination port', 'attack type'])

    for i in range(l_correct):
        if score[:l_correct][i]: tp = tp.append(correct.loc[i], ignore_index=True)
        else: fn = fn.append(correct.loc[i], ignore_index=True)

    # for i in range(l_answer):
    #     if not score[l_correct:][i]:
    #         fp = fp.append(answer.loc[i], ignore_index=True)

    return {'correct': len(tp), 'wrong': len(fn)}
    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(dest="correct", help="Correct answer sheet")
    parser.add_argument(dest="answer", help='User answer sheet')
    args = parser.parse_args()

    print(scoring(args))


if __name__ == "__main__":
    main()