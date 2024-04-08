# დავალება 1.

# დაწერეთ ორი ასინქრონული ფუნქცია, ერთ-ერთი დააყოვნეთ 2 წამი, მეორე 5 წამი, დაბეჭდეთ მათი დაწყება და დასრულება,
# თასქები შექმენით ცალ-ცალკე და გაუშვით.

import time
import asyncio


async def walking():
    print("Start walking!")
    await asyncio.sleep(2)
    print("Finished walking")



async def driving():
    print("Start driving!")
    await asyncio.sleep(5)
    print("Finished driving")



async def main():
    start_time = time.time()

    walking_taks = asyncio.create_task(walking()) 
    driving_task = asyncio.create_task(driving()) 

    await walking_taks
    await driving_task

    end_time = time.time()

    elapsed_time = start_time - end_time
    print(f"Elapsed time: {elapsed_time:.2f} seconds")


if __name__ == "__main__":
    asyncio.run(main()) 

