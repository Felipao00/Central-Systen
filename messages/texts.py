WELCOME_MESSAGE = """
👋<b>Olá, {first_name}! Seja bem vindo(a) a Central Systen!</b>

<b><i>Junte-se à <b>CENTRAL SYSTEN</b> e tenha acesso aos melhores serviços digitais com total segurança e agilidade!</i></b> 🚀

<blockquote>🔍 Escolha o serviço que você adquiriu e fale diretamente com nosso especialista!

😎 A Central Systen possui atendimento personalizado e rápido!</blockquote>

❓ <b><i>Caso tenha dúvidas, acesse nosso menu de Ajuda ou Horários!</i></b>
"""

SERVICE_SELECTION = """
📋 <b>SERVIÇOS DISPONÍVEIS</b>

<blockquote><b>Selecione abaixo o tipo de serviço que você adquiriu em nosso site:</b></blockquote>
"""

CARD_SERVICES = """
💳 <b>SERVIÇOS DE CARTÃO</b>

<blockquote><b>Selecione o tipo de INFO CSS adquirida:</b></blockquote>

<blockquote>❌ <b>Info CC S/Verificação</b>
✅ <b>Info CC Verificado</b></blockquote>
"""

def ghost_specialist_message(service):
    return f"""
🔷 <b>SERVIÇO SELECIONADO: {service}</b> 🔷

<blockquote><i>😁 Para dar continuidade ao seu atendimento,</i>
<i>fale diretamente com nosso especialista.</i></blockquote>

<blockquote><i>⚡ Ele irá processar sua solicitação rapidamente!</i></blockquote>

<blockquote>👀 <b>Obs</b>: <i>Após você entrar em contato, é importante que você envie o PRINT da compra e forneça as informações solicitadas abaixo.</i></blockquote>

━━━━━━━━━━━━━━━━━━
📋 <b>ENVIE NO CHAT DO CANAL:</b>

<blockquote>👤 <b>Especialista:</b> <i>Central</i>
🆔 <b>Seu ID:</b> <i>@username ou ID numérico</i>
📄 <b>Serviço:</b> {service}
🧾 <b>Comprovante:</b> <i>Print do pagamento</i>
📝 <b>Dados para consulta:</b> <i>Informações necessárias</i></blockquote>

👇 <b>Clique no botão abaixo para falar com o especialista:</b>
"""

def tio_duck_specialist_message(service):
    return f"""
🔶 <b>SERVIÇO SELECIONADO: {service}</b> 🔶

<blockquote><i>😁 Para dar continuidade ao seu atendimento,</i>
<i>fale diretamente com nosso especialista.</i></blockquote>

<blockquote><i>⚡ Ele irá processar sua solicitação rapidamente!</i></blockquote>

<blockquote>👀 <b>Obs</b>: <i>Após você entrar em contato, é importante que você envie o PRINT da compra e forneça as informações solicitadas abaixo.</i></blockquote>

━━━━━━━━━━━━━━━━━━
📋 <b>ENVIE NO CHAT DO CANAL:</b>

<blockquote>👤 <b>Especialista:</b> <i>Central</i>
🆔 <b>Seu ID:</b> <i>@username ou ID numérico</i>
📄 <b>Serviço:</b> {service}
🧾 <b>Comprovante:</b> <i>Print do pagamento</i>
📝 <b>Dados para consulta:</b> <i>Informações necessárias</i></blockquote>

👇 <b>Clique no botão abaixo para falar com o especialista:</b>
"""

def card_specialist_message(card_type):
    return f"""
💎 <b>SERVIÇO DE CARTÃO: {card_type}</b> 💎

<blockquote><i>😁 Para dar continuidade ao seu atendimento,</i>
<i>fale diretamente com nosso especialista.</i></blockquote>

<blockquote><i>⚡ Ele irá processar sua solicitação rapidamente!</i></blockquote>

<blockquote>👀 <b>Obs</b>: <i>Após você entrar em contato, é importante que você envie o PRINT da compra e forneça as informações solicitadas abaixo.</i></blockquote>

━━━━━━━━━━━━━━━━━━
📋 <b>ENVIE NO CHAT DO CANAL:</b>

<blockquote>👤 <b>Especialista:</b> <i>Central</i>
🆔 <b>Seu ID:</b> <i>@username ou ID numérico</i>
💳 <b>Serviço:</b> {card_type}
🧾 <b>Comprovante:</b> <i>Print do pagamento</i>
📝 <b>Dados do cartão:</b> <i>BIN e informações solicitadas</i></blockquote>

👇 <b>Clique no botão abaixo para falar com o especialista:</b>
"""

