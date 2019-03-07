"""empty message

Revision ID: a431ae7d0b69
Revises: 993c8ee6b44c
Create Date: 2019-03-05 16:51:31.379883

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a431ae7d0b69'
down_revision = '993c8ee6b44c'
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
