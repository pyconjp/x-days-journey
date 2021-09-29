from argparse import ArgumentParser, RawDescriptionHelpFormatter

from xdays_journey import あと何日

description = """あなたのXデーまであと何日かを表示

デフォルトではPyCon JP 2021 (2021/10/15) まであと何日かを表示します。"""

parser = ArgumentParser(
    prog="python -m xdays_journey",
    description=description,
    formatter_class=RawDescriptionHelpFormatter,
)
parser.parse_args()

print(あと何日())
