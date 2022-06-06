from motor.motor_asyncio import AsyncIOMotorClient


class motor_c:
    def __init__(self) -> None:
        db = AsyncIOMotorClient()
        scrap = db.scrap
        self.scrap =scrap
    async def get_wikidataDb(self):
        return self.scrap.wikidataDb
    async def get_ResourceDiscovery(self):
        return self.scrap.db
    async def get_robots(self):
        return self.scrap.robots
    async def get_dns(self):
        return self.scrap.DNS
