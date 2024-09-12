#10. Exponential Backoff
# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries.

import time

wait_time = 1 # in seconds
max_retries = 5 # maximum 5 attempts
attempts = 0 # intialy 0

while attempts < max_retries:
    print(f'Attempt - {attempts + 1} and the Wait time - {wait_time}')
    time.sleep(wait_time)
    wait_time = wait_time * 2
    attempts = attempts + 1

print('Program End') #after 16s it will end and print this