PARTNERS_MESSAGE = """
🤝 <b>Parceiros Oficiais</b> 🤝

<blockquote><b>Todos os parceiros listados abaixo são:</b>
✅ Verificados pela CENTRAL SYSTEN
✅ Confiáveis e seguros
✅ Recomendados oficialmente</blockquote>

💳 <b>Gateway de Pagamento</b>
<i>Bot oficial para processamento de pagamentos</i>

<blockquote>🔹 Transações 100% seguras
🔹 Suporte a PIX e Criptomoedas
🔹 Aprovação instantânea</blockquote>

👇 <i>Clique no botão abaixo para acessar:</i>
"""

HELP_MENU_MESSAGE = """
❓ <b>Central de Ajuda</b> ❓

<i>Selecione abaixo o tópico desejado:</i>

<blockquote>📋 <b>Como Funciona</b> - <i>Entenda nosso processo</i>
⏱️ <b>Prazos</b> - <i>Tempo de entrega dos serviços</i>
💳 <b>Pagamentos</b> - <i>Formas de pagamento aceitas</i></blockquote>

<i>Escolha uma opção para saber mais</i>
"""

HOW_IT_WORKS_MESSAGE = """
📋 <b>Como Funciona</b> 📋

<blockquote>1️⃣ <b>Escolha o serviço</b>
   Navegue pelo menu e selecione o serviço adquirido no nosso site</blockquote>

<blockquote>2️⃣ <b>Fale com o especialista</b>
   Clique no botão para falar diretamente com o responsável</blockquote>

<blockquote>3️⃣ <b>Envie as informações</b>
   Forneça os dados necessários para a consulta ou serviço solicitado</blockquote>

<blockquote>4️⃣ <b>Receba o resultado</b>
   Após a confirmação, você recebe na hora!</blockquote>

━━━━━━━━━━━━━━━━━━
<i>Qualquer dúvida, fale com nosso suporte!</i>
"""

DEADLINES_MESSAGE = """
⏱️ <b>Prazos de Entrega</b> ⏱️

<blockquote><b>CONSULTAS:</b>
🔹 Nossas consultas por se tratarem de serviços que demandam informações,
damos um prazo de até 48 horas para entrega, mas geralmente são entregues em menos de 24 horas.</blockquote>

<blockquote><b>CARTÕES:</b>
🔹 Para serviços de Info CC S/Verificação damos uma média de entrega de até <i>24 horas</i>
🔹 Para serviços de Info CC Verificado damos uma média de entrega de até <i>48 horas</i></blockquote>

━━━━━━━━━━━━━━━━━━
<i>Prazos podem variar conforme demanda</i>
"""

PAYMENTS_MESSAGE = """
💳 <b>Formas de Pagamento</b> 💳

<b>Aceitamos Apenas:</b>
🔸 PIX (Pagamento instantâneo)

<blockquote><b>Quer total segurança nas suas transações?</b>
Use nosso parceiro de pagamentos realizar depósitos
e realizar Transações com total sigilo!</blockquote>

👇 <i>Acesse na aba de PARCEIROS</i>
"""

BUSINESS_HOURS_MESSAGE = """
⏰ <b>Nossos Horários de Funcionamento</b> ⏰

<blockquote><b>🗓️ Segunda a Sexta:</b>
🕤 09:30 às 22:00

<b>🗓️ Sábado e Domingo:</b>
🕙 10:00 às 17:00

<b>🗓️ Feriados:</b>
🕙 10:00 às 17:00 (horário flexível)</blockquote>

━━━━━━━━━━━━━━━━━━
📌 <b>Horário de Brasília (GMT-3)</b>

✅ <b>Atendemos todos os dias!</b>

<i>Qualquer dúvida, fale com nosso suporte!</i>
"""

