from db import make_session, User


async def create_user(tg_id, nickname):
    session = make_session()
    user = User(tg_id=tg_id, nickname=nickname)
    session.add(user)
    session.commit()
    session.close()
    return True
