"""empty message

Revision ID: c76f74f6ea89
Revises: 
Create Date: 2024-10-30 00:06:24.913267

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c76f74f6ea89'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    pass
def downgrade() -> None:
    pass