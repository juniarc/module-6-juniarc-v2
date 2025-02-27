"""edit enclosures table

Revision ID: add78c484407
Revises: 270a7d2c3987
Create Date: 2024-10-09 23:09:16.620622

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'add78c484407'
down_revision = '270a7d2c3987'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('feedings', schema=None) as batch_op:
        batch_op.alter_column('animal_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.alter_column('enclosure_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('feedings', schema=None) as batch_op:
        batch_op.alter_column('enclosure_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('animal_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###
