# MetodoNewtonRaphson_Python

Trabalho da matéria de Cálculo numérico

  EXPLICANDO MÉTODO NEWTON RAPHSON:
  -> O método de Newton-Raphson se baseia na ideia de usar a reta tangente à função em um ponto próximo à raiz para estimar a próxima aproximação da raiz.

  COMO CÁLCULAR? 
  1- Escolha um chute inicial: Escolha um valor inicial x_0 para a raiz. Este valor pode ser qualquer valor, mas quanto mais próximo da raiz real, mais rápido o método convergirá.
  2- Calcule a próxima aproximação: Utilize a fórmula acima para calcular a próxima aproximação da raiz, x_1.
  3- Repita os passos 1 e 2: Continue calculando as próximas aproximações da raiz até que a convergência seja atingida.

  QUAL TOLERÂNCIA USAR?
  - Para aplicações científicas, geralmente se utiliza uma tolerância a erro de 10^-6 ou 10^-12. (1e-6) OU (1e-12)
  - Para aplicações de engenharia, geralmente se utiliza uma tolerância a erro de 10^-3 ou 10^-4. (1e-3) OU (1e-4)
  - Para aplicações financeiras, geralmente se utiliza uma tolerância a erro de 10^-6 ou 10^-8. (1e-6) OU (1e-8)
  
  EXPLICAÇÃO DO CÓDIGO USANDO MÉTODO
  
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


