import os

from concurrent import futures

from example17_2 import save_flag, get_flag, show, main
from example17_3 import download_one


def download_many(cc_list):
    cc_list = cc_list[:5]
    print('os.cpu_count()', os.cpu_count())
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        to_do = []
        for cc in sorted(cc_list):
            future = executor.submit(download_one, cc)
            to_do.append(future)
            msg = 'Scheduled for {}: {}'
            print(msg.format(cc, future))

        results = []
        for future in futures.as_completed(to_do):
            res = future.result()
            msg = '{} result: {!r}'
            print(msg.format(future, res))
            results.append(res)

    return len(results)


if __name__ == '__main__':
    main(download_many)

