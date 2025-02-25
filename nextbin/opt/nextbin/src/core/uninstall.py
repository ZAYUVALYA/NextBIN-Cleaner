import subprocess

class UninstallManager:
    @staticmethod
    def get_installed_packages():
        """Retrieve the list of installed applications on the system."""
        try:
            result = subprocess.run(["dpkg-query", "-W", "-f=${Package}\n"], capture_output=True, text=True, check=True)
            return result.stdout.splitlines()
        except subprocess.CalledProcessError:
            return []

    @staticmethod
    def run_with_sudo(command):
        """Run a command with pkexec to request sudo password through GUI."""
        subprocess.run(["pkexec"] + command, check=False)

    @staticmethod
    def uninstall_package(package_name):
        """Uninstall an application with GUI sudo prompt and clean up unused dependencies."""
        if package_name:
            try:
                UninstallManager.run_with_sudo(["apt", "remove", "--purge", package_name, "-y"])
                UninstallManager.run_with_sudo(["apt", "autoremove", "-y"])
                print(f"{package_name} has been successfully uninstalled.")
            except subprocess.CalledProcessError as e:
                print(f"Error uninstalling {package_name}: {e}")
