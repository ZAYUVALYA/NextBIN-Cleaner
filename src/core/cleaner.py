import os
import subprocess

class Cleaner:
    @staticmethod
    def get_directory_size(path):
        """Menghitung total ukuran direktori dalam MB."""
        if not os.path.exists(path):
            return 0
        total_size = 0
        for dirpath, _, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return round(total_size / (1024**2), 2)  # Konversi ke MB

    @staticmethod
    def get_cache_sizes():
        """Mengembalikan ukuran cache browser, APT cache, dan thumbnail cache."""
        return {
            "browser_cache": Cleaner.get_directory_size(os.path.expanduser("~/.cache/mozilla/firefox/")) +
                             Cleaner.get_directory_size(os.path.expanduser("~/.config/google-chrome/Default/Cache")),
            "apt_cache": Cleaner.get_directory_size("/var/cache/apt/archives"),
            "thumbnail_cache": Cleaner.get_directory_size(os.path.expanduser("~/.cache/thumbnails"))
        }

    @staticmethod
    def get_old_kernel_size():
        """Menghitung ukuran old kernel yang bisa dihapus."""
        try:
            result = subprocess.run(["dpkg", "-l", "|", "grep", "-E", "'linux-image-[0-9]+'"], capture_output=True, text=True, shell=True)
            if not result.stdout:
                return 0
            return len(result.stdout.splitlines()) * 150  # Perkiraan ukuran kernel lama (150MB per kernel)
        except Exception:
            return 0

    @staticmethod
    def get_cleanable_sizes():
        """Mengembalikan total ukuran file yang bisa dihapus."""
        sizes = Cleaner.get_cache_sizes()
        sizes["old_kernels"] = Cleaner.get_old_kernel_size()
        return sizes

    @staticmethod
    def clean_selected(options):
        """Menjalankan proses pembersihan sesuai dengan pilihan user."""
        if options.get("browser_cache"):
            subprocess.run(["rm", "-rf", os.path.expanduser("~/.cache/mozilla/firefox/"), os.path.expanduser("~/.config/google-chrome/Default/Cache")], check=False)
        if options.get("apt_cache"):
            subprocess.run(["sudo", "apt", "clean"], check=False)
        if options.get("thumbnail_cache"):
            subprocess.run(["rm", "-rf", os.path.expanduser("~/.cache/thumbnails")], check=False)
        if options.get("old_kernels"):
            subprocess.run(["sudo", "apt", "autoremove", "--purge", "-y"], check=False)
