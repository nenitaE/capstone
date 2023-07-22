from app.models import db, Role, environment, SCHEMA
from sqlalchemy.sql import text


# Adds a demo user, you can add other users here if you want
def seed_roles():
    role1 = Role(
        name='clinician'
        ),
    role2 = Role(
        name='patient'
        )

    db.session.add(role1)
    db.session.add(role2)
    db.session.commit()


# Uses a raw SQL query to TRUNCATE or DELETE the roles table. SQLAlchemy doesn't
# have a built in function to do this. With postgres in production TRUNCATE
# removes all the data from the table, and RESET IDENTITY resets the auto
# incrementing primary key, CASCADE deletes any dependent entities.  With
# sqlite3 in development you need to instead use DELETE to remove all data and
# it will reset the primary keys for you as well.
def undo_roles():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.roles RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM roles"))
        
    db.session.commit()