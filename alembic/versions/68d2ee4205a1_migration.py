"""migration

Revision ID: 68d2ee4205a1
Revises: e56e5e7cfb3d
Create Date: 2023-05-07 13:23:56.361633

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68d2ee4205a1'
down_revision = 'e56e5e7cfb3d'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('chat', sa.Column('name', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('chat', 'name')
    # ### end Alembic commands ###
