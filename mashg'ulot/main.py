def hisobla_yigindi(*sonlar: int | float) -> int | float:
    """Istalgancha son qabul qilib, ularning yig'indisini qaytaradi."""
    if not sonlar:
        return 0
    return sum(sonlar)


if __name__ == "__main__":
    natija = hisobla_yigindi(4, 5, 6, 7)
    print(f"Yig'indi: {natija}")