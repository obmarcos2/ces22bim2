  Para a síntese do diagrama de classes, primeiramente elaborou-se o diagrama para a classse Livro. Como esta
possui métodos distintos para cada tipo de gênero para o cálculo das taxas, é pertinente o uso da interface
Impostolivro para que possa ser modificada e extendida as taxas para cada gênero, sem precisar modificar a
classe Livro. 
  Com o mesmo raciocínio, tem-se a criação de uma interface de produtos, visando a futura adição de novos produtos
para venda no projeto. Com efeito, tem-se métodos definidos nele de modo que possam ser utilizados na classe
Carrinho, que manipula os produtos adquiridos pelo usuário.
  Por fim, tem-se o uso da classe BancoDados, que agregam os clientes, produtos e autores. Nessa classe é
denotado a manipulação das instâncias de forma simples (via armazenamento em lista), de modo a introduzir os
métodos de busca.

![diagram](https://user-images.githubusercontent.com/101301437/178034386-12f64e71-4560-49a7-a4e8-2f1f7b4da985.png)

Por fim, note-se que cada classe é implementada em seu próprio script, bem como as interfaces são denotadas
em um único script. o script main.py demonstra algumas operações presentes em tal projeto, cujo resultado segue também em png.
