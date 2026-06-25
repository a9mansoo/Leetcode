


class LogRateLimiter:

    def __init__(self):
        self.log_stream = {}
        self.limit_sec = 10

    def _check_timestamp(self, old_timestamp, new_timestamp):
        if (new_timestamp - old_timestamp) < 10:
            return False
        return True

    def shouldPrintMessage(self, timestamp, message):
        if message not in self.log_stream:
            self.log_stream[message] = timestamp
            return True
        
        can_print = self._check_timestamp(self.log_stream.get(message), timestamp)
        if can_print:
            self.log_stream[message] = timestamp
            return True
        return False


logger = LogRateLimiter()

print(logger.shouldPrintMessage(1, "foo"))

print(logger.shouldPrintMessage(2,"bar"))

print(logger.shouldPrintMessage(3,"foo"))

print(logger.shouldPrintMessage(8,"bar"))

print(logger.shouldPrintMessage(10,"foo"))

print(logger.shouldPrintMessage(11,"foo"))