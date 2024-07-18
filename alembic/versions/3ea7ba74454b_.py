"""empty message

Revision ID: 3ea7ba74454b
Revises: 4b2fc0bc15b9
Create Date: 2024-07-18 23:44:39.163916

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = '3ea7ba74454b'
down_revision: Union[str, None] = '4b2fc0bc15b9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blogpostmodel', schema=None) as batch_op:
        batch_op.add_column(sa.Column('publish_active', sa.Boolean(), server_default=sa.text('0'), nullable=False))
        batch_op.drop_column('publish_activ')

    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('blogpostmodel', schema=None) as batch_op:
        batch_op.add_column(sa.Column('publish_activ', sa.BOOLEAN(), nullable=False))
        batch_op.drop_column('publish_active')

    # ### end Alembic commands ###