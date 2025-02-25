import psutil
import subprocess
from PyQt6.QtWidgets import QMessageBox

class BatteryManager:
    SYSTEM_PROCESSES = ["systemd", "dbus-daemon", "pulseaudio", "gnome-shell", "snapd", "Xorg"]

    @staticmethod
    def get_battery_status():
        battery = psutil.sensors_battery()
        if battery:
            return {
                "percentage": battery.percent,
                "plugged": battery.power_plugged
            }
        return None

    @staticmethod
    def get_running_apps():
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
    def set_power_plan(mode):
        try:
            if mode == "Battery Saver":
                subprocess.run(["powerprofilesctl", "set", "power-saver"], check=False)
                subprocess.run(["sudo", "tlp", "bat"], check=False)
                subprocess.run(["sudo", "cpufreq-set", "-g", "powersave"], check=False)

            elif mode == "Balanced":
                subprocess.run(["powerprofilesctl", "set", "balanced"], check=False)
                subprocess.run(["sudo", "tlp", "auto"], check=False)
                subprocess.run(["sudo", "cpufreq-set", "-g", "ondemand"], check=False)

            elif mode == "Performance":
                subprocess.run(["powerprofilesctl", "set", "performance"], check=False)
                subprocess.run(["sudo", "tlp", "ac"], check=False)
                subprocess.run(["sudo", "cpufreq-set", "-g", "performance"], check=False)

        except Exception as e:
            print(f"Failed to change power plan: {e}")
