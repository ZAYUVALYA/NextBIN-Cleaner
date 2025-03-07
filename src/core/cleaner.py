import subprocess
import os
import shutil

class Cleaner:
    @staticmethod
    def get_cleanable_sizes():
        """Menghitung ukuran total dari cache yang bisa dibersihkan."""
        return {
            "browser_cache": Cleaner.get_browser_cache_size(),
            "apt_cache": Cleaner.get_apt_cache_size(),
            "thumbnail_cache": Cleaner.get_thumbnail_cache_size(),
            "old_kernels": Cleaner.get_old_kernel_size()
        }

    @staticmethod
    def get_browser_cache_size():
        """Menghitung ukuran cache browser dari Firefox dan Chrome."""
        total_size = 0
        browser_paths = [
            os.path.expanduser("~/.cache/mozilla/firefox/"),
            os.path.expanduser("~/.cache/google-chrome/"),
            os.path.expanduser("~/.cache/chromium/")
        ]
        
        for path in browser_paths:
            if os.path.exists(path):
                total_size += Cleaner.get_folder_size(path)
        
        return total_size

    @staticmethod
    def get_apt_cache_size():
        """Menghitung ukuran cache APT."""
        try:
            result = subprocess.run(["du", "-sb", "/var/cache/apt/archives"], capture_output=True, text=True)
            size = int(result.stdout.split()[0]) if result.stdout else 0
            return size
        except Exception as e:
            print(f"Error checking APT cache size: {e}")
            return 0

    @staticmethod
    def get_thumbnail_cache_size():
        """Menghitung ukuran cache thumbnail pengguna."""
        try:
            home = os.path.expanduser("~")
            thumbnail_path = os.path.join(home, ".cache/thumbnails")
            return Cleaner.get_folder_size(thumbnail_path)
        except Exception as e:
            print(f"Error checking thumbnail cache size: {e}")
            return 0

    @staticmethod
    def get_old_kernel_size():
        """Menghitung total ukuran old kernels yang bisa dihapus."""
        try:
            result = subprocess.run(["dpkg", "--list"], capture_output=True, text=True)
            current_kernel = subprocess.run(["uname", "-r"], capture_output=True, text=True).stdout.strip()

            old_kernels = [
                line.split()[1] for line in result.stdout.splitlines()
                if "linux-image-" in line and current_kernel not in line
            ]

            if not old_kernels:
                return 0  # Tidak ada old kernel

            return len(old_kernels) * 150 * 1024 * 1024  # Estimasi 150MB per kernel
        except Exception as e:
            print(f"Error checking old kernels: {e}")
            return 0

    @staticmethod
    def clean_selected(options):
        """Menghapus cache berdasarkan opsi yang dipilih pengguna."""
        if options.get("browser_cache", False):
            Cleaner.clean_browser_cache()
        if options.get("apt_cache", False):
            Cleaner.clean_apt_cache()
        if options.get("thumbnail_cache", False):
            Cleaner.clean_thumbnail_cache()
        if options.get("old_kernels", False):
            Cleaner.clean_old_kernels()

    @staticmethod
    def clean_browser_cache():
        """Menghapus cache browser."""
        browser_paths = [
            os.path.expanduser("~/.cache/mozilla/firefox/"),
            os.path.expanduser("~/.cache/google-chrome/"),
            os.path.expanduser("~/.cache/chromium/")
        ]
        
        for path in browser_paths:
            if os.path.exists(path):
                try:
                    shutil.rmtree(path)
                    print(f"Browser cache cleaned: {path}")
                except Exception as e:
                    print(f"Error cleaning {path}: {e}")

    @staticmethod
    def clean_apt_cache():
        """Membersihkan cache APT menggunakan pkexec agar meminta password sudo."""
        try:
            subprocess.run(["pkexec", "apt-get", "clean"], check=True)
            print("APT cache cleaned.")
        except subprocess.CalledProcessError as e:
            print(f"Error cleaning APT cache: {e}")

    @staticmethod
    def clean_thumbnail_cache():
        """Menghapus cache thumbnail pengguna."""
        try:
            home = os.path.expanduser("~")
            thumbnail_path = os.path.join(home, ".cache/thumbnails")
            shutil.rmtree(thumbnail_path)
            print("Thumbnail cache cleaned.")
        except Exception as e:
            print(f"Error cleaning thumbnails: {e}")

    @staticmethod
    def clean_old_kernels():
        """Menghapus kernel lama yang tidak digunakan."""
        try:
            result = subprocess.run(["dpkg", "--list"], capture_output=True, text=True)
            current_kernel = subprocess.run(["uname", "-r"], capture_output=True, text=True).stdout.strip()

            old_kernels = [
                line.split()[1] for line in result.stdout.splitlines()
                if "linux-image-" in line and current_kernel not in line
            ]

            if not old_kernels:
                print("No old kernels to remove.")
                return

            # Hapus setiap old kernel
            for kernel in old_kernels:
                subprocess.run(["pkexec", "apt-get", "-y", "purge", kernel], check=True)
                print(f"Removed old kernel: {kernel}")

        except Exception as e:
            print(f"Error cleaning old kernels: {e}")

    @staticmethod
    def get_folder_size(path):
        """Menghitung ukuran total folder dalam byte."""
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                if os.path.exists(fp):
                    total_size += os.path.getsize(fp)
        return total_size
