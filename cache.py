# Hruday Natakam - 201763048
# The capacity of the cache is 8 pages.
# Global scope variables
cache = []
requests = []

# Function to run FIFO cache memory algorithm
def fifo():
    global cache
    for page in requests:
        if page in cache:
            print("Hit")
        else:
            print("Miss", end=" ")
            if len(cache) == 8:
                evicted_page = cache.pop(0)
                print(f"- Evict {evicted_page},", end=" ")
            print(f"Adding {page} to Cache")
            if page not in cache:
                cache.append(page)

# Function to run LFU cache memory algorithm
def lfu():
    global cache
    page_count = {}
    for page in requests:
        if page in cache:
            print("Hit")
            page_count[page] += 1
        else:
            print("Miss - Evicting", min(page_count, key=page_count.get, default=page), "Adding", page, "to Cache")
            if len(cache) == 8:
                evict_page = min(page_count, key=page_count.get, default=page)
                cache.remove(evict_page)
                del page_count[evict_page]
            cache.append(page)
            page_count[page] = 1

# Main program
while True:
    print("\nEnter page requests (enter 0 to stop):")
    while True:
        page = int(input())
        if page == 0:
            break
        requests.append(page)

    print("\nChoose cache eviction algorithm:")
    print("1. FIFO")
    print("2. LFU")
    print("Q. Quit")

    choice = input().upper()

    if choice == '1':
        fifo()
    elif choice == '2':
        lfu()
    elif choice == 'Q':
        break

    print("\nFinal state of cache:", cache)
    cache = []
    requests = []
