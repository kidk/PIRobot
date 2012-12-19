__author__ = 'Samuel'

from multiprocessing import Process, Queue, Pipe
from Services import WebService

if __name__ == '__main__':
    messageQueue = Queue()
    imagePipeReceiver, imagePipeSender = Pipe()

    # Start webserver
    webService = WebService.WebServer(messageQueue, imagePipeReceiver)
    webService.start()

