# დავალება 2.

# დაწერეთ ფუნქცია, რომელსაც ატრიბუტად გადაეცემა რიცხვებისგან შემდგარი Queue, 
# ფუნქციამ უნდა დაბეჭდოს ნაკადის სახელი, რიგიდან ამოღებული მნიშვნელობა და არის თუ არა ეს რიცხვი ლუწი.
# გაუშვით სამი ნაკადი(thread) და მხოლოდ ამის შემდეგ შეავსეთ რიგი(queue). საბოლოოდ დააჯოინეთ და დაბეჭდეთ
# რომ ყველა ამოცანა შესრულებულია.


import threading
from queue import Queue
import random


# Function to generate random numbers
def generate_random_numbers(num):
    return [random.randint(1, 11) for _ in range(num)]


# Function for each worker thread
def worker(thread_id, number_queue):
    while True:
        number = number_queue.get()

        if number == None:
            break

        even = number % 2 == 0

        print(f"Thread: {thread_id}, Number: {number}, Even: {even}")
        number_queue.task_done()



def main():
    numbers = generate_random_numbers(10)
    num_threads = 3

    queue = Queue()
    

    threads = []
    # Create and start worker threads
    for i in range(num_threads):
        thread = threading.Thread(target=worker, args=(i, queue))
        thread.start()
        threads.append(thread)
    

    # Add numbers to the queue
    for number in numbers:
        queue.put(number)


    # Add termination signal to the queue
    for _ in range(num_threads):
        queue.put(None)


    # Wait for all threads to finish
    for thread in threads:
        thread.join()


    print("All tasks done")



if __name__ == "__main__":
    main()



