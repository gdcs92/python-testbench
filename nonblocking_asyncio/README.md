# nonblocking_asyncio

A ideia nesse diretório é tentar encontrar um jeito de lidar com tasks do
asyncio que estão demorando muito para retornar e atrasando a execução de um
loop onde cada iteração deve ter uma duração fixa.

## Conclusão

Depois de olhar algumas possibilidades diferentes, incluindo fora da biblioteca
asyncio, vi que as funções `wait` e `wait_for` resolvem o meu problema, uma vez
que eu consigo definir um tempo de espera aceitável ao fim do qual vou querer
simplesmente continuar a execução do loop, ignorando tarefas pendentes.

A diferença entre `wait` e `wait_for` é que a primeira ignora tasks que não
tenham sido finalizadas até o timeout (e retorna como segundo elemento da sua
saída), enquanto a segunda cancela e levanta TimeoutError.

Poderia também resolver de outras maneiras; por exemplo através de *threads*.
Entretanto, prefiro a solução com asyncio por ser de fácil implementação e
manter a forma de paralelismo que já estava utilizando.

## Referências

* [Coroutines and Tasks - Python documentation]
(https://docs.python.org/3/library/asyncio-task.html)
* [Real Python - Speed Up Your Python Program With Concurrency]
(https://realpython.com/python-concurrency/)
* [Real Python - Async IO in Python: A Complete Walkthrough]
(https://realpython.com/async-io-python/)
