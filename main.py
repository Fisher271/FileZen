from organize_files import organize_files
from sort_by_date import sort_by_year_and_month
import sys
sys.stdout.reconfigure(encoding='utf-8')


def main():
    print("Виберіть дію")
    print("1. Сортувати за типами файлів")
    print("2. Сортувати за роками і місяцями")

    choice = input("Введіть ваш вибір (1 або 2): ")
    folder_path = input("Введіть шлях до папки, яку потрібно впорядкувати: ")

    if choice == "1":
        organize_files(folder_path)
    elif choice == "2":
        sort_by_year_and_month(folder_path)
    else:
        print("Невірний вибір. Спробувати ще раз.")


if __name__ == "__main__":
    main()
