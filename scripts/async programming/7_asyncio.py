import asyncio

# python 3.4
# @asyncio.coroutine # decorator
# def smth():
#    pass
#    yield from asyncio.sleep(1)

# python 3.6
# ensure_future -> create_task

async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(1)

async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print('{} elapsed seconds'.format(count))
        count += 1
        await asyncio.sleep(1)

async def main():
    task_one = asyncio.create_task(print_nums())
    task_two = asyncio.create_task(print_time())

    await asyncio.gather(task_one, task_two)

if __name__ == '__main__':
    #loop = asyncio.get_event_loop()
    #loop.run_until_complete(main())
    #loop.close()
    
    # python 3.7
    asyncio.run(main())
