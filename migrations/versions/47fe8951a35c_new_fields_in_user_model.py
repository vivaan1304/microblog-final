"""new fields in user model

Revision ID: 47fe8951a35c
Revises: 6cd127f0337a
Create Date: 2021-07-27 20:05:03.241563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47fe8951a35c'
down_revision = '6cd127f0337a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
