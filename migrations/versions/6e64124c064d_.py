"""empty message

Revision ID: 6e64124c064d
Revises: 08bc20ca41e3
Create Date: 2019-03-05 18:39:25.413177

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6e64124c064d'
down_revision = '08bc20ca41e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('areas_ibfk_1', 'areas', type_='foreignkey')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('areas_ibfk_1', 'areas', 'areas', ['pid'], ['id'])
    # ### end Alembic commands ###