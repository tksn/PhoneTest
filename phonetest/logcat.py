import subprocess
import threading
import locale
import re
import functools
import phonetest.exception

class _LogcatWatcherThread(threading.Thread):

    """
    """

    ADB_COMMAND = ['adb', 'logcat']

    def __init__(self):
        threading.Thread.__init__(self)
        self.callbacks = []
        self.process = subprocess.Popen(self.ADB_COMMAND, stdout=subprocess.PIPE)
        self.started_event = threading.Event()

    def add_callback(self, callback):
        self.callbacks.append(callback)

    def run(self):
        self.started_event.set()
        for line in iter(self.process.stdout.readline, b''):
            line_str = line.decode(locale.getpreferredencoding())
            for cb in self.callbacks:
                cb(line_str)

    def stop(self):
        self.started_event.wait()
        self.process.kill()
        self.process.communicate()
        threading.Thread.join(self)


class LogcatWatcher(object):

    def __init__(self):
        self.lock = threading.Lock()
        self.errors = {}
        self.thread = _LogcatWatcherThread()

        def fatal_error_callback(line):
            if re.search(r'FATAL EXCEPTION', line):
                with self.lock:
                     self.errors['FATAL EXCEPTION'] = line

        self.thread.add_callback(fatal_error_callback)
        self.thread.start()

    def stop(self):
        self.thread.stop()

    def check_errors(self, context_str):
        with self.lock:
            fatal = self.errors.get('FATAL EXCEPTION')
            if fatal:
                raise phonetest.exception.PhonetestException(
                    '[{0}]Found fatal error in logcat log - {1}'.format(context_str, fatal))


logcat_watcher = None


def start_logcat_watcher():
    global logcat_watcher
    logcat_watcher = LogcatWatcher()


def stop_logcat_watcher():
    global logcat_watcher
    logcat_watcher.stop()


def with_logcat_check(method):
    @functools.wraps(method)
    def wrapped_func(*args, **kwargs):
        logcat_watcher.check_errors('pre_op')
        method(*args, **kwargs)
        logcat_watcher.check_errors('post_op')
    return wrapped_func