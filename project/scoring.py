import pandas as pd
import argparse


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