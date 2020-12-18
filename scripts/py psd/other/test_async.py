import asyncio

async def printValue(message, count):
    for i in range(count):
        print(f'{message}: {i}')
        await asyncio.sleep(1)

    print(f'done "{message}"')
    
async def main():
    one = asyncio.create_task(printValue('one', 5))
    two = asyncio.create_task(printValue('two', 3))
    await asyncio.gather(one, two)
    print('done main')

if __name__ == '__main__':
    asyncio.run(main())
    print('done entry')
