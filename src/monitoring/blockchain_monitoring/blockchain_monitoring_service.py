# src/monitoring/blockchain_monitoring/blockchain_monitoring_service.py

from typing import List
from .evm_monitor import EVMMonitor
# from .stellar_monitor import StellarMonitor  # to add later
# from .starknet_monitor import StarknetMonitor  # to add later
# from .stacks_monitor import StacksMonitor  # to add later

class BlockchainMonitoringService:
    """
    Orchestrates deposit monitoring across multiple blockchains.
    """

    def __init__(self):
        # Initialize monitors for each chain
        self.monitors: List = []
        self.monitors.append(EVMMonitor(network="polygon"))
        # self.monitors.append(StellarMonitor())
        # self.monitors.append(StarknetMonitor())
        # self.monitors.append(StacksMonitor())

    def start(self):
        """
        Start all chain monitors.
        """
        for monitor in self.monitors:
            monitor.start()

    def stop(self):
        """
        Stop all chain monitors.
        """
        for monitor in self.monitors:
            monitor.stop()
