soma = 0

while True: 
    num = int(input("Digite um número inteiro: "))
    
    if num < 0: 
        break 
        
    soma += num 
        
print("A soma dos números digitados é:", soma) 
