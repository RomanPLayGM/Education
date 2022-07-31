from math import sqrt
print(
    *filter(
        lambda i: all(
            map(
                lambda x: i % x != 0,
                range(2, int(sqrt(i)) + 1)
            )
        )
        , range(
            2, int(input()) + 1
        )
    )
)
