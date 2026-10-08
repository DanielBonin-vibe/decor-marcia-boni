"""melhorias de integridade e normalizacao da tabela contrato

Revision ID: 8904e85896ef
Revises: 752f218b6de2
Create Date: 2026-10-08 18:13:03.319158

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8904e85896ef'
down_revision: Union[str, Sequence[str], None] = '752f218b6de2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column('contrato', 'status', new_column_name='status_contrato', existing_type=sa.String(length=100),
        existing_nullable=False
    )

    op.alter_column('contrato', 'status_contrato', existing_type=sa.String(length=100), 
        existing_nullable=False, server_default=sa.text("'rascunho'")
        )

    op.create_check_constraint('ck_contrato_valor_positivo', 
    'contrato', "valor_total > 0"
    )

    op.create_check_constraint('ck_contrato_status_contrato', 'contrato', "status_contrato IN ('rascunho', 'assinado', 'pendente_assinatura', 'cancelado')")

    op.create_check_constraint('ck_contrato_integridade_assinatura', 'contrato', """
        (status_contrato = 'assinado' AND data_assinatura IS NOT NULL) OR
        (status_contrato = 'rascunho' AND data_assinatura IS NULL) OR
        (status_contrato = 'pendente_assinatura' AND data_assinatura IS NULL) OR
        (status_contrato = 'cancelado')
        """
    )

    op.create_unique_constraint('uq_contrato_id_proposta', 'contrato', ['id_proposta'])

    op.drop_column('contrato', 'id_evento')

def downgrade() -> None:
    """Downgrade schema."""

    op.drop_constraint('ck_contrato_valor_positivo', 'contrato', type_='check')

    op.drop_constraint('ck_contrato_status_contrato', 'contrato', type_='check')

    op.drop_constraint('ck_contrato_integridade_assinatura', 'contrato', type_='check')

    op.drop_constraint('uq_contrato_id_proposta', 'contrato', type_='unique')

    op.alter_column('contrato', 'status_contrato', existing_type=sa.String(length=100),
        existing_nullable=False, server_default=None
    )

    op.alter_column('contrato', 'status_contrato', new_column_name='status',
        existing_type=sa.String(length=100), existing_nullable=False       
    )

    op.add_column('contrato', sa.Column('id_evento', sa.Integer(), nullable=True))

    op.execute("""
        UPDATE contrato AS c
        SET id_evento = p.id_evento
        FROM proposta AS p
        WHERE c.id_proposta = p.id_proposta
    """)

    op.alter_column('contrato', 'id_evento', existing_type=sa.Integer(), 
        nullable=False
                    
    )

    op.create_foreign_key('contrato_id_evento_fkey', 'contrato', 'evento',
        ['id_evento'], ['id_evento']
    )

    