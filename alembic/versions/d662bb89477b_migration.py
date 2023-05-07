"""migration

Revision ID: d662bb89477b
Revises: 68d2ee4205a1
Create Date: 2023-05-07 13:44:56.820456

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd662bb89477b'
down_revision = '68d2ee4205a1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('message', sa.Column('sender_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'message', 'user', ['sender_id'], ['id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'message', type_='foreignkey')
    op.drop_column('message', 'sender_id')
    # ### end Alembic commands ###