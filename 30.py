def prime_generator(limit):
    for num in range(2, limit + 1):
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num

print("Primes up to 30:")
for prime in prime_generator(30):
    print(prime, end=" ")
print()

print()

def character_stream(text):
    for ch in text:
        if ch.isalnum():
            yield ch.upper()

stream = "".join(character_stream("python 3.12 is cool!"))
print("Alphanumeric uppercase stream:", stream)

print()

class StepRange:
    def __init__(self, start, end, step=1):
        self.current = start
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        val = self.current
        self.current = self.current + self.step
        return val

print("Custom StepRange (1 to 20 step 3):")
for val in StepRange(1, 20, 3):
    print(val, end=" ")
print()
