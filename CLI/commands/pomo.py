from CLI.commands.base import Command


class PomoCommand(Command):
    name = "pomo"
    help = "enter pomodoro functionality"

    def handle(self, args, service):
        service.pomo()
