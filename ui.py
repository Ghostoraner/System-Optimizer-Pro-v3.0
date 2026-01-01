import os
import sys
import time
from colors import Colors

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def draw_header():
    clear_screen()
    print(f"""
{Colors.HEADER}{Colors.BOLD}
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║          SYSTEM OPTIMIZER PRO v3.0 - ULTIMATE CLEAN         ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
{Colors.ENDC}""")

def animate_progress_bar(duration, message):
    items = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    start_time = time.time()
    i = 0
    while time.time() - start_time < duration:
        print(f"\r{Colors.OKCYAN}{message} {items[i % len(items)]}{Colors.ENDC}", end="")
        sys.stdout.flush()
        time.sleep(0.2)
        i += 1
    print(f"\r{Colors.OKGREEN}{message} [■■■■■■■■■■] ГОТОВО!{Colors.ENDC}")

def fake_scan():
    print(f"\n{Colors.BOLD}Запуск системного анализа...{Colors.ENDC}")
    time.sleep(1)
    animate_progress_bar(2, "Сканирование реестра на ошибки...")
    time.sleep(0.5)
    animate_progress_bar(2, "Анализ временных файлов...")
    time.sleep(0.5)
    animate_progress_bar(2, "Проверка фрагментации диска...")
    time.sleep(0.5)
    animate_progress_bar(2, "Поиск неиспользуемых DLL...")
    time.sleep(0.5)
    print(f"\n{Colors.WARNING}ОБНАРУЖЕНЫ ПРОБЛЕМЫ:{Colors.ENDC}")
    print(" - Найдено 15,842 ошибки в реестре")
    print(" - Обнаружено 3.2 ГБ мусорных файлов")
    print(" - Фрагментация диска: 78% (КРИТИЧЕСКАЯ)")
    print(" - 156 устаревших драйверов")
    time.sleep(2)

def fake_optimize():
    print(f"\n{Colors.BOLD}Применение исправлений и оптимизация...{Colors.ENDC}")
    time.sleep(1)
    animate_progress_bar(3, "Очистка реестра...")
    time.sleep(0.5)
    animate_progress_bar(3, "Дефрагментация системных файлов...")
    time.sleep(0.5)
    animate_progress_bar(3, "Оптимизация памяти...")
    time.sleep(0.5)
    animate_progress_bar(3, "Применение твиков производительности...")
