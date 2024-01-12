"""empty message

Revision ID: 050e757a3749
Revises: 
Create Date: 2023-12-23 23:31:28.716963

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '050e757a3749'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('puppy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('users')
    op.drop_table('upload')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('upload',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('filename', sa.VARCHAR(length=50), nullable=True),
    sa.Column('data', sa.BLOB(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=250), nullable=False),
    sa.Column('password', sa.VARCHAR(length=250), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('password'),
    sa.UniqueConstraint('username')
    )
    op.drop_table('puppy')
    # ### end Alembic commands ###