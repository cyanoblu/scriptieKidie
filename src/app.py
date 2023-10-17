import logging
from modules.automation.sneakPeekSlayer import SneakPeekSlayer as slayer
from modules.automation.lazyStarter import LazyStarter as lazy

logger = logging.getLogger()
logger.setLevel(logging.INFO)
# create file handler which logs even debug messages
fh = logging.FileHandler("app.log")
fh.setLevel(logging.INFO)
# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
# create formatter and add it to the handlers
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
fh.setFormatter(formatter)
ch.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(fh)
logger.addHandler(ch)


class App:
    sps = slayer()
    lz = lazy()

    def run(self):
        self.lz.run()
        self.sps.ripAndTear()


if __name__ == "__main__":
    logging.info("initializing...")
    app = App()
    app.run()
    logging.info("end of process")
