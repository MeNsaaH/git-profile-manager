import setuptools
from setuptools.command.install import install
from git_profile_manager.__version__ import __version__
from git_profile_manager import utils

REQUIRED_PYTHON = (3, 0)

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        # Setup git-profile-manager
        utils.setup()

setuptools.setup(
    name="git-profile-manager",
    version=__version__,
    author='Mmadu Manasseh',
    author_email="mmadumanasseh@gmail.com",
    description="A git extension to allow you manage multiple git profiles on your workstation",
    url="https://github.com/MeNsaaH/git-profile-manager",
    project_urls={
        "Source": "https://github.com/MeNsaaH/git-profile-manager",
    },
    packages=setuptools.find_packages(),
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    license="MIT",
    cmdclass={
        'install': PostInstallCommand,
    },
    entry_points={'console_scripts': [
        'git-create-profile=git_profile_manager.commands.create_profile:cmd',
        'git-remove-profile=git_profile_manager.commands.remove_profile:cmd',
        'git-list-profiles=git_profile_manager.commands.list_profiles:cmd',
        'git-use-profile=git_profile_manager.commands.use_profile:cmd',
        'git-global-config=git_profile_manager.commands.global_config:cmd',
        'git-current-profile=git_profile_manager.commands.current_profile:cmd',
        'git-apply-profile=git_profile_manager.commands.apply_profile:cmd',
    ]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>={}.{}'.format(*REQUIRED_PYTHON),
)
