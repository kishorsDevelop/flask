"""empty message

Revision ID: 4062f9e25c8b
Revises: 
Create Date: 2024-01-05 23:50:17.636364

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4062f9e25c8b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('puppy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('owner',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('pup_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['pup_id'], ['puppy.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('owner')
    op.drop_table('puppy')
    # ### end Alembic commands ###
