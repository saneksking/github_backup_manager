# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2024, A.A. Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab
# --------------------------------------------------------
import argparse
import os
from dotenv import load_dotenv

from tools.app_manager import AppManager
from tools.github_api_man import GitHubAPI
from tools.archive_man import ArchiveTolls


def main():
    app_manager = AppManager()

    load_dotenv()
    token = os.getenv("GITHUB_API_TOKEN")
    name = os.getenv("GITHUB_NAME")

    parser = argparse.ArgumentParser(description=app_manager.config.name)
    parser.add_argument('-a', action='store_true', help='Auto', default=False)
    parser.add_argument('-g', action='store_true', help='Download gists', default=False)
    parser.add_argument('-r', action='store_true', help='Download repos', default=False)
    # parser.add_argument('-gr', action='store_true', help='Download gists and repos', default=False)
    # parser.add_argument('-rg', action='store_true', help='Download repos and gists', default=False)
    args = parser.parse_args()
    auto = args.a
    gists = args.g
    repos = args.r
    # gists_repos = args.gr
    # repos_gists = args.rg

    app_manager.smart_printer.show_head(text='Gists Backup Tool')

    print('Please wait...')

    github_api_manager_gists = GitHubAPI(
        name=name,
        token=token
    )
    github_api_manager_repos = GitHubAPI(
        name=name,
        token=token,
        url='https://api.github.com/user/repos'
    )

    if gists:
        gists = github_api_manager_gists.get_names()
        print(f'Name: {github_api_manager_gists.name} | Gists: {len(gists)}')

        if auto:
            app_manager.gists_clone_master.clone_gist(gists=gists, auto=True)
        elif not auto:
            app_manager.gists_clone_master.clone_gist(gists=gists)
    elif repos:
        repos = github_api_manager_repos.get_names()
        if auto:
            app_manager.repo_clone_master.clone_repo(repos=repos, auto=True)
        elif not auto:
            app_manager.repo_clone_master.clone_repo(repos=repos)
    else:
        gists = github_api_manager_gists.get_names()
        repos = github_api_manager_repos.get_names()
        if auto:
            app_manager.gists_clone_master.clone_gist(gists=gists, auto=True)
            print(f'Name: {github_api_manager_repos.name} | Repos: {len(repos)}')
            app_manager.repo_clone_master.clone_repo(repos=repos, auto=True)
            print(f'Name: {github_api_manager_repos.name} | Repos: {len(repos)}')
        elif not auto:
            app_manager.gists_clone_master.clone_gist(gists=gists)
            app_manager.repo_clone_master.clone_repo(repos=repos)
    archive = ArchiveTolls()
    archive.archive()
    app_manager.smart_printer.show_footer(url=app_manager.config.url, copyright_=app_manager.config.copyright_)


if __name__ == '__main__':
    main()
