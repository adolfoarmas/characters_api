"""Initial migration

Revision ID: d4eb7d8e448e
Revises: 79132f5bfd93
Create Date: 2024-09-19 23:40:48.373386

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd4eb7d8e448e'
down_revision: Union[str, None] = '79132f5bfd93'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
