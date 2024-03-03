def newton_raphson(f, derivF, x0, t, max=100):
  """
  EXPLICAÇÃO: 
  1. Função aplica o método, encontrando raízes de uma função.
  2. Usa a reta tangente à função em um ponto próximo à raiz 
  para estimar a próxima aproximação da raiz.
  3. Fórmula: x1 = x - f(x) / f'(x)
  4. Retorno do código: A raiz da função f.

  f(f(x)): Função para usar no método.
  derivF (f'(x)): Derivada da função f.
  x0 (x): Chute inicial para a raiz.
  t: Tolerância para erro
  max: Número máximo de iterações.

  """

  valX = [x0] #Valores de x

  for i in range(max):
    x1 = x0 - f(x0) / derivF(x0) #fórmula  
    if abs(x1 - x0) < t: # Verificação da convergência
      return x1
    x0 = x1 #atualizando x0 para novo teste
    valX.append(x1)

  raise RuntimeError("O método ultrapassou {} iterações.".format(max))
