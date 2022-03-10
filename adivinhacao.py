print("********************************");
print("Seja bem-vindo ao jogo de Adivinhação");
print("********************************");

numero_secreto = 66;

chute_str = input("Digite um número: ");

print("Você digitou: ", chute_str);

chute = int(chute_str);

if(numero_secreto == chute):
    print("Parabens, você acertou o número!");
else:
    print("Você errou o número!");

print("Fim do Jogo");