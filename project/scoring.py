import pandas as pd
import argparse


def scoring(args): 
    # correct = pd.read_excel(args.correct)
    # answer = pd.read_excel(args.answer).drop_duplicates()
    correct = pd.read_csv(args.correct)
    answer = pd.read_csv(args.answer).drop_duplicates()

    wrong = pd.concat([correct, answer])
    print(wrong.duplicated())
    # right = 


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(dest="correct", help="Correct answer sheet")
    parser.add_argument(dest="answer", help='User answer sheet')
    args = parser.parse_args()

    scoring(args)


if __name__ == "__main__":
    main()