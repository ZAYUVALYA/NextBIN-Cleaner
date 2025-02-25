import psutil
import subprocess
from PyQt6.QtWidgets import QMessageBox

class BatteryManager:
    SYSTEM_PROCESSES = ["systemd", "dbus-daemon", "pulseaudio", "gnome-shell", "snapd", "Xorg"]

    @staticmethod
    def get_battery_status():
        """Returns battery status (percentage and charging status)."""
        battery = psutil.sensors_battery()
        if battery:
            return {
                "percentage": battery.percent,
                "plugged": battery.power_plugged
            }
        return None

    @staticmethod
    def get_running_apps():
        """Returns a list of running applications along with their resource usage."""
        processes = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info', 'io_counters']):
            if proc.info['name'] and not any(system_proc in proc.info['name'].lower() for system_proc in BatteryManager.SYSTEM_PROCESSES):
                processes.append({
                    "pid": proc.info['pid'],
                    "name": proc.info['name'],
                    "cpu": proc.info['cpu_percent'],
                    "memory": round(proc.info['memory_info'].rss / (1024**2), 2),  # Convert to MB
                    "disk": proc.info['io_counters'].write_bytes if proc.info['io_counters'] else 0  # Disk Write Bytes
                })
        return processes

    @staticmethod
    def run_with_sudo(command):
        """Executes a command using pkexec to prompt for sudo password via GUI."""
        subprocess.run(["pkexec"] + command, check=False)

    @staticmethod
    def set_power_plan(mode):
        """Changes the power mode according to the user's choice using pkexec."""
        try:
            if mode == "Battery Saver":
                BatteryManager.run_with_sudo(["powerprofilesctl", "set", "power-saver"])
                BatteryManager.run_with_sudo(["tlp", "bat"])
                BatteryManager.run_with_sudo(["cpufreq-set", "-g", "powersave"])
                print("Power mode changed to Battery Saver")

            elif mode == "Balanced":
                BatteryManager.run_with_sudo(["powerprofilesctl", "set", "balanced"])
                BatteryManager.run_with_sudo(["tlp", "auto"])
                BatteryManager.run_with_sudo(["cpufreq-set", "-g", "ondemand"])
                print("Power mode changed to Balanced")

            elif mode == "Performance":
                BatteryManager.run_with_sudo(["powerprofilesctl", "set", "performance"])
                BatteryManager.run_with_sudo(["tlp", "ac"])
                BatteryManager.run_with_sudo(["cpufreq-set", "-g", "performance"])
                print("Power mode changed to Performance")

        except subprocess.CalledProcessError as e:
            print(f"Failed to change power plan: {e}")
            QMessageBox.critical(None, "Error", f"Failed to change power plan: {e}")

    @staticmethod
    def kill_process(pid, parent=None):
        """Stops a process based on PID."""
        try:
            subprocess.run(["kill", "-9", str(pid)], check=True)
            print(f"Process {pid} killed successfully")
        except subprocess.CalledProcessError as e:
            print(f"Failed to kill process {pid}: {e}")
            QMessageBox.critical(parent, "Error", f"Failed to kill process {pid}: {e}")
