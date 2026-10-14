"""melhorias de integridade da tabela usuario

Revision ID: 2b0a60562e70
Revises: 596c2be827a3
Create Date: 2026-10-14 10:37:00.896305

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2b0a60562e70'
down_revision: Union[str, Sequence[str], None] = '596c2be827a3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    op.create_check_constraint('ck_usuario_perfil_valido', 'usuario', "perfil IN ('funcionario', 'admin')")

    op.create_check_constraint('ck_usuario_tamanho_nome_valido', 'usuario', "LENGTH(TRIM(nome)) > 0")

    op.create_check_constraint('ck_usuario_tamanho_senha_hash__valido', 'usuario', "LENGTH(TRIM(senha_hash)) > 0")

    op.create_check_constraint('ck_usuario_formato_email_valido', 'usuario', "LENGTH(TRIM(email)) > 0")

    op.create_index('uq_usuario_email_lower', 'usuario', [sa.text('LOWER(email)')], unique=True)

    op.alter_column('usuario', 'ativo', existing_type=sa.Boolean(), existing_nullable=False, server_default=sa.text('true'))

    op.drop_constraint('usuario_email_key', 'usuario', type_='unique')

def downgrade() -> None:
    """Downgrade schema."""

    op.create_unique_constraint('usuario_email_key', 'usuario', ['email'])

    op.alter_column('uq_usuario_email_lower', 'ativo', existing_type=sa.Boolean(), existing_nullable=False, server_default=None)

    op.drop_index('uq_usuario_email_lower', table_name='usuario')
    
    op.drop_constraint('ck_usuario_formato_email_valido', 'usuario', type_='check')

    op.drop_constraint('ck_usuario_tamanho_senha_hash__valido', 'usuario', type_='check')

    op.drop_constraint('ck_usuario_tamanho_nome_valido', 'usuario', type_='check')

    op.drop_constraint('ck_usuario_perfil_valido', 'usuario', type_='check')
