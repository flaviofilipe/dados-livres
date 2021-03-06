"""update tables

Revision ID: 99ed7135dcc3
Revises: 14ae4890a500
Create Date: 2020-07-15 16:42:30.123713

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99ed7135dcc3'
down_revision = '14ae4890a500'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.drop_column('language')

    with op.batch_alter_table('similar', schema=None) as batch_op:
        batch_op.add_column(sa.Column('softwareSimilare_id', sa.Integer(), nullable=True))
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_similar_softwareSimilare_id_software'), 'software', ['softwareSimilare_id'], ['id'])
        batch_op.drop_column('softwarSimilare_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('similar', schema=None) as batch_op:
        batch_op.add_column(sa.Column('softwarSimilare_id', sa.INTEGER(), nullable=True))
        batch_op.drop_constraint(batch_op.f('fk_similar_softwareSimilare_id_software'), type_='foreignkey')
        batch_op.create_foreign_key(None, 'software', ['softwarSimilare_id'], ['id'])
        batch_op.drop_column('softwareSimilare_id')

    with op.batch_alter_table('post', schema=None) as batch_op:
        batch_op.add_column(sa.Column('language', sa.VARCHAR(length=5), nullable=True))

    # ### end Alembic commands ###
