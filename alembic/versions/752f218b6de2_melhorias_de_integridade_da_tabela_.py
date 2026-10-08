"""Melhorias de integridade da tabela cliente.

Revision ID: 752f218b6de2
Revises: 753af9d88168
Create Date: 2026-10-08 11:20:21.702412

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '752f218b6de2'
down_revision: Union[str, Sequence[str], None] = '753af9d88168'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.alter_column('cliente', 'ativo', existing_type=sa.Boolean(),
        existing_nullable=False, server_default=sa.text('true')
    )

    op.alter_column('cliente', 'estado', existing_type=sa.String(length=150),
        type_=sa.String(length=2), existing_nullable=False
    )

    op.create_check_constraint('ck_cliente_cpf_formato', 
        'cliente', "cpf ~ '^[0-9]{11}$'"
    )

    op.create_check_constraint('ck_cliente_cep_formato', 
        'cliente', "cep ~ '^[0-9]{8}$'"                           
    )

    op.create_check_constraint('ck_cliente_estado_formato',
        'cliente', "ESTADO IN ('AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO')"
    )

    op.create_check_constraint('ck_cliente_telefone_formato',
        'cliente', "telefone ~ '^[0-9]{10,11}$'"                           
    )

    op.create_index('uq_cliente_email_lower',
        'cliente', [sa.text('LOWER(email)')], unique=True
        
    )

    op.execute("""
    CREATE OR REPLACE FUNCTION atualizar_data_cliente()
    RETURNS TRIGGER AS $$
    BEGIN
        NEW.data_atualizacao = CURRENT_TIMESTAMP;
        RETURN NEW;
    END;
    $$ LANGUAGE plpgsql;
""")

    op.execute("""
    CREATE TRIGGER trg_cliente_data_atualizacao
    BEFORE UPDATE ON cliente
    FOR EACH ROW
    EXECUTE FUNCTION atualizar_data_cliente();
""")


def downgrade() -> None:
    """Downgrade schema."""

    op.execute("""
        DROP TRIGGER trg_cliente_data_atualizacao ON cliente;
    """)

    op.execute("""
    DROP FUNCTION atualizar_data_cliente();
    """)

    op.drop_index(
        'uq_cliente_email_lower', table_name='cliente'
    )

    op.drop_constraint(
        'ck_cliente_cpf_formato', 'cliente', type_='check'
    )

    op.drop_constraint(
        'ck_cliente_cep_formato', 'cliente', type_='check'
    )

    op.drop_constraint(
        'ck_cliente_estado_formato', 'cliente', type_='check'
    )

    op.drop_constraint(
        'ck_cliente_telefone_formato', 'cliente', type_='check'
    )

    op.alter_column('cliente', 'estado', existing_type=sa.String(length=2),
        type_=sa.String(length=150), existing_nullable=False
    )

    op.alter_column('cliente', 'ativo', existing_type=sa.Boolean(),
        existing_nullable=False, server_default=None                
    )