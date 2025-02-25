import os
import subprocess

class Cleaner:
    @staticmethod
    def get_directory_size(path):
        """Calculate the total size of a directory in MB."""
        if not os.path.exists(path):
            return 0
        total_size = 0
        for dirpath, _, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return round(total_size / (1024**2), 2)

    @staticmethod
    def get_cache_sizes():
        """Return the size of caches that can be deleted."""
        return {
            "browser_cache": Cleaner.get_directory_size(os.path.expanduser("~/.cache/mozilla/firefox/")) +
                             Cleaner.get_directory_size(os.path.expanduser("~/.config/google-chrome/Default/Cache")),
            "apt_cache": Cleaner.get_directory_size("/var/cache/apt/archives"),
            "thumbnail_cache": Cleaner.get_directory_size(os.path.expanduser("~/.cache/thumbnails"))
        }

    @staticmethod
    def get_old_kernel_size():
        """Calculate the size of old kernels that can be deleted."""
        try:
            result = subprocess.run(["dpkg", "-l", "|", "grep", "-E", "'linux-image-[0-9]+'"], capture_output=True, text=True, shell=True)
            if not result.stdout:
                return 0
            return len(result.stdout.splitlines()) * 150  # Estimate 150MB per old kernel
        except Exception:
            return 0

    @staticmethod
    def get_cleanable_sizes():
        """Return the total size of files that can be deleted."""
        sizes = Cleaner.get_cache_sizes()
        sizes["old_kernels"] = Cleaner.get_old_kernel_size()
        return sizes

    @staticmethod
    def run_with_sudo(command):
        """Run a command with pkexec to request sudo password through GUI."""
        subprocess.run(["pkexec"] + command, check=False)

    @staticmethod
    def clean_selected(options):
        """Run cleaning based on user selection."""
        if options.get("browser_cache"):
            subprocess.run(["rm", "-rf", os.path.expanduser("~/.cache/mozilla/firefox/"), os.path.expanduser("~/.config/google-chrome/Default/Cache")], check=False)
        if options.get("apt_cache"):
            Cleaner.run_with_sudo(["apt", "clean"])
        if options.get("thumbnail_cache"):
            subprocess.run(["rm", "-rf", os.path.expanduser("~/.cache/thumbnails")], check=False)
        if options.get("old_kernels"):
            Cleaner.run_with_sudo(["apt", "autoremove", "--purge", "-y"])
