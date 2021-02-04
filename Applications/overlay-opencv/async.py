import asyncio
import keyboard

async def get_key(key):
  while True:
    if keyboard.is_pressed(key):
      print(key)
    await asyncio.sleep(0.1)

async def main():
  task_one = asyncio.create_task(get_key("q"))
  task_two = asyncio.create_task(get_key("w"))
  
  # try:
  #   k = 1 / 0
  # except Exception as e:
  #   print("ERROR!", e)
  
  await asyncio.gather(task_one, task_two)

if __name__ == "__main__":
    asyncio.run(main())