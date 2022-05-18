from motor.motor_asyncio import AsyncIOMotorClient


async def get_wikidataDb():
    db = AsyncIOMotorClient()
    scrap = db.scrap
    wikidataDb = scrap.website
    return wikidataDb
