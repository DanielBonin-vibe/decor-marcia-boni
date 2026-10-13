"""Melhorias de integridade da tabela item-proposta.

Revision ID: 693305dd558d
Revises: 62eac6f53051
Create Date: 2026-10-13 13:50:01.113932

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '693305dd558d'
down_revision: Union[str, Sequence[str], None] = '62eac6f53051'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_check_constraint('ck_item_proposta_quantidade_valida', 'item_proposta', "quantidade > 0")

    op.create_check_constraint('ck_item_proposta_categorias_validas', 'item_proposta', "categoria IN ('movel', 'decoracao', 'iluminacao', 'flores', 'servico', 'outros')")

    op.create_check_constraint('ck_item_proposta_ordem_valida', 'item_proposta', "ordem > 0")

    op.create_check_constraint('ck_item_proposta_tamanho_nome_valido', 'item_proposta', "LENGTH(TRIM(nome)) > 0")

    op.alter_column('item_proposta', 'categoria', existing_type=sa.String(length=100), existing_nullable=False, server_default=sa.text("'decoracao'"))

    op.alter_column('item_proposta', 'opcional', existing_type=sa.Boolean(), existing_nullable=False, server_default=sa.text("false"))

def downgrade() -> None:
    """Downgrade schema."""
    op.alter_column('item_proposta', 'opcional', existing_type=sa.Boolean(), existing_nullable=False, default=None)

    op.alter_column('item_proposta', 'categoria',  existing_type=sa.String(length=100), existing_nullable=False, default=None)

    op.drop_constraint('ck_item_proposta_quantidade_valida', 'item_proposta', type_='check')

    op.drop_constraint('ck_item_proposta_categorias_validas', 'item_proposta', type_='check')

    op.drop_constraint('ck_item_proposta_ordem_valida', 'item_proposta', type_='check')

    op.drop_constraint('ck_item_proposta_tamanho_nome_valido', 'item_proposta', type_='check')