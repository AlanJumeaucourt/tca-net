"""
    A logger util to manage verbosity and debug messages
"""


class Logger:
    def __init__(self, verbose=True) -> None:
        self.level = "INFO"
        self.verbose = verbose

    def __log(self, level, message) -> None:
        if self.verbose:
            print(f"#[TCA-NET {level} : {message}]")

    def info(self, message) -> None:
        self.__log("INFO", message)

    def warn(self, message) -> None:
        self.__log("WARNING", message)

    def error(self, message) -> None:
        self.__log("ERROR", message)
