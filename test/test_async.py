class AsyncContextManager:
    async def __aenter__(self):
        return self
    async def __aexit__(self, exc_type, exc, tb):
        pass

mock_instance = MagicMock(AsyncContextManager())  # AsyncMock also works here
async def main():
    async with mock_instance as result:
        pass

asyncio.run(main())
mock_instance.__aenter__.assert_awaited_once()
mock_instance.__aexit__.assert_awaited_once()