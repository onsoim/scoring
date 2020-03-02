import pandas as pd
import numpy as np
import argparse


def scoring(args): 
    correct = pd.read_excel(args.correct, skiprows = 2).drop(columns = ['번호', '취약사유', '개선방안']).dropna(how = 'all', axis = 'rows').dropna(how='all', axis='columns')
    student = pd.read_excel(args.student, skiprows = 2).drop(columns = ['번호', '취약사유', '개선방안']).dropna(how = 'all', axis = 'rows').dropna(how='all', axis='columns')
    # correct = pd.read_csv(args.correct)
    # student = pd.read_csv(args.student).drop_duplicates()

    score = pd.concat([correct, student]).duplicated(keep=False)

    # true positive == correct && student
    tp = pd.DataFrame(columns = ['source ip', 'destination ip', 'source port', 'destination port', 'attack type'])

    # false positive == !correct && student
    fp = pd.DataFrame(columns = ['source ip', 'destination ip', 'source port', 'destination port', 'attack type'])

    # false negative == correct && !student
    fn = pd.DataFrame(columns = ['source ip', 'destination ip', 'source port', 'destination port', 'attack type'])

    l_correct = len(correct)
    # for i in range(l_correct):
    #     if score[:l_correct][i]: tp = tp.append(correct.loc[i], ignore_index=True)
    #     else: fn = fn.append(correct.loc[i], ignore_index=True)

    # for i in range(len(student)):
    #     if not score[l_correct:][i]:
    #         fp = fp.append(student.loc[i], ignore_index=True)
    return {
        'id': int(args.student.split('_')[0]),
        'name': args.student.split('_')[1].split('.')[0],
        'grade': {
            'score': 50,
            'list': list(score[l_correct:]),
        },
    }
    

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(dest="correct", help="Correct answer sheet")
    parser.add_argument(dest="student", help='Student answer sheet')
    args = parser.parse_args()

    print(scoring(args))


if __name__ == "__main__":
    main()