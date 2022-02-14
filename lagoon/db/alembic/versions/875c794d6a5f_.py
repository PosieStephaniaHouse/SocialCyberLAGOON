"""empty message

Revision ID: 875c794d6a5f
Revises: 7d51ac305f89
Create Date: 2022-02-11 14:11:19.438883

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '875c794d6a5f'
down_revision = '7d51ac305f89'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('attrs_base', 'super_type',
               existing_type=sa.VARCHAR(length=14),
               type_=sa.Enum('computed_attrs', 'entity', 'observation', name='supertypeenum', native_enum=False),
               existing_nullable=False)
    op.alter_column('cache_fused_entity', 'name',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.String(),
               existing_nullable=False)
    op.alter_column('cache_fused_entity', 'type',
               existing_type=sa.VARCHAR(length=10),
               type_=sa.Enum('file', 'git_commit', 'git_pullrequest', 'message', 'pep', 'person', name='entitytypeenum', native_enum=False),
               existing_nullable=False)
    op.alter_column('cache_fused_observation', 'type',
               existing_type=sa.VARCHAR(length=13),
               type_=sa.Enum('attached_to', 'committed', 'created', 'message_cc', 'message_from', 'message_ref', 'message_to', 'modified', 'superseded_by', 'requires', name='observationtypeenum', native_enum=False),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('cache_fused_observation', 'type',
               existing_type=sa.Enum('attached_to', 'committed', 'created', 'message_cc', 'message_from', 'message_ref', 'message_to', 'modified', 'superseded_by', 'requires', name='observationtypeenum', native_enum=False),
               type_=sa.VARCHAR(length=13),
               existing_nullable=False)
    op.alter_column('cache_fused_entity', 'name',
               existing_type=sa.String(),
               type_=sa.VARCHAR(length=65535),  # Manual dummy value
               existing_nullable=False)
    op.alter_column('cache_fused_entity', 'type',
               existing_type=sa.Enum('file', 'git_commit', 'git_pullrequest', 'message', 'pep', 'person', name='entitytypeenum', native_enum=False),
               type_=sa.VARCHAR(length=10),
               existing_nullable=False)
    op.alter_column('attrs_base', 'super_type',
               existing_type=sa.Enum('computed_attrs', 'entity', 'observation', name='supertypeenum', native_enum=False),
               type_=sa.VARCHAR(length=14),
               existing_nullable=False)
    # ### end Alembic commands ###
