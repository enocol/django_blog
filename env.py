import os

os.environ.setdefault("DATABASE_URL",  "postgresql://neondb_owner:npg_mTJOzXVn1kt4@ep-bitter-mud-a2g3b5ng.eu-central-1.aws.neon.tech/fox_dock_frill_839343")

print(f"DATABASE_URL in env.py: {os.environ.get('DATABASE_URL')}")