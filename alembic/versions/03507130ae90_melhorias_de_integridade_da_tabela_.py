"""Melhorias de integridade da tabela pagamento.

Revision ID: 03507130ae90
Revises: 693305dd558d
Create Date: 2026-10-13 15:17:39.911597

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '03507130ae90'
down_revision: Union[str, Sequence[str], None] = '693305dd558d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_check_constraint('ck_pagamento_valor_valido', 'pagamento', "valor > 0")

    op.create_check_constraint('ck_pagamento_formas_pagamentos_validas', 'pagamento', "forma_pagamento IN ('pix', 'dinheiro', 'cartao_credito', 'cartao_debito', 'transferencia', 'boleto', 'outros')")

def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('ck_pagamento_valor_valido', 'pagamento', type_='check')

    op.drop_constraint('ck_pagamento_formas_pagamentos_validas', 'pagamento', type_='check')
