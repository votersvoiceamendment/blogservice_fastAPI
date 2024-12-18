"""Post featured NOT nullable

Revision ID: 02adc4472a91
Revises: cc3856fa4dbf
Create Date: 2024-11-11 14:18:40.437378

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '02adc4472a91'
down_revision: Union[str, None] = 'cc3856fa4dbf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('post', 'featured',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('post', 'featured',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###
