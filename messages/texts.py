WELCOME_MESSAGE = """
👋<b>Olá, {first_name}! Seja bem vindo(a) a Central Systen!</b>

<b><i>Junte-se à <b>CENTRAL SYSTEN</b> e tenha acesso aos melhores serviços digitais com total segurança e agilidade!</i></b> 🚀

<blockquote>🔍 Escolha o serviço que você adquiriu e fale diretamente com nosso especialista!

😎 Com a <b>CENTRAL SYSTEN</b>, você tem:
🔹 Atendimento rápido e personalizado
🔹 Especialistas verificados
🔹 100% de sigilo e segurança</blockquote>

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

<blockquote><b>Assim que estivermos online, um especialista </b>
<b>entrará em contato para atendê-lo.</b></blockquote>

💡 <i>Volte durante nosso horário de 
funcionamento para atendimento imediato!</i>

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