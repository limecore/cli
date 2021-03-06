from argparse import ArgumentParser, Namespace


class Command:
    @classmethod
    def create_argument_parser(cls, parser: ArgumentParser, **kwargs) -> None:
        pass

    def run(self, argv: Namespace):
        raise NotImplementedError()
