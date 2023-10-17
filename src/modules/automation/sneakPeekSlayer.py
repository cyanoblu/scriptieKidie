""" .________.______  ._______.______  .____/\      ._______ ._______._______.____/\      .________.___    .______   ____   ____._______.______  
|    ___/:      \ : .____/:      \ :   /  \     : ____  |: .____/: .____/:   /  \     |    ___/|   |   :      \  \   \_/   /: .____/: __   \ 
|___    \|       || : _/\ |   .   ||.  ___/     |    :  || : _/\ | : _/\ |.  ___/     |___    \|   |   |   .   |  \___ ___/ | : _/\ |  \____|
|       /|   |   ||   /  \|   :   ||     \      |   |___||   /  \|   /  \|     \      |       /|   |/\ |   :   |    |   |   |   /  \|   :  \ 
|__:___/ |___|   ||_.: __/|___|   ||      \     |___|    |_.: __/|_.: __/|      \     |__:___/ |   /  \|___|   |    |___|   |_.: __/|   |___\
   :         |___|   :/       |___||___\  /                 :/      :/   |___\  /        :     |______/    |___|               :/   |___|    
                                        \/                                    \/                                                              """
import subprocess, schedule, time, logging
from . import slayerWarnings as sw
from win10toast import ToastNotifier
from random import randint


class SneakPeekSlayer:
    # Detects demons invading personal space through uvnc and similars
    # Assumes standard port :5900 being used
    toaster = ToastNotifier()
    warnings = sw.SlayerWarnings()

    def peekChecker(self):
        warnings = self.warnings
        # Checks port status for uvnc connection, notify user in case of detection
        try:
            subprocess.check_output(
                'netstat -an | find "ESTABLISHED" | find ":5900"', shell=True, text=True
            )

            self.toaster.show_toast(
                "Peek Detected!",
                warnings.detectionWarnings[randint(0, 9)],
                icon_path="./src/assets/slayer.ico",
                duration=5,
                threaded=True,
            )

            logging.warning(
                f"PEEK DETECTED! {warnings.detectionWarnings[randint(0, 9)]}"
            )
        except subprocess.CalledProcessError:
            logging.info(f"All clear... {warnings.clearWarnings[randint(0, 9)]}")
        except Exception as e:
            logging.error(f"{warnings.errorWarnings[randint(0, 9)]} {e}")

    def ripAndTear(self):
        warnings = self.warnings
        logging.info(warnings.initWarnings[randint(0, 9)])
        # Schedule and checks for peeks once a minute
        try:
            schedule.every(1).minutes.do(self.peekChecker)
        except Exception as e:
            logging.error(f"{warnings.errorWarnings[randint(0, 9)]} {e}")

        while True:
            schedule.run_pending()
            time.sleep(1)
