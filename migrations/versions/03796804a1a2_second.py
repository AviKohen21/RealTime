"""second

Revision ID: 03796804a1a2
Revises: 715dd5682c54
Create Date: 2021-01-13 15:03:41.561244

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03796804a1a2'
down_revision = '715dd5682c54'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('counter', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_users_counter'), 'users', ['counter'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_counter'), table_name='users')
    op.drop_column('users', 'counter')
    # ### end Alembic commands ###
