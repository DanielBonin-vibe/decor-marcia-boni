"""melhorias de integridade da tabela evento

Revision ID: 62eac6f53051
Revises: 2ea3f3a059f3
Create Date: 2026-10-13 10:22:19.646919

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '62eac6f53051'
down_revision: Union[str, Sequence[str], None] = '2ea3f3a059f3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_check_constraint('ck_evento_convidados_validos', 'evento', 'numero_convidados > 0')

    op.create_check_constraint('ck_evento_tipos_validos', 'evento', "tipo_evento IN ('casamento', 'aniversario', 'formatura', 'corporativo', 'batizado', 'outro')")

    op.create_check_constraint('ck_evento_status_valido', 'evento', "status IN ('planejamento', 'confirmado', 'realizado', 'cancelado')")

    op.alter_column('evento', 'status', existing_type=sa.String(length=100), existing_nullable=False, server_default=sa.text("'planejamento'"))


def downgrade() -> None:
    """Downgrade schema."""

    op.alter_column('evento', 'status', existing_type=sa.String(100), existing_nullable=False, server_default=None)

    op.drop_constraint('ck_evento_convidados_validos', 'evento', type_='check')

    op.drop_constraint('ck_evento_tipos_validos', 'evento',  type_='check')

    op.drop_constraint('ck_evento_status_valido','evento', type_='check')