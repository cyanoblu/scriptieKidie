import logging, os


class LazyStarter:
    # Auto opens main apps used daily at work
    def run(self):
        logging.info("Opening main apps...")

        logging.info("Initializing chrome...")
        os.startfile("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe")

        logging.info("Initializing outlook...")
        os.startfile(
            "C:/Program Files (x86)/Microsoft Office/root/Office16/OUTLOOK.EXE"
        )

        logging.info("Initializing spark...")
        os.startfile("C:/Program Files (x86)/Spark/Spark.exe")

        logging.info("Initializing VS Code...")
        os.startfile("C:/Users/brito/AppData/Local/Programs/Microsoft VS Code/Code.exe")

        logging.info("Done.")
