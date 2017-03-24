#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 线程和进程，线程可以改变全局变量的值，进程可以通过一些手段进行资源共享
# 线程池和进程池的实现

import multiprocessing
import threading
import time

# 线程池
thread_pool = threading.Semaphore(3)


def test_thread(cur_num):
    try:
        print cur_num
        time.sleep(3)
    finally:
        thread_pool.release()


def multi_thread():
    lst_thread = []
    for i in xrange(10):
        thread_pool.acquire()
        thread_instance = threading.Thread(target=test_thread, args=(i,))
        lst_thread.append(thread_instance)
        thread_instance.start()
        
    for instance in lst_thread:
        instance.join()
        
        
# 进程池
def test_process(cur_num):
        print cur_num
        time.sleep(3)


def multi_process():
    lst_process = []
    pool = multiprocessing.Pool(processes=3)
    
    for i in xrange(10):
        # 阻塞
        #pool.apply(test_process, args=(i,))
        # 非阻塞
        pool.apply_async(test_process, args=(i,))
    
    pool.close()
    pool.join()
        
if __name__ == '__main__':
    multi_process()
    