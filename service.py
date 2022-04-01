from datetime import date, timedelta
from database.models import User, Favorite
from sqlalchemy.future import select
from database.connection import async_session
from sqlalchemy import delete
from aiohttp import ClientSession


class UserService:
  async def create_user(name: str):
    async with async_session() as session:
      session.add(User(name=name))
      await session.commit()

  async def delete_user(user_id: int):
    async with async_session() as session:
      await session.execute(delete(User).where(User.id==user_id))
      await session.commit()

  async def list_user():
    async with async_session() as session:
      result = await session.execute(select(User))
      return result.scalars().all()


class FavoriteService:
  async def add_favorite(user_id: int, symbol: str):
    async with async_session() as session:
      session.add(Favorite(user_id=user_id, symbol=symbol))
      await session.commit()

  async def delete_favorite(user_id: int, symbol: str):
    async with async_session() as session:
      await session.execute(delete(Favorite).where(
        Favorite.user_id==user_id, Favorite.symbol==symbol
        )
      )
      await session.commit()

class AssetService:
  async def day_summary(symbol: str):
    async with ClientSession() as session:
      yesterday = date.today() - timedelta(days=1)
      url = f"https://www.mercadobitcoin.net/api/{symbol.upper()}/day-summary/{yesterday.year}/{yesterday.month}/{yesterday.day}"
      response = await session.get(url)
      data = await response.json()
      return {
        "highest": data['highest'],
        "lowest": data['lowest'],
        "symbol": symbol
      }
