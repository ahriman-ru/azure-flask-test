"""empty message

Revision ID: 913403b41a5e
Revises: None
Create Date: 2017-01-27 18:21:37.565000

"""

# revision identifiers, used by Alembic.
revision = '913403b41a5e'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('chat_id', sa.String(length=64), nullable=False),
    sa.Column('login', sa.String(length=64), nullable=False),
    sa.Column('token', sa.String(length=12), nullable=True),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_index(op.f('ix_users_chat_id'), 'users', ['chat_id'], unique=True)
    op.create_index(op.f('ix_users_login'), 'users', ['login'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_login'), table_name='users')
    op.drop_index(op.f('ix_users_chat_id'), table_name='users')
    op.drop_table('users')
    ### end Alembic commands ###