RULES_MESSAGE = """
📋 <b>Regras da CENTRAL SYSTEN</b> 📋

<blockquote><b>1️⃣ ATENDIMENTO:</b>
• Atendemos somente via Telegram
• Respeite os horários de funcionamento
• Seja claro e objetivo na solicitação</blockquote>

<blockquote><b>2️⃣ SERVIÇOS:</b>
• Todos os serviços são digitais
• Entrega é realizada após confirmação de pagamento
• Não realizamos estornos sobre nenhum serviço prestado</blockquote>

<blockquote><b>3️⃣ PAGAMENTOS:</b>
• Pagamento antecipado
• Comprovante é obrigatório</blockquote>

<blockquote><b>4️⃣ CONDUTA:</b>
• Proibido spam ou assédio
• Respeite nossos especialistas
• Uso indevido resulta em bloqueio</blockquote>

<blockquote><b>5️⃣ PRIVACIDADE:</b>
• Seus dados são protegidos
• Não compartilhamos informações
• Atendimento 100% sigiloso</blockquote>

━━━━━━━━━━━━━━━━━━
⚠️ <i>O descumprimento das regras 
pode resultar em bloqueio permanente.</i>
"""

RECHARGES_MESSAGE = """
📱 <b>Recargas de Celular</b> 📱

<i>Selecione a operadora desejada:</i>

<blockquote>🔴 <b>CLARO</b>
🔵 <b>TIM</b>
🟣 <b>VIVO</b></blockquote>

━━━━━━━━━━━━━━━━━━
<blockquote>⚡ <b>Recarga cai na hora!</b>
✅ Atendimento Rápido e Seguro</blockquote>

👇 <i>Escolha a sua operadora abaixo:</i>
"""

def claro_message():
    return """
🔴 <b>Recarga Claro</b> 🔴

<b>Valores disponíveis:</b>
💰 <i>R$ 25 | R$ 30 | R$ 35 | R$ 40 | R$ 50 | R$ 60 | R$ 100</i>

<blockquote><b>Como funciona:</b>
1️⃣ Informe o número com DDD
2️⃣ Escolha o valor da recarga
3️⃣ Realize o pagamento
4️⃣ Recarga cai na hora!</blockquote>

<b>Bônus Claro:</b>
🎁 <i>A cada R$ 30,00 em recargas, ganhe 1GB de bônus!</i>

━━━━━━━━━━━━━━━━━━
📋 <b>ENVIE NO CHAT DO CANAL:</b>

<blockquote>👤 <b>Especialista:</b> <i>Central</i>
🆔 <b>Seu ID:</b> <i>@username ou ID numérico</i>
📱 <b>Serviço:</b> <i>Recarga CLARO</i>
🧾 <b>Comprovante:</b> <i>Print do pagamento</i>
📞 <b>Número:</b> <i>Com DDD (ex: 11 99999-9999)</i>
💰 <b>Valor:</b> <i>R$ 25, 30, 35, 40, 50, 60 ou 100</i></blockquote>

⚠️ <i>Recarga válida para todo Brasil</i>

👇 <b>Clique abaixo para falar com o especialista:</b>
"""

def tim_message():
    return """
🔵 <b>Recarga Tim</b> 🔵

<b>Valores disponíveis:</b>
💰 <i>R$ 20 | R$ 30</i>

<blockquote><b>Como funciona:</b>
1️⃣ Informe o número com DDD
2️⃣ Escolha o valor da recarga
3️⃣ Realize o pagamento
4️⃣ Recarga cai na hora!</blockquote>

<b>Bônus TIM:</b>
🎁 <i>Recargas acima de R$ 30 ganham TIM Banca ilimitada!</i>

━━━━━━━━━━━━━━━━━━
📋 <b>ENVIE NO CHAT DO CANAL:</b>

<blockquote>👤 <b>Especialista:</b> <i>Central</i>
🆔 <b>Seu ID:</b> <i>@username ou ID numérico</i>
📱 <b>Serviço:</b> <i>Recarga TIM</i>
🧾 <b>Comprovante:</b> <i>Print do pagamento</i>
📞 <b>Número:</b> <i>Com DDD (ex: 11 99999-9999)</i>
💰 <b>Valor:</b> <i>R$ 20 ou R$ 30</i></blockquote>

⚠️ <i>Recarga válida para todo Brasil</i>

👇 <b>Clique abaixo para falar com o especialista:</b>
"""

