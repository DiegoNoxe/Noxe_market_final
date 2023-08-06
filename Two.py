from time import sleep
import random
class Supermercado:
    def __init__(self):
        self.divida = 0
        self.deposito = 0
        self.banco  = 0
        self.gastos = 0
        self.comprador = 0
        self.compras_feitas = []
        self.produtos_disponiveis = {
            1: {'produto': 'Coca-cola 2L'     , 'preco': 7},
            2: {'produto': 'Guaravita 150ml'    , 'preco': 1},
            3: {'produto': 'Caderno grande'    , 'preco': 3},
            4: {'produto': 'Caneta bic azul'   , 'preco': 1},
            5: {'produto': 'Fanta uva 2L'      , 'preco': 6},
            6: {'produto': 'Carregador xiaomi' , 'preco': 15},
            7: {'produto': 'Carregador apple'  , 'preco': 30},
            8: {'produto': 'Mouse', 'preco': 9},
            9: {'produto': 'Fone de ouvido com fio' , 'preco': 13},
            10:{'produto': 'Tapete verde', 'preco': 10},}
        self.dialogos = {"Funcionario: "}
    def dialogo_boas_vindas(self):
        dialogo = ['Atendente: Seja bem vindo a loja noxe!', 'Atendente: Opa, boas compras!'
                   ,'Atendente: Tenha um bom dia!','Atendente: Deseja de alguma ajuda?']
        dia_al  = random.choice(dialogo)
        print('\033[1;31m' + dia_al)
    def dialogo_despedida(self):
        print()
        despedi = ['Até a proxima!','Volte sempre!','Tenha uma otima semana']
        despedida = random.choice(despedi)
        print('\033[1;31m' + despedida)
    def dialogo_compras(self):
        print()
    def comentaris_banco(self):
        bank = ['Bem vindo ao banco Exon!', 'Faça seu emprestimo!', 'Emprestimo rápido e facil']
        banco = random.choice(bank)
        print('\033[1;31m' + banco)
    def escolhendo(self):
        self.news()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        merq = int(input('''\033[1;36mEscolha uma das opções abaixo: 
(1) Verificar produtos
(2) Verificar saldo atual
(3) Ir ao banco
(4) Sair do mercado
(5) Verificar Compras feitas
R: '''))
        #Compras
        if merq == 1:
            print()
            print('\033[1;30mProdutos disponiveis: ')
            for num, produto in self.produtos_disponiveis.items():
                produtes = produto['produto']
                print(f'\033[1;31mCodigo:{num} | \033[1;34mNome: {produtes}')
            print('\033[m')
            comprar = str(input('\033[1;30mDeseja comprar algum produto: S/N')).upper()
            if comprar == 'S':
                print('Ok!')
                sleep(1)
                print('Iremos verificar o preço')
                sleep(2)
                for num, produto in self.produtos_disponiveis.items():
                    produtes = produto['produto']
                    preco = produto['preco']
                    print(f'\033[1;31mCodigo:{num} | \033[1;34mNome: {produtes} | \033[1;30mpreço: {preco}')
                    print()
                comprar_pro = int(input('Selecione o codigo do produto para compra-lo'))
                if comprar_pro in self.produtos_disponiveis:
                    compras = self.produtos_disponiveis[comprar_pro]
                    preco   = compras['preco']
                    produto = compras['produto']
                    if self.comprador >= preco:
                     print(f'\033[1;35mVocê acabou de comprar o produto "{produto}" por {preco}R$!')
                     self.comprador-= preco
                     self.gastos += preco
                     print()
                     print()
                     sleep(2)
                     print(f'Saldo atual: {self.comprador}')
                     sleep(1)
                     self.compras_feitas.append(produto)
                     print(f'\033[1;36mProdutos comprados até agora:')
                     for produto in self.compras_feitas:
                            print(f'- {produto}')
                else:
                    print('Saldo invalido?')






            else:
                print('Você não tem saldo para esse produto!')
                sleep(3)
                return self.escolhendo()
        #Verificar saldo atual
        if merq == 2:
            print()
            print('\033[1;31m*'*25)
            print(f'\033[1;31mSeu saldo atual é:{self.comprador}')
            print('\033[1;31m*' * 25)
            return False

        #bano comenario
        if merq == 3:
            print()
            noxe = int(input('''Seja bem-vindo ao banco Exon! O que deseja?
            (1) Emprestimo
            (2) Consulta dividas
            (3) Depositar dinheiro
            (4) Sacar dinheiro
            (5) Sair do banco'''))

            if noxe == 1:
                self.comentaris_banco()
                print()
                print()
                emprestimo = int(input('Gerente: Qual é o valor do emprestimo que você deseja? '))
                print('Ok, iremos verificar se o senhor está apto para receber! Aguarde um momento')
                sleep(3)
                if self.divida > 10:
                    print(f'Olá, {self.nome} você tem uma divida muito alta! EMPRESTIMO NEGADO!')
                    print()
                    return self.escolhendo()
                elif self.idade < 18:
                    print(f'{self.nome} você não tem idade para pegar emprestimo! EMPRESTIMO NEGADO!')
                    sleep(2)
                    return self.escolhendo()
                elif emprestimo > 35 and self.comprador < 5:
                    print('Atendente: Você tem muito pouco é o valor que você deseja é muito alto! Emprestimo negado')
                    sleep(2)
                    return self.escolhendo()
                elif emprestimo < 10 and self.comprador > 100:
                    print('Atendente: Você já tem uma boa quantia! Não há necessidade de emprestimo!')
                    sleep(2)
                    return self.escolhendo()
                elif emprestimo < 20 and self.comprador > 5:
                    print('Emprestimo concedido!')
                    self.comprador+= emprestimo
                    self.divida += emprestimo
                    sleep(2)
                    return self.escolhendo()
                else:
                    print('Emprestimo concedido!')
                    self.comprador += emprestimo
                    self.divida += emprestimo
                    sleep(2)
                    return self.escolhendo()
            elif noxe == 2:
                print()
                print()
                print('O senhor tem uma divida de: ', self.divida)
                sleep(2)
                return self.escolhendo()

            elif noxe == 3:
                print('Quanto deseja deposita?')
                deposito = int(input('R: '))
                if deposito > self.comprador:
                    print('Você não tem saldo para depositar esse valor!')
                    return False

                else:
                    self.deposito += deposito
                    self.comprador -= deposito
                    print(f'Saldo guardado:{self.deposito}')
                    print(f'Saldo para gastos:{self.comprador}')
            elif noxe == 4:
                print('Escolha o valor que desejar sacar')
                print('Saldo disponivel para saque: ', self.deposito)
                sacar = int(input('R: '))
                if sacar > self.deposito:
                    print('Valor mais alto do que você tem depositado!')
                    return False
                else:
                    self.deposito-= sacar
                    self.comprador+= sacar




            if noxe == 5:
                return self.escolhendo()
        #Opção sair mercado
        if merq == 4:
            print()
            print('\033[1;34mTem certeza que deseja sair do mercado?')
            ctz = str(input('S/N')).upper()
            if ctz == 'S':
                print()
                print('\033[1;31mOk,saindo do mercado!')
                print('Abaixo estão as suas estastisticas:')
                print()
                print('Produtos comprados:')
                for produtos in self.compras_feitas:
                    print(f'\n{produtos}')
                print(f'Dinheiro gasto: {self.gastos}')
                print(f'Valor pego no banco: {self.banco}')
                print()
                print()
                self.dialogo_despedida()
                exit()
        elif merq == 5:
            print()
            print()
            print('Compras feitas  até o momento:')
            if self.gastos > 1:
                print('\033[1;31mCompras feitas até o momento')
                for compras in self.compras_feitas:
                    print(compras)
            else:
                print('\033[1;31mVocê ainda não fez nenhuma compra!')
                sleep(4)
                self.escolhendo()


        else:
            return False
    def titulo(self):
        print()
        print('                                     \033[4;30mMercado Noxe')
        sleep(1.7)
        print('\033[9;30mPromoção boa é aqui!\033[m')
        print()
    def news(self):
        print()
        news_noxe = ['Mercado noxe em alta!','Crise no mercado noxe!', 'Mercado noxe mais barato',
                     'Mercado noxe tem concorrencia nova!', 'Preço da coca-cola cai!', 'Coca-cola tem nova alta',
                     'No momento está fazendo 25 Graus!', 'Banco Exon tem altas nas ações!','Acidente no mercado noxe']
        news_news = random.choice(news_noxe)
        print('\033[1;33m*' * 30)
        print(f'''\033[1;34mNoticia do dia:              
{news_news}''')
        print('\033[1;33m*'*  30)
        print('\033[m')
    def configuracao(self):
     try:
        self.nome = str(input('\033[1;35mQual é o seu nome: '))
        self.dinheiro = int(input('\033[1;34mCom quanto deseja iniciar $? '))
        self.comprador+= self.dinheiro
        self.cidade = str(input('\033[1;31mCidade: '))
        self.idade  = int(input('\033[1;32mIdade: '))
        print('\033[1;30mEstamos analisando as informações...')
        sleep(1.7)
        print('Aguarde!')
        sleep(2)
     except ValueError:
        print('Opção incorreta!!')
        print('Refaça novamente em 3s!')
        sleep(3)
        return self.configuracao()
     print('Ok!')
market = Supermercado()
market.titulo()
market.configuracao()
market.titulo()
market.dialogo_boas_vindas()
while True:
 market.escolhendo()

