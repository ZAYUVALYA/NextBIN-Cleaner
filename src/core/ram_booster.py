import psutil
import subprocess
from PyQt6.QtWidgets import QMessageBox

class RAMBooster:
    @staticmethod
    def get_ram_status():
        """Mengambil informasi RAM total dan RAM yang sedang digunakan."""
        ram = psutil.virtual_memory()
        total_ram = round(ram.total / (1024**3), 2)  # Convert ke GB
        used_ram = round(ram.used / (1024**3), 2)    # Convert ke GB
        return total_ram, used_ram

    @staticmethod
    def clear_cache():
        """Membersihkan cache RAM tanpa menghentikan proses yang berjalan."""
        try:
            subprocess.run(["pkexec", "sh", "-c", "sync; echo 3 > /proc/sys/vm/drop_caches"], check=True)
            QMessageBox.information(None, "RAM Booster", "RAM cache has been cleared successfully!")
        except subprocess.CalledProcessError as e:
            QMessageBox.critical(None, "Error", f"Failed to clear RAM cache: {e}")
