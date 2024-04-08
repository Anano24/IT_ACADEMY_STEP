# დავალება 3.

# დაწერეთ ასინქრონული ფუნქცია, დააბრუნებს ატრიბუტად გადაწოდებული რიცხვის კვადრატს, იმ შემთხვევაში თუ ეს რიცხვი 
# არის ლუწი, ამის შესამოწმებლად დაწერეთ მეორე ასინქრონული ფუნქცია. შესამოწმებლად შექმენით რამდენიმე თასქი, გამოიყენეთ
# gather მეთოდი


import asyncio
import random



# Asynchronous function to calculate the square of a number
async def square(num):
    # Check if the number is even
    if not await is_even(num):
        return f"{num} is not even!"
    return f"{num} square is {num * num}"


# Asynchronous function to check if a number is even
async def is_even(num):
    return num % 2 == 0



# Asynchronous main function
async def main():
    tasks = []

    # Generate 5 random numbers and create tasks to calculate their squares
    for _ in range(5):
        num = random.randint(1, 10)
        tasks.append(square(num))

    # Execute all tasks concurrently
    results = await asyncio.gather(*tasks)
    for result in results:
        print(result)



if __name__ == "__main__":
    asyncio.run(main())
