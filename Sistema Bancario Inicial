menu = """

  SISTEMA BANCARIO

=====================
[d] Deposito
[s] Saque
[e] Extrato
[l] Log de erros
[q] Sair
=====================
              by jeds

=> """

saldo = float(0)
valor = float(0)
limite = float(500)
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
log_erros = ""
    
while True:
    
    opcao = input(menu)
    
    if opcao == "d":
        print("DEPOSITO")
        valor = input("Qual valor você deseja depositar?: "))
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito (+): R$ {valor:10.2f}\n"
            print(f"Você acabou de depositar R$ {valor:10.2f} no seu saldo.\n")
            
        else:
            print("Informe um valor válido!")
            log_erros += f"Informado um valor inválido para depósito. Valor: {valor:10.2f}\n"
            
     
    elif opcao == "s":
        print("SAQUE")
        valor = (input("Qual o valor que você deseja sacar?: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente!")
            log_erros += f"Operação falhou! Saldo insuficiente! Valor : {valor:10.2f}\n"
        
        elif excedeu_limite:
            print("Operação falhou! Valor do saque excede o limite!")
            log_erros += f"Operação falhou! Valor do saque excede o limite! Valor: {valor:10.2f}\n"
                    
        elif excedeu_saques:
            print("Operação falhou! Você excedeu o número de saques diários!")
            log_erros += f"Operação falhou! Você excedeu o número de saques! Quantidade: {numero_saques}\n"
                        
        elif valor > 0:
            saldo -= valor
            extrato +=f"Saque    (-): R$ {valor:10.2f}\n"
            print(f"Você acabou de sacar R$ {valor:10.2f} do seu saldo.\n")
            numero_saques += 1
        else:
            print("Operação falhou! O valor do saque deve ser maior que zero!")
            log_erros += f"Operação falhou! O valor do saque deve ser maior que zero! Valor: {valor:10.2f}\n"
            
        
    elif opcao == "e":
        print("\n================= EXTRATO =================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo Atual: R$ {saldo:10.2f}")
        print("============================================")   
        
    elif opcao == "l":
        print("\n============================= ERROS ==============================")
        print("Não foram registrados erros." if not log_erros else log_erros)
        print("=================================================================")
           
        
    elif opcao == "q":
        print("Saindo do sistema...")
        break
    
    else:
        print("Opção inválida. Tente novamente!")


