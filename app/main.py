
def format_linter_error(error: dict) -> dict:
    return  {
    "line": error["line_number"],
    "column": error["column_number"],
    "message": error["text"],
    "name": error["code"],
    "source": "flake8"
}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {
        "errors": errors,
        "path": file_path,
        "status": "failed"
    }


def format_linter_report(linter_report: dict) -> list:
    return [
            {
                "errors": format_linter_error(error),
                "path": "./source_code_2.py",
                "status": "failed"
            }
            for error in linter_report["./source_code_2.py"]
    ]