def vivo_message():
    return """
🟣 <b>Recarga Vivo</b> 🟣

<b>Valores disponíveis:</b>
💰 <i>R$ 20 | R$ 25 | R$ 30</i>

<blockquote><b>Como funciona:</b>
1️⃣ Informe o número com DDD
2️⃣ Escolha o valor da recarga
3️⃣ Realize o pagamento
4️⃣ Recarga cai na hora!</blockquote>

<b>Bônus VIVO:</b>
🎁 <i>VIVO Turbo: 2x mais internet nas recargas!</i>

━━━━━━━━━━━━━━━━━━
📋 <b>ENVIE NO CHAT DO CANAL:</b>

<blockquote>👤 <b>Especialista:</b> <i>Central</i>
🆔 <b>Seu ID:</b> <i>@username ou ID numérico</i>
📱 <b>Serviço:</b> <i>Recarga VIVO</i>
🧾 <b>Comprovante:</b> <i>Print do pagamento</i>
📞 <b>Número:</b> <i>Com DDD (ex: 11 99999-9999)</i>
💰 <b>Valor:</b> <i>R$ 20, R$ 25 ou R$ 30</i></blockquote>

⚠️ <i>Recarga válida para todo Brasil</i>

👇 <b>Clique abaixo para falar com o especialista:</b>
"""

OUT_OF_HOURS_MESSAGE = """
😴 <b>Estamos fora do horário de funcionamento</b> 😴

<i>Nossa equipe está descansando no momento!</i>

<blockquote><b>📅 Hoje é {current_day}</b>
<b>🕐 Hora atual:</b> {current_time} (Brasília)</blockquote>

<blockquote><b>⏰ Nosso horário de atendimento:</b>
{business_hours}</blockquote>

━━━━━━━━━━━━━━━━━━
✅ <b>Sua solicitação foi registrada!</b>

<blockquote>💡 <i>Volte durante nosso horário de 
funcionamento para atendimento imediato!</i></blockquote>

👇 <i>Você pode consultar nossos horários no menu principal.</i>
"""

# Adicione no final do arquivo:

BOT_VIP_MESSAGE = """
🤖 <b>BOT VIP COMPLETO - Tudo que você precisa!</b> 🤖

<blockquote><b>Um único bot com TODAS as funcionalidades para automatizar e monetizar seu grupo ou canal no Telegram!</b></blockquote>

━━━━━━━━━━━━━━━━━━
<b>🚀 TUDO INCLUSO NO SEU BOT:</b>

<blockquote>🔒 <b>Gestão de Grupo VIP</b>
<i>Controle de acesso por assinatura, links temporários, expulsão automática.</i>

📦 <b>Sistema de Vendas</b>
<i>Venda de packs, produtos digitais e serviços automatizados.</i>

🎟️ <b>Assinaturas Recorrentes</b>
<i>Cobrança automática mensal, semanal ou anual.</i>

💰 <b>Pagamento PIX Automático</b>
<i>Confirmação instantânea, liberação automática.</i>

📊 <b>Painel de Gestão</b>
<i>Controle total de membros, vendas e assinaturas.</i></blockquote>

━━━━━━━━━━━━━━━━━━
<b>⚙️ FUNCIONALIDADES COMPLETAS:</b>

<blockquote>✅ Pagamento via PIX automático
✅ Gestão de membros VIP (adiciona/remove automaticamente)
✅ Expulsão de inadimplentes
✅ Links de convite únicos e temporários
✅ Múltiplos planos de assinatura
✅ Sistema de vendas de packs/produtos
✅ Entrega automática após pagamento
✅ Cobrança recorrente (semanal/mensal/anual)
✅ Lembretes de vencimento
✅ Relatórios de vendas e assinantes
✅ Painel administrativo completo
✅ Personalização de nome, cores e valores
✅ Suporte a múltiplos grupos/canais</blockquote>

━━━━━━━━━━━━━━━━━━
💰 <b>INVESTIMENTO ÚNICO:</b>

<blockquote><b>🔥 VALOR FIXO: R$ 110,90 🔥</b>
<i>Pagamento único - NUNCA mais paga nada!</i>

⚡ <b>Entrega:</b> <i>Até 24 a 48 horas após pagamento</i>
🎨 <b>Personalização:</b> <i>Você escolhe nome, valores dos planos e dias</i>
📦 <b>Já tem packs?</b> <i>Configuramos tudo para você!</i>
🛠️ <b>Suporte:</b> <i>Te ajudamos a configurar</i></blockquote>

━━━━━━━━━━━━━━━━━━
<b>📋 COMO FUNCIONA:</b>

<blockquote>1️⃣ Você nos envia as informações (nome do bot, valores, packs)
2️⃣ Configuramos seu bot na nossa plataforma
3️⃣ Em até 24h ele está PRONTO e FUNCIONANDO
4️⃣ É só adicionar no seu grupo e começar a lucrar!</blockquote>

<blockquote><i>💡 Um único bot faz TUDO: gestão VIP + vendas + assinaturas!</i></blockquote>

👇 <i>Escolha uma opção abaixo:</i>
"""

