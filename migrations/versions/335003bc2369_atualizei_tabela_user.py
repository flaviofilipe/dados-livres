"""atualizei tabela user

Revision ID: 335003bc2369
Revises: b3362ea95a51
Create Date: 2020-09-29 17:48:28.198363

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '335003bc2369'
down_revision = 'b3362ea95a51'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_user_nickname'), ['nickname'])
        batch_op.drop_index('ix_user_nickname')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.create_index('ix_user_nickname', ['nickname'], unique=1)
        batch_op.drop_constraint(batch_op.f('uq_user_nickname'), type_='unique')

    # ### end Alembic commands ###