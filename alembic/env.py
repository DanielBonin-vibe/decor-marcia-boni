from logging.config import fileConfig

from sqlalchemy import engine_from_config
from sqlalchemy import pool

from alembic import context

from app.core.database import Base, DATABASE_URL

from app.models.cliente import Cliente
from app.models.contrato import Contrato
from app.models.documento import Documento
from app.models.evento import Evento
from app.models.item_proposta import ItemProposta
from app.models.pagamento import Pagamento
from app.models.parcela import Parcela
from app.models.proposta import Proposta
from app.models.recibo import Recibo
from app.models.usuario import Usuario


# Configuração do Alembic
config = context.config

# Usa a mesma URL do banco definida no database.py
# O replace é necessário porque o Alembic/configparser
# interpreta o caractere % de forma especial.
config.set_main_option(
    "sqlalchemy.url",
    DATABASE_URL.replace("%", "%%")
)

# Configuração de logs
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata dos models para o autogenerate
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Executa migrations no modo offline."""

    url = config.get_main_option("sqlalchemy.url")

    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Executa migrations no modo online."""

    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()