# Remove as mensagens MODEL_VIP_GROUP_MESSAGE, MODEL_SALES_MESSAGE, MODEL_SUBSCRIPTION_MESSAGE
# pois agora é um único bot completo

# Atualize o REQUEST_QUOTE_MESSAGE:
REQUEST_QUOTE_MESSAGE = """
💬 <b>SOLICITAR BOT VIP COMPLETO</b> 💬

<blockquote><i>Garanta já seu Bot VIP Completo por apenas <b>R$ 110,90</b>!</i></blockquote>

━━━━━━━━━━━━━━━━━━
📋 <b>ENVIE NO CHAT DO CANAL:</b>

<blockquote>👤 <b>Especialista:</b> <i>Central</i>
🆔 <b>Seu ID:</b> <i>@username ou ID numérico</i>
🤖 <b>Serviço:</b> <i>Bot VIP Completo</i>
📝 <b>Informe:</b>
  • Nome desejado para o bot
  • Valores dos planos (se tiver) e a quantidade de dias de cada plano
  • Quais packs/produtos vai vender caso tenha</blockquote>

━━━━━━━━━━━━━━━━━━
💰 <b>VALOR: R$ 110,90 (PAGAMENTO ÚNICO)</b>

⚡ <i>Após pagamento, entrega em até 24 a 48 horas!</i>

👇 <b>Clique abaixo para falar com o especialista:</b>
"""

# Adicione no final do arquivo:

FF_ACCOUNTS_MESSAGE = """
🎮 <b>CONTAS FREE FIRE</b> 🎮

<blockquote><b>Contas de Free Fire de alta qualidade, seguras e com garantia!</b></blockquote>

━━━━━━━━━━━━━━━━━━
<b>🔥 O QUE OFERECEMOS:</b>

<blockquote>✅ Contas niveladas e prontas para jogar
✅ Skins lendárias e raras
✅ Personagens desbloqueados
✅ Pets e emotes exclusivos
✅ Diamantes e ouro na conta
✅ Passe de elite ativo
✅ Troca de email e senha na hora
✅ Garantia de 7 dias</blockquote>

━━━━━━━━━━━━━━━━━━
<b>🛡️ SEGURANÇA E GARANTIA:</b>

<blockquote>🔒 Contas 100% seguras e verificadas
📧 Email e senha originais
🔄 Suporte para troca de dados
✅ Garantia de 7 dias contra recuperação
⚡ Entrega imediata após pagamento</blockquote>

━━━━━━━━━━━━━━━━━━
<b>📋 COMO COMPRAR:</b>

<blockquote>1️⃣ Clique em "VER CONTAS DISPONÍVEIS"
2️⃣ Escolha a conta que deseja
3️⃣ Clique em "SOLICITAR CONTA"
4️⃣ Fale com o nosso especialista
5️⃣ Realize o pagamento via PIX
6️⃣ Receba os dados da conta na hora!</blockquote>

👇 <i>Escolha uma opção abaixo:</i>
"""

