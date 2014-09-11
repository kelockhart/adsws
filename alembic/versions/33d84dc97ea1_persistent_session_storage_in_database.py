"""persistent session storage in database

Revision ID: 33d84dc97ea1
Revises: 51f3b3b5cd5d
Create Date: 2014-09-09 11:30:32.615000

"""

# revision identifiers, used by Alembic.
revision = '33d84dc97ea1'
down_revision = '51f3b3b5cd5d'

from alembic import op
import sqlalchemy as db


def upgrade():
    op.create_table('session',

def downgrade():
    op.drop_table('session')