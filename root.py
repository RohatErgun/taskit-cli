from core.database import init_db
from CLI.main import TaskCLI


def main():
    init_db()
    TaskCLI().run()


if __name__ == "__main__":
    main()