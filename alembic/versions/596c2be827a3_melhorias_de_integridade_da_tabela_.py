"""melhorias de integridade da tabela recibo

Revision ID: 596c2be827a3
Revises: 8aa8ecca46df
Create Date: 2026-10-14 09:25:05.155667

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '596c2be827a3'
down_revision: Union[str, Sequence[str], None] = '8aa8ecca46df'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.execute("CREATE SEQUENCE seq_numero_recibo START WITH 1")

    op.alter_column('recibo', 'numero_recibo', existing_type=sa.Integer(), existing_nullable=False, server_default=sa.text("nextval('seq_numero_recibo'::regclass)"))

    op.create_check_constraint('ck_numero_recibo_valido', 'recibo', "numero_recibo > 0")

    op.create_unique_constraint('uq_recibo_id_pagamento', 'recibo', ['id_pagamento'])

    op.add_column('recibo', sa.Column('observacoes', sa.String(1000), nullable=True))

    op.add_column('recibo', sa.Column('data_criacao', sa.DateTime(timezone=True), nullable=False, server_default=sa.func.now()))

def downgrade() -> None:
    """Downgrade schema."""

    op.drop_column('recibo', 'data_criacao')

    op.drop_column('recibo', 'observacoes')

    op.drop_constraint('uq_recibo_id_pagamento', 'recibo', type_='unique')

    op.drop_constraint('ck_numero_recibo_valido', 'recibo', type_='check')

    op.alter_column('recibo', 'numero_recibo', existing_type=sa.Integer(), existing_nullable=False, server_default=None)

    op.execute("DROP SEQUENCE seq_numero_recibo")