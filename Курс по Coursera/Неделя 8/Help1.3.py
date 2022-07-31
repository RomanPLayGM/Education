print(
    any(
        map(
            lambda x: x == 0,
            map(
                int,
                open('input.txt').read().split()[1:]
            )
        )
    )
)
