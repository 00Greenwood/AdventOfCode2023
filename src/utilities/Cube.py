ID = 0


class Cube:
    def __init__(
        self,
        bottom_x: str,
        bottom_y: str,
        bottom_z: str,
        top_x: str,
        top_y: str,
        top_z: str,
        ID: int,
    ) -> None:
        self.ID = ID
        self.bottom_x = int(bottom_x)
        self.bottom_y = int(bottom_y)
        self.bottom_z = int(bottom_z)
        self.top_x = int(top_x)
        self.top_y = int(top_y)
        self.top_z = int(top_z)

    def __str__(self) -> str:
        return f"{self.ID}"
