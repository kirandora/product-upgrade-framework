from handlers import OnpremUpgradeHandler, CloudUpgradeHandler


class UpgradeHandler:
    @classmethod
    def instantiate(cls, dep_type):
        if dep_type is "On-Prem":
            return OnpremUpgradeHandler()
        else:
            return CloudUpgradeHandler()
