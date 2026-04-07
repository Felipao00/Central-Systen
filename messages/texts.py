WELCOME_MESSAGE = """
🎯 <b>BEM-VINDO À CENTRAL SYSTEN</b> 🎯

<blockquote><b>Olá! Somos especialistas em soluções digitais.</b>
<b>Clique no botão abaixo para selecionar o tipo de serviço adquirido.</b></blockquote>

<i>Especialistas disponíveis para...</i>
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

<blockquote><i>Para dar continuidade ao seu atendimento,</i>
<i>fale diretamente com nosso especialista.</i></blockquote>

<blockquote><i>Ele irá processar sua solicitação rapidamente! ⚡</i></blockquote>

👇 <i>Clique no botão abaixo!</i> 👇
"""

def tio_duck_specialist_message(service):
    return f"""
🔶 <b>SERVIÇO SELECIONADO: {service}</b> 🔶

<blockquote><i>Para dar continuidade ao seu atendimento,</i>
<i>fale diretamente com nosso especialista.</i></blockquote>

<blockquote><i>Ele irá processar sua solicitação rapidamente! ⚡</i></blockquote>

👇 <i>Clique no botão abaixo!</i> 👇
"""

def card_specialist_message(card_type):
    return f"""
💎 <b>SERVIÇO DE CARTÃO: {card_type}</b> 💎

<blockquote><i>Para dar continuidade ao seu atendimento,</i>
<i>fale diretamente com nosso especialista.</i></blockquote>

<blockquote><i>Ele irá processar sua solicitação com total segurança! 🔒</i></blockquote>

👇 <i>Clique no botão abaixo!</i> 👇
"""