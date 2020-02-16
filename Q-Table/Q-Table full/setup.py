from cx_Freeze import setup, Executable

base = None

executables = [Executable("tictactoe.py", base=base)]

includefiles = ['QTable.csv']
includes = ['numpy']

setup(
    name="TicTacToe",
    options={
        'build_exe': {'includes': includes, 'include_files': includefiles}},
    version="1.0",
    description='Testing',
    executables=executables
)
