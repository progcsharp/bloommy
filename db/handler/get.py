from db import make_session, User


async def get_user_by_tg_id(tg_ig):
    session = make_session()
    user = session.query(User).filter(User.tg_id == tg_ig).first()
    session.close()
    if user:
        return False
    return True
