import h1don
import concurrent.futures

if __name__ == "__main__":
    mstdn = h1don.h1don()
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)
    executor.submit(mstdn.get_LTL_stream())
    executor.submit(mstdn.heartbeat_check())