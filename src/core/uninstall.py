import subprocess

class UninstallManager:
    @staticmethod
    def get_installed_packages():
        try:
            result = subprocess.run(["dpkg-query", "-W", "-f=${Package}\n"], capture_output=True, text=True, check=True)
            return result.stdout.splitlines()
        except subprocess.CalledProcessError:
            return []

    @staticmethod
    def uninstall_package(package_name):
        if package_name:
            try:
                subprocess.run(["sudo", "apt", "remove", "--purge", package_name, "-y"], check=True)
                subprocess.run(["sudo", "apt", "autoremove", "-y"], check=True)
                print(f"{package_name} has been successfully uninstalled.")
            except subprocess.CalledProcessError as e:
                print(f"Error uninstalling {package_name}: {e}")
