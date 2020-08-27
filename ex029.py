v = float(input('Qual a velocidade atual do carro? '))
multa = (v-80) * 7
if v > 80:
    print('\033[31mMULTADO! Você excedeu o limite permitido que é de 80Km/h\033[m')
    print('\033[31mDeverá pagar uma multa de \033[33mR${:.2f}\033[31m!'.format(multa))
print('\033[33mTenha um bom dia! Dirija com segurança!\033[m')
