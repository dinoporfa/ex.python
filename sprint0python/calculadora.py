from operacions import suma, resta, multi, divi

if __name__=="__main__":
    ope='si'
    while ope=='si':
        print('que operación a facer')
        ope = input()
        while ope not in ['suma', 'resta', 'multiplicación', 'división']:
            print('que operación a facer')
            ope = input()

        print('introduce o primeiro número')
        num1 = int(input())
        print('introduce o segundo número')
        num2 = int(input())

        if ope == 'división':
            print(divi(num1, num2))
        else:
            if ope == 'suma':
                print(suma(num1, num2))
            else:
                if ope == 'resta':
                    print(resta(num1, num2))
                else:
                    print(multi(num1, num2))
        print('facer outra operación?')
        ope = input()