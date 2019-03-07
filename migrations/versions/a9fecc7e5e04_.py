"""empty message

Revision ID: a9fecc7e5e04
Revises: 6e64124c064d
Create Date: 2019-03-05 20:58:28.163355

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9fecc7e5e04'
down_revision = '6e64124c064d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'areas', 'areas', ['pid'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'areas', type_='foreignkey')
    # ### end Alembic commands ###