FF_ACCOUNTS_LIST_MESSAGE = """
📋 <b>CONTAS FREE FIRE DISPONÍVEIS</b> 📋

<blockquote><i>Estoque atualizado diariamente!</i></blockquote>

━━━━━━━━━━━━━━━━━━

<blockquote>⛔No momento, estamos sem contas disponíveis, mas não se preocupe! Nosso estoque é renovado constantemente. Fale com nosso especialista para saber mais sobre as próximas disponibilizações e garantir a sua conta personalizada!</blockquote>

━━━━━━━━━━━━━━━━━━

<b>🎯 CONTAS PERSONALIZADAS</b>
<blockquote><i>Não encontrou o que queria?
Solicite uma conta personalizada com as skins e personagens que você deseja!</i></blockquote>

👇 <i>Clique abaixo para solicitar sua conta:</i>
"""

FF_PRICES_MESSAGE = """
💰 <b>TABELA DE PREÇOS - CONTAS FREE FIRE</b> 💰

<blockquote><b>Valores base - Consulte disponibilidade!</b></blockquote>

<b>📊 CONTAS POR NÍVEL:</b>

<blockquote>🔥 Vamos disponibilizar os requisitos das contas vendidas pela central logo mais. Aguarde!</blockquote>

<b>🎨 SKINS EXTRAS (ADICIONAL):</b>

<blockquote>📍 Em Desenvolvimento</blockquote>

<b>💳 FORMAS DE PAGAMENTO:</b>

<blockquote>✅ PIX (Pagamento instantâneo)
✅ Entrega imediata após confirmação</blockquote>

👇 <i>Solicite sua conta agora:</i>
"""

REQUEST_FF_ACCOUNT_MESSAGE = """
💬 <b>SOLICITAR CONTA FREE FIRE</b> 💬

<blockquote><i>Garanta já sua conta de Free Fire!</i></blockquote>

━━━━━━━━━━━━━━━━━━
📋 <b>ENVIE NO CHAT DO CANAL:</b>

<blockquote>👤 <b>Especialista:</b> <i>Central</i>
🆔 <b>Seu ID:</b> <i>@username ou ID numérico</i>
🎮 <b>Serviço:</b> <i>CONTA FREE FIRE</i>
📝 <b>Informe:</b>
  • Qual conta deseja (nível/personagens)
  • Ou descreva a conta dos sonhos</blockquote>

━━━━━━━━━━━━━━━━━━
⚡ <i>Entrega imediata após confirmação do pagamento!</i>
🛡️ <i>Garantia de 3 dias contra recuperação!</i>

👇 <b>Clique abaixo para falar com Tio Duck:</b>
"""

FAKE_NOTES_MESSAGE = """
💵 <b>NOTAS FALSAS - ALTA QUALIDADE</b> 💵

<blockquote><b>Notas falsas de alta qualidade, idênticas às reais!</b></blockquote>

━━━━━━━━━━━━━━━━━━
<b>🔥 O QUE OFERECEMOS:</b>

<blockquote>✅ Notas que passam no teste da caneta
✅ Marca d'água e alto relevo
✅ Fita de segurança holográfica
✅ Numeração individual por nota
✅ Qualidade superior AAA+
✅ Entrega discreta e segura
✅ Embalagem camuflada
✅ Rastreio disponível</blockquote>

━━━━━━━━━━━━━━━━━━
<b>📦 VALORES DISPONÍVEIS:</b>

<blockquote>💵 R$ 20,00
💵 R$ 50,00
💵 R$ 100,00
💵 R$ 200,00</blockquote>

━━━━━━━━━━━━━━━━━━
<b>📋 COMO COMPRAR:</b>

<blockquote>1️⃣ Clique em "VER VALORES" para ver os preços
2️⃣ Escolha a quantidade e valor das notas
3️⃣ Clique em "SOLICITAR NOTAS"
4️⃣ Fale com o especialista
5️⃣ Realize o pagamento
6️⃣ Receba seu pedido discretamente</blockquote>

<blockquote><i>👤 Especialista responsável: GHOST</i></blockquote>

👇 <i>Escolha uma opção abaixo:</i>
"""

