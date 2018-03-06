print(
    any(
        map(
            lambda x: x == 0,
            map(
                int,
                map(
                    lambda x: input(),
                    range(
                        int(input())
                    )
                )
            )
        )
    )
)
