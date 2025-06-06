
# Monitoramento de Movimentos no Escuro – Projeto IoT

## Descrição

Este projeto propõe uma solução de monitoramento de movimentos em ambientes escuros, com foco especial em situações de **queda de energia**. O objetivo principal é **preservar a segurança vital das pessoas**, detectando presença em locais com baixa iluminação e emitindo alertas imediatos via som (alarme sonoro).

A solução se insere em um contexto de **Segurança**, mitigando riscos decorrentes de falhas de energia que podem comprometer a integridade de indivíduos em ambientes vulneráveis.

## Componentes do Projeto

- **main.py** – Código principal de execução do sistema de detecção.
- **requirements.txt** – Lista de bibliotecas necessárias para rodar o projeto.
- **alarm.wav** – Arquivo de som utilizado como alarme de detecção.

## Funcionalidades

- Monitoramento contínuo de presença via sensores (adaptável a PIR ou outros).
- Execução de alarme sonoro ao detectar movimento no escuro.
- Pode ser integrado a soluções maiores de monitoramento e segurança.

## Como Executar

1. Clone este repositório ou extraia o conteúdo.
2. Instale as dependências com:

   ```bash
   pip install -r requirements.txt
   ```

3. Execute o programa:

   ```bash
   python main.py
   ```

> **Nota**: É necessário que o dispositivo tenha suporte a áudio para reprodução do alarme.

## Autores

- **Guilherme Daher** – 98611  
- **Gustavo Akio** – 550241  
- **Heitor Nobre** – 551539
