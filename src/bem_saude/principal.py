"""
Ponto de entrada principal da aplicação

Este módulo é o entry point para rodar a aplicação com uvison.

Uso:
    uvicorn bem_saude.principal:app --reload
Ou para produção:
    unicorn bem_saude.principal:app --host 0.0.0.0  --port 8000
"""

from bem_saude.api import app   

__all__ = ["app"]