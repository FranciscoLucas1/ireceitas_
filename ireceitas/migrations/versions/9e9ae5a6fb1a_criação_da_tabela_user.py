"""Criação da tabela User

Revision ID: 9e9ae5a6fb1a
Revises: 
Create Date: 2021-10-28 17:31:46.312956

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e9ae5a6fb1a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=70), nullable=False),
    sa.Column('email', sa.String(length=70), nullable=False),
    sa.Column('password', sa.String(length=2048), nullable=False),
    sa.Column('sobre', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user')),
    sa.UniqueConstraint('email', name=op.f('uq_user_email'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
