"""melhorias de integridade e estrutura da tabela documento

Revision ID: 2ea3f3a059f3
Revises: 8904e85896ef
Create Date: 2026-10-08 20:06:37.699520

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2ea3f3a059f3'
down_revision: Union[str, Sequence[str], None] = '8904e85896ef'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column('documento', sa.Column('id_proposta', sa.Integer(), nullable=True))

    op.add_column('documento', sa.Column('formato', sa.VARCHAR(10), nullable=False))

    op.add_column('documento', sa.Column('origem', sa.VARCHAR(30), nullable=False))

    op.create_foreign_key('documento_id_proposta_fkey', 'documento', 'proposta', ['id_proposta'], ['id_proposta'])

    op.alter_column('documento', 'data_geracao', new_column_name='data_cadastro', existing_type=sa.DateTime(timezone=True), existing_nullable=False)

    op.alter_column('documento', 'versao', existing_type=sa.Integer(), existing_nullable=False, server_default=sa.text('1'))

    op.alter_column('documento', 'nome_arquivo', existing_type=sa.String(100), type_=sa.String(255), existing_nullable=False)

    op.create_check_constraint('ck_documento_tipo_permitido', 'documento', "tipo IN ('proposta', 'contrato', 'recibo', 'orcamento','nota_fiscal', 'comprovante', 'cotacao', 'outro')")

    op.create_check_constraint('ck_documento_versao_positiva', 'documento', "versao > 0")

    op.create_check_constraint('ck_documento_formato_permitido', 'documento', "formato IN ('pdf', 'docx', 'xlsx', 'jpg', 'png')")

    op.create_check_constraint('ck_documento_origem_permitida', 'documento', "origem IN ('documento_proprio', 'documento_externo')")


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_constraint('ck_documento_tipo_permitido', 'documento', type_='check')

    op.drop_constraint('ck_documento_versao_positiva', 'documento', type_='check')

    op.drop_constraint('ck_documento_formato_permitido', 'documento', type_='check')

    op.drop_constraint('ck_documento_origem_permitida', 'documento', type_='check')

    op.drop_column('documento', 'origem')

    op.drop_column('documento', 'formato')

    op.drop_constraint('documento_id_proposta_fkey', 'documento', type_='foreignkey')

    op.drop_column('documento', 'id_proposta')

    op.alter_column('documento', 'nome_arquivo', existing_type=sa.String(255), type_=sa.String(100), existing_nullable=False)

    op.alter_column('documento', 'data_cadastro', new_column_name='data_geracao', existing_type=sa.DateTime(timezone=True), existing_nullable=False)

    op.alter_column('documento', 'versao', existing_type=sa.Integer(), existing_nullable=False, server_default=None)