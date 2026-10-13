"""melhorias de integridade da tabela parcela

Revision ID: c4669de4f69e
Revises: 03507130ae90
Create Date: 2026-10-13 19:00:04.153869

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c4669de4f69e'
down_revision: Union[str, Sequence[str], None] = '03507130ae90'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_check_constraint('ck_numero_parcela_valida', 'parcela', "numero_parcela > 0")

    op.create_check_constraint('ck_valor_parcela_valido', 'parcela', "valor > 0")

    op.create_check_constraint('ck_status_validos', 'parcela', "status IN ('paga', 'cancelada', 'atrasada', 'pendente', 'parcialmente_paga')")

    op.create_unique_constraint('uq_parcela_contrato_numero', 'parcela', ['id_contrato', 'numero_parcela'])

    op.alter_column('parcela', 'status', existing_type=sa.String(length=100), existing_nullable=False, server_default=sa.text("'pendente'"))

def downgrade() -> None:
    """Downgrade schema."""

    op.alter_column('parcela', 'status', existing_type=sa.String(length=100), existing_nullable=False, server_default=None)

    op.drop_constraint('uq_parcela_contrato_numero', 'parcela', type_='unique')

    op.drop_constraint('ck_numero_parcela_valida', 'parcela', type_='check')

    op.drop_constraint('ck_valor_parcela_valido', 'parcela', type_='check')

    op.drop_constraint('ck_status_validos', 'parcela', type_='check')