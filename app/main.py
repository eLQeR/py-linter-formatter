
def format_linter_error(error: dict) -> dict:
    return  {
    "line": error["line_number"],
    "column": error["column_number"],
    "message": error["text"],
    "name": error["code"],
    "source": "flake8"
}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {"errors": [format_linter_error(error) for error in errors],
            "path": file_path,
            "status": "failed" if [format_linter_error(error) for error in errors] else "passed"
            }



def format_linter_report(linter_report: dict) -> list:
    return [format_single_linter_file(key, error) for key, error in linter_report.items()]

errors = {
    "./test_source_code_2.py": [],
    "./source_code_2.py": [
        {
            "code": "E501",
            "filename": "./source_code_2.py",
            "line_number": 18,
            "column_number": 80,
            "text": "line too long (99 > 79 characters)",
            "physical_line": '    return f"I like to filter, rounding, doubling, '
            "store and decorate numbers: {', '.join(items)}!\"",
        },
        {
            "code": "W292",
            "filename": "./source_code_2.py",
            "line_number": 18,
            "column_number": 100,
            "text": "no newline at end of file",
            "physical_line": '    return f"I like to filter, rounding, doubling, '
            "store and decorate numbers: {', '.join(items)}!\"",
        },
    ],
    "./source_code_1.py": [
        {
            "code": "E702",
            "filename": "./source_code_1.py",
            "line_number": 3,
            "column_number": 74,
            "text": "multiple statements on one line (semicolon)",
            "physical_line": '        new_items = [f"{key} -> {value}" for key, '
            "value in items.items()]; return func(new_items)\n",
        },
        {
            "code": "E501",
            "filename": "./source_code_1.py",
            "line_number": 3,
            "column_number": 80,
            "text": "line too long (97 > 79 characters)",
            "physical_line": '        new_items = [f"{key} -> {value}" for key, '
            "value in items.items()]; return func(new_items)\n",
        },
        {
            "code": "E302",
            "filename": "./source_code_1.py",
            "line_number": 15,
            "column_number": 1,
            "text": "expected 2 blank lines, found 1",
            "physical_line": "def number_filter(func):\n",
        },
        {
            "code": "E303",
            "filename": "./source_code_1.py",
            "line_number": 27,
            "column_number": 1,
            "text": "too many blank lines (6)",
            "physical_line": "@number_filter\n",
        },
        {
            "code": "E501",
            "filename": "./source_code_1.py",
            "line_number": 31,
            "column_number": 80,
            "text": "line too long (99 > 79 characters)",
            "physical_line": '    return f"I like to filter, rounding, doubling, '
            "store and decorate numbers: {', '.join(items)}!\"\n",
        },
    ],
    "./test_source_code_1.py": [
        {
            "code": "E302",
            "filename": "./test_source_code_1.py",
            "line_number": 4,
            "column_number": 1,
            "text": "expected 2 blank lines, found 1",
            "physical_line": "@pytest.mark.parametrize(\n",
        },
        {
            "code": "E501",
            "filename": "./test_source_code_1.py",
            "line_number": 32,
            "column_number": 80,
            "text": "line too long (84 > 79 characters)",
            "physical_line": '            "decorate numbers: 1 -> 2, 2 -> 4, 6 -> 12, -111 -> -222, -50 -> -100!",\n',
        },
        {
            "code": "W292",
            "filename": "./test_source_code_1.py",
            "line_number": 112,
            "column_number": 6,
            "text": "no newline at end of file",
            "physical_line": "    )",
        },
    ],
}

for key in format_linter_report(errors):
    print(key)
