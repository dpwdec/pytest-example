from database import Session, Base, db
from user.model import User

Base.metadata.create_all(db)
session = Session()
# BaseModel.set_session(session)

# User(name="Jimothy", age=10).save()
# session.commit()

# for user in session.query(User)\
#     .filter_by(name="Alan")\
#     .filter_by(age=105):
#     print(user.name)

for user in session.query(User).filter(User.age > 100):
    print(user.name)

# g_user = User(name="Gedothy", age=20)
# session.add(g_user)
# session.commit()
# a_user = User(name="Alan", age=105)
# session.add(a_user)
# session.commit()

# print(session.query(User)[0].name)

# for name, age in session.query(User.name, User.age):
#     print(name)
#     print(age)

# for user in session.query(User):
#     print(user.name)