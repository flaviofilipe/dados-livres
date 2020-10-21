"""update tagging

Revision ID: e01dba08123e
Revises: bb0cd63a5e4f
Create Date: 2020-10-20 00:21:27.218505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e01dba08123e'
down_revision = 'bb0cd63a5e4f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tag', schema=None) as batch_op:
        batch_op.drop_index('ix_tag_timestamp')
        batch_op.drop_column('timestamp')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tag', schema=None) as batch_op:
        batch_op.add_column(sa.Column('timestamp', sa.DATETIME(), nullable=True))
        batch_op.create_index('ix_tag_timestamp', ['timestamp'], unique=False)

    # ### end Alembic commands ###