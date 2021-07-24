# Análise Pinch - Integração Energética.
Engenharia Química/Integração Energética.

# O que ele faz:
Algoritmo que calcula a demanda mínima de energia necessária proveniente de utilidades (vapor, água de refrigeração) a serem adicionados ao processo. De tal forma a reaproveitar a energia contida nas linhas quentes e frias do processo produtivo. O algoritmo é uma alternativa com baixo custo computacional frente à modelos de otimização existentes.

# Como ele faz:
É necessário saber basicamente duas coisas:
  1) Quantidade de correntes frias e quentes (que não seja utilidade) existentes no processo.
  2) Entalpia específica de cada corrente, ou a capacidade calorífica específica de cada corrente.

# Considerações:
  1) O método despreza mudança de fase entre as correntes de processo.
  2) Entende-se como correntes, o fluxo material das substancias participantes do processo químico que não sejam as utilidades.

