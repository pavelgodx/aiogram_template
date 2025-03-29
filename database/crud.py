from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.models import UserModel


async def create_new_user(
        session: AsyncSession,
        telegram_id: int,
        username: str,
        full_name: str,
        is_premium: bool = False,
) -> UserModel:
    result = await session.execute(
        select(UserModel).where(UserModel.telegram_id == telegram_id)
    )
    user = result.scalar_one_or_none()

    if user is None:
        user = UserModel(
            telegram_id=telegram_id,
            username=username,
            full_name=full_name,
            is_premium=is_premium,
        )
        session.add(user)
        await session.commit()
        await session.refresh(user)

    return user
