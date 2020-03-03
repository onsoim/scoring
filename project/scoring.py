import pandas as pd
import numpy as np
import argparse

def _scoring(args): 
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


def scoring(args): 
    correct = pd.read_excel(args.correct, skiprows = 2).drop(columns = ['번호', '취약사유', '개선방안']).dropna(how = 'all', axis = 'rows').dropna(how='all', axis='columns').apply(lambda x: x.astype(str).str.lower())
    student = pd.read_excel(args.student, skiprows = 2).drop(columns = ['번호', '취약사유', '개선방안']).dropna(how = 'all', axis = 'rows').dropna(how='all', axis='columns').apply(lambda x: x.astype(str).str.lower())

    score = pd.concat([correct, student]).duplicated(keep=False)

    l_correct = len(correct)
    return {
        'stuid': int(args.student.split('_')[0]),
        'name': args.student.split('_')[1].split('.')[0],
        'grade': {
            'score': score[l_correct:].sum() * 10,
            'ans': [list(score[l_correct:])],
            'ans': [
                {
                    'result': score[l_correct:][i],
                    'code': student.loc[i].loc['항목코드'],
                    'url': student.loc[i].loc['경로'],
                    'value': student.loc[i].loc['변수명'],
                } for i in range(len(student))
            ],
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