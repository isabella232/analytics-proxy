"""empty message

Revision ID: 463d896e9f73
Revises: None
Create Date: 2014-11-14 13:50:51.223120

"""

# revision identifiers, used by Alembic.
revision = '463d896e9f73'
down_revision = None

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('proxies',
    sa.Column('endpoint', sa.String(), nullable=False),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('data', postgresql.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('endpoint'),
    sa.UniqueConstraint('url')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('proxies')
    ### end Alembic commands ###
