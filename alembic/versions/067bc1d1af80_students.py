"""Students

Revision ID: 067bc1d1af80
Revises: 75b071c93829
Create Date: 2023-01-15 17:59:32.253637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '067bc1d1af80'
down_revision = '75b071c93829'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=255), nullable=False),
    sa.Column('lastname', sa.String(length=255), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('students')
    # ### end Alembic commands ###
