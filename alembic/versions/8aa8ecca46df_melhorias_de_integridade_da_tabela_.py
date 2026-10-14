"""melhorias de integridade da tabela proposta

Revision ID: 8aa8ecca46df
Revises: c4669de4f69e
Create Date: 2026-10-13 20:06:41.628678

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8aa8ecca46df'
down_revision: Union[str, Sequence[str], None] = 'c4669de4f69e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_check_constraint('ck_proposta_versao_valida', 'proposta', "versao > 0")

    op.create_check_constraint('ck_proposta_valores_decoracao_validos', 'proposta', "valor_decoracao >= 0")

    op.create_check_constraint('ck_proposta_valores_moveis_validos', 'proposta', "valor_moveis >= 0")

    op.create_check_constraint('ck_proposta_valores_adicionais_validos', 'proposta', "valor_adicionais >= 0")

    op.create_check_constraint('ck_proposta_valor_total_valido', 'proposta', "valor_total > 0")

    op.create_check_constraint('ck_proposta_status_validos', 'proposta', "status IN ('aceito', 'recusado', 'cancelado', 'pendente')")

    op.create_unique_constraint('uq_proposta_evento_versao', 'proposta', ['id_evento', 'versao'])

    op.alter_column('proposta', 'status', existing_type=sa.String(length=100), existing_nullable=False, server_default=sa.text("'pendente'"))

def downgrade() -> None:
    """Downgrade schema."""

    op.alter_column('proposta', 'status', existing_type=sa.String(length=100), existing_nullable=False, server_default=None)

    op.drop_constraint('uq_proposta_evento_versao', 'proposta', type_='unique')

    op.drop_constraint('ck_proposta_status_validos', 'proposta', type_='check')

    op.drop_constraint('ck_proposta_valor_total_valido', 'proposta', type_='check')

    op.drop_constraint('ck_proposta_valores_adicionais_validos', 'proposta', type_='check')

    op.drop_constraint('ck_proposta_valores_moveis_validos', 'proposta', type_='check')

    op.drop_constraint('ck_proposta_valores_decoracao_validos', 'proposta', type_='check')

    op.drop_constraint('ck_proposta_versao_valida', 'proposta', type_='check')