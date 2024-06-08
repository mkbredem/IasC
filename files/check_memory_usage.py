# check_memory_usage.py
import psutil

def check_memory_usage():
    memory_info = psutil.virtual_memory()
    print(f"Total: {memory_info.total // (2**20)} MiB")
    print(f"Available: {memory_info.available // (2**20)} MiB")
    print(f"Used: {memory_info.used // (2**20)} MiB")
    print(f"Percentage: {memory_info.percent}%")

if __name__ == "__main__":
    check_memory_usage()
