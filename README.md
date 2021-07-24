# Introdução:
  Este é um algoritmo que calcula a demanda mínima de energia necessária, proveniente de utilidades (vapor e água de refrigeração) a serem adicionados a um processo industrial contínuo. O objetivo é reaproveitar a energia contida nas linhas quentes e frias do processo produtivo. O algoritmo não retorna necessariamente um valor ótimo, mas sim um valor bom. Seu uso pode ser utilizado para fins didáticos ou como uma primeira análise de projetos, pois é uma alternativa com baixo custo computacional frente à modelos de otimização existentes, onde sua aplicação prática se justifica no sentido de resultar numa quantidade factível de energia passível de ser reaproveitada. 
Para saber detalhes teóricos sobre a análise Pinch, recomendo a leitura do livro Redes de Trocadores de Calor – Ravagnani e Suaréz. 

# Como ele faz:
  É necessário saber:
  1) Quantidade de correntes frias e quentes (que não seja utilidade) existentes no processo.
  2) Entalpia (MW) de cada corrente, ou a Capacidade Térmica (MW/°C) de cada corrente.
  3) Temperatura (°C) de entrada e saída de cada corrente.
  4) Diferença de temperatura mínima permitida nos terminais dos trocadores de calor (Delta T min).

# O Resultado:
  Você pode escolher entre imprimir o resultado na tela, ou gerar um arquivo xlsx, que será enviado para o mesmo path dos arquivos py.

# Considerações:
  1) O método despreza mudanças de fase entre as correntes de processo.
  2) Entende-se como correntes, o fluxo material das substancias participantes do processo industrial que não sejam as utilidades.

# Cuidados:
  Não entrar com valores de Entalpia ou Capacidade Térmica negativos.
  Não utilizar virgula (,) como separador de decimal, e sim (.).

# Exemplo Prático: 
  Dados do Problema:

![image](https://user-images.githubusercontent.com/79408563/126881347-c4b1e68e-395a-4623-8349-75199e649654.png)


  Após executar o programa você deverá selecionar a opção desejada e o número de correntes de processo:
  
  ![image](https://user-images.githubusercontent.com/79408563/126881415-421e57a3-e67c-480a-8827-f1fd5094a605.png)


  Na sequência você deve inserir os dados das correntes:
  
  ![image](https://user-images.githubusercontent.com/79408563/126881445-affa9a0d-4de1-4291-b8ef-f7960cde8347.png) 
  ![image](https://user-images.githubusercontent.com/79408563/126881463-9617e271-2631-4e41-9f1f-97975fcff9fc.png)

  Por último, insira o delta T min desejado:
  
  ![image](https://user-images.githubusercontent.com/79408563/126881497-3a41a5ba-aefc-4404-b650-4d290c521ebd.png)

  Escolha se deseja ver o resultado na tela, ou se quer gerar um arquivo xlsx com o resultado obtido.
  
  ![image](https://user-images.githubusercontent.com/79408563/126881519-b19ab4c3-8a59-4f03-973b-f55fa420a960.png)

  Saídas:    
    Primeiramente veremos uma tabela com todos os dados que inserimos para a resolução do problema, e posteriormente veremos os resultados. Destaquei em amarelo as quantidades de energia que devem ser retiradas e inseridas do processo e a Temperatura Pinch.
  
   ![image](https://user-images.githubusercontent.com/79408563/126881567-5d88d687-c190-4fcf-a5e1-ebcfeee33fbc.png)
