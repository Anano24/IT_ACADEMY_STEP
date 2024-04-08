# დავალება 2.

# დაწერეთ ასინქრონული ფუნქცია, რომელიც რენდომად არჩეული დროით დააყოვნებს და დაბეჭდავს
# რიცხვებს 1-დან 10-მდე


import asyncio
import random
import time


# defines an asynchronous function that prints numbers with random delays
async def task(n, delay):
    print(f"Started {n}")
    start_time = time.time()

    await asyncio.sleep(delay)

    end_time = time.time()
    print(f"Finished {n} in {end_time - start_time:.2f} Seconds")


# Asynchronous main function
async def main():
    tasks = []

    for i in range(1, 11):
        delay = random.randint(1, 6)
        num = i
        tasks.append(task(num, delay))
    
    all_tasks = asyncio.gather(*tasks)
    await all_tasks



if __name__ == "__main__":
    asyncio.run(main())