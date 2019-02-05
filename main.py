def h1(text: str) -> str:
    return f'<h1>{text}<h1>'


if __name__ == "__main__":
    something: int = 5

    something_as_title: str = h1(something)

    print(something_as_title)
