from .UpgradeHandler import UpgradeHandler


class UpgradeService:
    def __init__(self):
        self.upg_handler = UpgradeHandler.instantiate("On-Prem")

    def loop(self):
        # Perform Pretask
        self.upg_handler.pre_tasks()
        # Get Priority App list
        self.upg_handler.get_priority_list()
        # Perform Priority App Upgrade
        self.upg_handler.perform_priority_upgrade()
        # File download
        self.upg_handler.process_app_download()
        # Perform Other App Upgrade
        self.upg_handler.process_app_upgrade()


