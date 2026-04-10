from .start import start, menu, servicos, ajuda, contato
from .services import (
    handle_service_acquired,
    handle_consultas,
    handle_cards,
    handle_service_selection,
    handle_card_selection,
    handle_back_to_main,
    handle_back_to_services,
    handle_back_to_consultas,
    handle_back_to_cards,
    handle_partners,
    handle_help_menu,
    handle_how_it_works,
    handle_deadlines,
    handle_payments,
    handle_rules,
    handle_recharges,
    handle_recharge_selection,
    handle_business_hours  # 👈 NOVO
)

__all__ = [
    'start', 'menu', 'servicos', 'ajuda', 'contato',
    'handle_service_acquired', 'handle_consultas', 'handle_cards',
    'handle_service_selection', 'handle_card_selection',
    'handle_back_to_main', 'handle_back_to_services',
    'handle_back_to_consultas', 'handle_back_to_cards',
    'handle_partners', 'handle_help_menu', 'handle_how_it_works',
    'handle_deadlines', 'handle_payments', 'handle_rules',
    'handle_recharges', 'handle_recharge_selection',
    'handle_business_hours'  # 👈 NOVO
]