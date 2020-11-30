import argparse, math
parser = argparse.ArgumentParser()
parser.add_argument('--type', choices = ['annuity', 'diff'])
parser.add_argument('--principal', type=int)
parser.add_argument('--periods', type=int)
parser.add_argument('--interest', type=float)
parser.add_argument('--payment', type=int)
args = parser.parse_args()



try:
    p = args.principal
    n = args.periods
    a = args.payment
    i = args.interest / 1200
    if args.type == 'annuity':
        if p is None:
            if args.periods < 0:
                print('Incorrect parameters')
            elif args.payment < 0:
                print('Incorrect parameters')
            elif args.interest < 0:
                print('Incorrect parameters')
            else:
                prin = math.floor(a / ((i * (pow((1 + i), n))) / ((pow((1 + i), n)) - 1)))
                print('Your loan principal = ', prin ,'!')
                print('Overpayment= ', (a * n) - prin)
        elif n is None:
            if args.principal < 0:
                print('Incorrect parameters')
            elif args.payment < 0:
                print('Incorrect parameters')
            elif args.interest < 0:
                print('Incorrect parameters')
            else:
                period = math.ceil(math.log(a / (a - i * p), (1 + i)))
                print(f'It will take {period} months to repay this loan!' if period < 12 else f'It will take {period // 12} years to repay this loan!' if period % 12 == 0 else f'It will take {period // 12} years and {period % 12} months to repay this loan!')
                print('Overpayment= ', (a * period) - p)
        elif a is None:
            if args.principal < 0:
                print('Incorrect parameters')
            elif args.periods < 0:
                print('Incorrect parameters')
            elif args.interest < 0:
                print('Incorrect parameters')
            else:
                pay = math.ceil((p * (i * pow((1 + i),n)) / (pow((1 + i), n) - 1)))
                print('Your monthly payment = ', pay , '!')
                print('Overpayment= ', (pay * n) - p)

    elif args.type == 'diff':
        if args.principal < 0:
            print('Incorrect parameters')
        elif args.periods < 0:
            print('Incorrect parameters')
        elif args.interest < 0:
            print('Incorrect parameters')
        else:
            diff_total = 0
            p = int(args.principal)
            n = int(args.periods)
            for _ in range(n):
                m=_+1
                print(f'Month {m}: payment is ', math.ceil((p / n) + i * (p - (p * (m - 1) / n))))
                diff_total += math.ceil((p / n) + i * (p - (p * (m - 1) / n)))
            print('')
            print('Overpayment = ',diff_total - p)
    else:
        print('Incorrect parameters')
except TypeError:
    print('Incorrect parameters')