FAKE_NOTES_PRICES_MESSAGE = """
💰 <b>TABELA DE PREÇOS - NOTAS FALSAS</b> 💰

<blockquote><b>Qualidade AAA+ - As melhores do mercado!</b></blockquote>

━━━━━━━━━━━━━━━━━━

<b>💵 NOTA DE R$ 20,00</b>
<blockquote>📦 10 unidades: R$ XX,XX
📦 20 unidades: R$ XX,XX
📦 50 unidades: R$ XX,XX
📦 100 unidades: R$ XX,XX</blockquote>

━━━━━━━━━━━━━━━━━━

<b>💵 NOTA DE R$ 50,00</b>
<blockquote>📦 10 unidades: R$ XX,XX
📦 20 unidades: R$ XX,XX
📦 50 unidades: R$ XX,XX
📦 100 unidades: R$ XX,XX</blockquote>

━━━━━━━━━━━━━━━━━━

<b>💵 NOTA DE R$ 100,00</b>
<blockquote>📦 10 unidades: R$ XX,XX
📦 20 unidades: R$ XX,XX
📦 50 unidades: R$ XX,XX
📦 100 unidades: R$ XX,XX</blockquote>

━━━━━━━━━━━━━━━━━━

<b>💵 NOTA DE R$ 200,00</b>
<blockquote>📦 10 unidades: R$ XX,XX
📦 20 unidades: R$ XX,XX
📦 50 unidades: R$ XX,XX
📦 100 unidades: R$ XX,XX</blockquote>

━━━━━━━━━━━━━━━━━━

<b>🎁 KIT MISTO (TODOS OS VALORES)</b>
<blockquote>📦 40 unidades (10 de cada): R$ XX,XX
📦 80 unidades (20 de cada): R$ XX,XX
📦 200 unidades (50 de cada): R$ XX,XX</blockquote>

👇 <i>Solicite agora seu pedido:</i>
"""

FAKE_NOTES_INFO_MESSAGE = """
📋 <b>COMO FUNCIONA - NOTAS FALSAS</b> 📋

<blockquote><b>Tudo que você precisa saber sobre nossas notas!</b></blockquote>

━━━━━━━━━━━━━━━━━━

<b>✅ QUALIDADE GARANTIDA:</b>

<blockquote>🔹 Passam no teste da caneta
🔹 Marca d'água visível contra luz
🔹 Alto relevo perceptível ao toque
🔹 Fita holográfica brilhante
🔹 Numeração individual
🔹 Tamanho e cor idênticos</blockquote>

━━━━━━━━━━━━━━━━━━

<b>📦 ENVIO E ENTREGA:</b>

<blockquote>🚚 Envio discreto em embalagem camuflada
📮 Sedex ou PAC (com rastreio)
⏱️ Prazo de entrega: 3 a 7 dias úteis
🔒 Seus dados 100% seguros</blockquote>

━━━━━━━━━━━━━━━━━━

<b>💳 PAGAMENTO:</b>

<blockquote>✅ PIX (Pagamento instantâneo)
✅ Criptomoedas (consulte)
✅ Envio após confirmação do pagamento</blockquote>

━━━━━━━━━━━━━━━━━━

<b>⚠️ GARANTIA:</b>

<blockquote>🛡️ Garantia de 7 dias contra defeitos
🔄 Troca em caso de problemas na entrega
📞 Suporte via Telegram</blockquote>

👇 <i>Pronto para comprar? Solicite agora:</i>
"""

REQUEST_FAKE_NOTES_MESSAGE = """
💬 <b>SOLICITAR NOTAS FALSAS</b> 💬

<blockquote><i>Garanta já suas notas de alta qualidade!</i></blockquote>

━━━━━━━━━━━━━━━━━━
📋 <b>ENVIE NO CHAT DO CANAL:</b>

<blockquote>👤 <b>Especialista:</b> <i>GHOST</i>
🆔 <b>Seu ID:</b> <i>@username ou ID numérico</i>
💵 <b>Serviço:</b> <i>NOTAS FALSAS</i>
📝 <b>Informe:</b>
  • Qual valor de nota deseja
  • Quantidade desejada
  • Endereço para envio (com CEP)</blockquote>

━━━━━━━━━━━━━━━━━━
⚡ <i>Entrega em 3 a 7 dias úteis após pagamento!</i>
🛡️ <i>Garantia de qualidade AAA+!</i>
📮 <i>Envio discreto e seguro!</i>

👇 <b>Clique abaixo para falar com Ghost:</b>
"""