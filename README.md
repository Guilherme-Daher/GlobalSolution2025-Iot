
# Projeto IoT – Monitoramento de Movimentos no Escuro

## Visão Geral

Este projeto foi desenvolvido com o objetivo de **proteger residências durante quedas de energia**, quando sistemas comuns de segurança (como portões automáticos, câmeras ou iluminação) podem ficar inoperantes.

A proposta é simples: ao detectar **qualquer movimento suspeito no escuro**, o sistema emite um **alarme sonoro**, funcionando como um aviso imediato para moradores e também como uma forma de **inibir possíveis invasores**.

Imagine a seguinte situação: a luz acaba, o portão da casa fica aberto, a rua está escura... e alguém mal-intencionado se aproxima. Esse projeto entra em ação nesses momentos críticos.

## Objetivo

Criar uma solução acessível que:

- Detecta movimentos em ambientes sem iluminação.
- Emite um **alerta sonoro imediato** ao identificar uma presença suspeita.
- Atua como medida de **prevenção contra invasões e riscos durante apagões**.

## Estrutura do Projeto

- `main.py` – Código principal que detecta movimento e dispara o alarme.
- `alarm.wav` – Som de alerta usado para assustar e alertar.
- `requirements.txt` – Bibliotecas necessárias para executar o código.

## Como Funciona

- O sensor detecta qualquer movimentação no ambiente.
- Caso seja identificado alguém se movendo no escuro, o sistema dispara um som de alarme (alto e claro).
- Pode ser usado em entradas de casas, garagens, corredores, varandas e quintais.

## Como Usar

```bash
# 1. Clone o repositório:
git clone https://github.com/Guilherme-Daher/GlobalSolution2025-Iot.git
cd GlobalSolution2025-Iot

# 2. Instale os pacotes necessários:
pip install -r requirements.txt

# 3. Execute o sistema:
python main.py
```

> Recomendação: Use este sistema com algum sensor de movimento compatível com Raspberry Pi ou similar. A reprodução do alarme exige que o dispositivo tenha saída de áudio.

## Possíveis Expansões

- Integração com sistema de iluminação de emergência.
- Notificação por aplicativo (Telegram, WhatsApp, etc.).
- Integração com câmeras ou gravação de vídeo.
- Alimentação via bateria ou nobreak (para continuar funcionando mesmo sem energia).

## Autores

- Guilherme Daher – RA: 98611  
- Gustavo Akio – RA: 550241  
- Heitor Nobre – RA: 551539

---

Projeto desenvolvido como parte da disciplina de **Engenharia de Software**  
**FIAP – Global Solution 2025**
