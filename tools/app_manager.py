# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
from smart.smart_printer import SmartPrinter
from tools.config import Config
from tools.gists_clone_master import GistsCloneMaster
from tools.repo_clone_master import RepoCloneMaster


class AppManager:
    def __init__(self):
        self.config = Config()
        self.smart_printer = SmartPrinter()
        self.gists_clone_master = GistsCloneMaster()
        self.repo_clone_master = RepoCloneMaster()