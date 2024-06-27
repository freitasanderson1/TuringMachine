## Máquina de Turing

##
- Funcionamento:
    - Se o número 1 estiver no inicio da fita, o cabeçote é movido para a direita.
    - Se o número 1 estiver no fim da fita, o anterior da fita é trocado por 1 caso seja 0.
    - Se o cabeçote ler o número 1 ele é trocado por 0 e o cabeçote é movido para a direita.
    - Se o cabeçote ler o número 0 o cabeçote é movido para a direita.
##
#### gravador.py
- Este script tem a função de:

    - Receber códigos de execução da Máquina de Turing.
    - Calcular os hashes desses códigos.
    - Armazenar esses hashes em um arquivo t1.hashes.
##

#### executor.py
- Este script tem a função de:

    - Receber um código fonte de uma Máquina de Turing.
    - Calcular o hash desse código.
    - Verificar se o hash existe no arquivo t1.hashes.
    - Se o hash for encontrado, solicitar a fita inicial e executar o código da Máquina de Turing passo a passo, exibindo a execução animada.
    - Se o hash não for encontrado, informar que o código é corrompido ou não autorizado.