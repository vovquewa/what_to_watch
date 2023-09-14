"""added added_by field

Revision ID: 0bcde9aa53d7
Revises: 
Create Date: 2023-09-12 17:47:49.821636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0bcde9aa53d7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('opinion', sa.Column('added_by', sa.String(length=64), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('opinion', 'added_by')
    # ### end Alembic commands ###
